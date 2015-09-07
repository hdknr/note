## テンプレートメール

- django のテンプレートを作成
- テンプレートローダーがローディングできる場所に置く
- テンプレート名でデータベースを探してなかったらローダーから読み込んで保存(デプロイ)
- 存在したらそれを使う。以降は(管理画面とか)サイトで修正可能
- `send(**kwargs)` に渡された変数がテンプレートに反映される
- テンプレートはDjangoが処理できるテンプレート言語を使える

~~~py
from django import VERSION
from django import template
from django.db import models
from django.conf import settings
from django.core.mail.message import SafeMIMEText
from email import Charset
import os
import io
import uuid

from paloma import (
    tasks, mails,
    models as paloma_models)


__all__ = ['get_template_source', 'Template', ]

if VERSION < (1, 8):
    def get_template_loaders():
        from django.template import loader
        return tuple(
            loader.find_template_loader(i)
            for i in settings.TEMPLATE_LOADERS
        )
else:
    def get_template_loaders():
        from django.template import engine
        return engine.Engine.get_default().template_loaders


def get_template_source(name):
    '''
    :rtype: tuple(source text, path)
    '''
    for loader in get_template_loaders():
        try:
            return loader.load_template_source(name)
        except:
            pass
    return (None, None)


def create_message(
  addr_from='me@localhost',
  addr_to='you@localhost',
  message_id=None,
  subject='subject',
  body='body',
  subtype='plain', encoding="utf-8"
  ):
    ''' Creating Message
    :rtype: SafeMIMTExt(MIMEMixin, email.mime.text.MIMETex)
    - `as_string()` method serializes into string
    '''

    message_id = message_id or uuid.uuid1().hex
    if encoding == "shift_jis":
      #: DoCoMo
      #: TODO chekck message encoding and convert it
      Charset.add_charset(
        'shift_jis', Charset.QP, Charset.BASE64, 'shift_jis')
      Charset.add_codec('shift_jis', 'cp932')

    message = SafeMIMEText(body, subtype, encoding)
    message['Subject'] = subject
    message['From'] = addr_from
    message['To'] = addr_to
    message['Message-ID'] = message_id

    return message

def send_raw_message(
    return_path, recipients,
    raw_message, *args, **kwargs):
    '''
    Send email using SMTP backend
    :param str return_path: the Envelope From address
    :param list(str) recipients: the Envelope To address
    :param str raw_message:
    string expression of Python :py:class:`email.message.Message` object
    '''

    try:
        conn = get_connection(backend=BACKEND)
        conn.open()     # django.core.mail.backends.smtp.EmailBackend
        conn.connection.sendmail(
            return_path, recipients, smart_str(raw_message))
    except Exception, e:
        logger.debug(traceback.format_exc())


class TemplateQuerySet(models.QuerysSet):
    def get_by_name(self, name):
        obj = self.filter(name=name).first()
        if not obj:
            source, path = get_template_source(name)
            text = source or "subject\nbody"
            subject, body = text.split('\n', 1)

            obj = self.create(
                name=name,
                subject=subject, body=body)
        return obj

class Template(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    subject = models.CharField(max_legnth=200)
    body = models.TextField()

    objetcs = TemplateQuerySet.as_manager()

    def subject(self, **kwargs):
        return template.Template(self.subject).render(template.Context(kwargs))

    def body(self, **kwargs):
        return template.Template(self.body).render(template.Context(kwargs))

    def create(self, addr_from='', addr_to='', message_id=None,
               subtype='plain', encoding="utf-8", **kwargs):
        return create_message(
            addr_from=addr_from, addr_to=addr_to, message_id=message_id,
            subtype=subtype, encoding=encoding,
            subject=self.subject(
                addr_from=addr_from, addr_to=addr_to, **kwargs),
            body=self.body(addr_from=addr_from, addr_to=addr_to, **kwargs),)

    def send(self, return_path, recipients,
             addr_from='', addr_to='', message_id=None,
             subtype='plain', encoding="utf-8", **kwargs):
        message = self.create(
            addr_from=addr_from, addr_to=addr_to,
            message_id=message_id, subtype=subtype, encoding=encoding,
            **kwargs)
        send_raw_message(
            return_path, recipients,
            message.as_string())

    def rewrite(self, directory):
        path = os.path.join(directory, self.instance.name)
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with io.open(path, 'w', encoding='utf-8') as out:
            out.write(self.instance.subject + "\n")
            out.write(self.instance.text + "\n")
~~~
