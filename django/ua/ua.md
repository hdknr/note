Django: User Agentを記録してAdminで管理

# Project作成

- GET /accounts/login でログインフォームを出す
- POST /accounts/login でログインし、/accounts/profile/ にリダイレクト
- GET /accounts/profile で個人情報表示

## startproject

~~~
(v17)hdknr@wzy:~/ve/v17/src$ mkdir -p ua/web
(v17)hdknr@wzy:~/ve/v17/src$ django-admin startproject app ua/web
(v17)hdknr@wzy:~/ve/v17/src$ cd ua/web
~~~

~~~
(v17)hdknr@wzy:~/ve/v17/src/ua/web$ python manage.py migrate
(v17)hdknr@wzy:~/ve/v17/src/ua/web$ python manage.py createsuperuser
~~~

## accounts 追加

~~~
(v17)hdknr@wzy:~/ve/v17/src/ua/web$ python manage.py startapp accounts
~~~

### app/settings.py

~~~
INSTALLED_APPS += (
    'accounts',
)
~~~

### app/urls.py


~~~
    url(r'^accounts/', include('accounts.urls')),
~~~

### accounts/urls.py


~~~
from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'login/$', 'django.contrib.auth.views.login'),
    url(r'profile/$', views.profile),
)
~~~


### accounts/views.py


~~~
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

import models


@login_required
def profile(request):
    ua = None
    return TemplateResponse(
        request,
        'registration/profile.html',
        dict(request=request, ua=ua, ))
~~~

### accounts/templates/registration

~~~
(v17)hdknr@wzy:~/ve/v17/src/ua/web$ mkdir -p accounts/templates/registration
~~~

- login.html

~~~
<form method="post">{% csrf_token %}
{{ form.as_p }}
<input type="submit" />
</form>
~~~

- profile.html

~~~
{{ request.user }}
{{ ua }}
~~~

- この時点でログインまで動きます

# UserAgentモデル

## UA判定(accounts/ua.py)

- agent_type() : 正規表現で マッチングする agentを見つける

~~~
import re


DETECTOR = [
    # Featured Phone
    r'(?P<agent>DoCoMo)',
    r'(?P<agent>SoftBank)',
    r'^(?P<agent>KDDI)',     # if no KDDI, HDML browser.
    r'(?P<agent>Vodafone)',

    ....
]


def agent_type(agent_string):
    for d in DETECTOR:
        m = re.search(d, agent_string, flags=re.IGNORECASE)
        m = m and m.groupdict() or {}
        if m:
            return m['agent'].lower().replace('-', '').replace(' ', '')
    return "generic"
~~~    


## モデル(accounts/models.py)

~~~
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from ua import agent_type
import hashlib

class UserAgent(models.Model):
    agent = models.CharField(
        _(u'User Agent'),
        max_length=30, default="PC")
    key = models.CharField(
        _(u'User Agent Header MD5 Hash'),
        max_length=40, unique=True, db_index=True,)
    header = models.CharField(
        _(u'User Agent Header'),  max_length=512, )
    users = models.ManyToManyField(
        User, default=None, null=True, blank=True)


    @classmethod
    def get_ua(cls, ua_header, user=None):
        ua, created = cls.objects.get_or_create(
            key=hashlib.md5(ua_header).hexdigest())

        if created:
            ua.agent = agent_type(ua_header)
            ua.header = ua_header
            ua.save()

        if user:
            ua.users.add(user)

        return ua

    def __unicode__(self):
        return "%s(%s)" % (self.agent, getattr(self, 'id', ''))
~~~

## /accounts/profileで記録する(acounts/views.py)

- profile()修正

~~~
@login_required
def profile(request):
    ua = models.UserAgent.get_ua(
        request.META.get('HTTP_USER_AGENT', 'N/A'),
        request.user)

    return TemplateResponse(
        request,
        'registration/profile.html',
        dict(request=request, ua=ua, ))
~~~        

## マイグレート

~~~
(v17)hdknr@wzy:~/ve/v17/src/ua/web$ python manage.py makemigrations accounts
Migrations for 'accounts':
  0001_initial.py:
    - Create model UserAgent
~~~
~~~    
(v17)hdknr@wzy:~/ve/v17/src/ua/web$ python manage.py migrate  accounts
Operations to perform:
  Apply all migrations: accounts
Running migrations:
  Applying accounts.0001_initial... OK
~~~      

## accounts/admin.py

~~~
from django.contrib import admin
import models


class UserAgentAdmin(admin.ModelAdmin):
    list_display = tuple(
        [f.name for f in models.UserAgent._meta.fields
         if f.name not in ['key']]
    )

admin.site.register(UserAgent, UserAgentAdmin)

~~~    

- この時点でUserAgentのAdmin管理できる

# Adminカスタマイズ

## UserAgentAdmin(accounts/admin.py)

###  1. agentフィールドでフィルターする

~~~    
    list_filter = ('agent', )    
~~~

### 2. usersフィールドを編集できないようにする

~~~    
    add_exclude = ('users',)
    edit_exclude = ('users',)

    def add_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'add_exclude', ())
        return super(UserAgentAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'edit_exclude', ())
        return super(UserAgentAdmin, self).change_view(*args, **kwargs)
~~~

### 3. UserAgentでログインしたユーザーの数を表示させ、一覧にリンクさせる

~~~
from django.core.urlresolvers import reverse
~~~

~~~    
    list_display = tuple(
        [f.name for f in models.UserAgent._meta.fields
         if f.name not in ['key']]
    ) + ('users_count',)

    def users_count(self, obj):
        if not obj.users.exists():
            return '0'

        uri = reverse("admin:%s_changelist" % obj.users.model._meta.db_table)
        query = "?useragent__id__exact=%d" % (obj.id)
        return mark_safe(
            u"<a href='%s'>%d Users</a>" % (uri + query, obj.users.count()))

    users_count.allow_tags = True
~~~
    
![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/django/ua/UserAgent.list.png)
    
### 4. usersフィールドを編集させない変わりに、 ログインしたユーザーへのリンクを表示させる

~~~    
    readonly_fields = ('ua_users', )

    def ua_users(self, instance):
        try:
            return ",".join([
                mark_safe('<a href="%s">%s</a>   ' % (
                    reverse("admin:%s_change" % u._meta.db_table, args=[u.id]),
                    u.__unicode__()))
                for u in instance.users.all()])
        except:
            return "errors"

    ua_users.short_description = "UserAgent Users"
    ua_users.allow_tags = True
~~~    

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/django/ua/UserAgent.edit.png)
    

## UserAdmin(accounts/admin.py)

- UserからUserAgentのAdmin画面に戻れるようにする

~~~
from django.db.models.manager import Manager
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
~~~

- モデルとそのリレーションフールドが指定されたときに、そのフィールドのAdmin画面に戻れるリンクを作るユーティリティ

~~~
def link_to_relation(self, obj, field=""):
    fobj = obj and getattr(obj, field, None)

    if fobj is None:
        return "No Link"

    if issubclass(fobj.__class__, Manager):
        fobj = fobj.all()
    else:
        fobj = [fobj, ]

    return mark_safe("<br/>".join([
        '<a href="%s">%s</a>' % (
            reverse("admin:%s_change" % ln._meta.db_table, args=[ln.id]),
            ln.__unicode__()
        ) for ln in fobj]))
~~~        

- Userオブジェクトとuseragent_set でバックリンクを作る

~~~
useragent_link = lambda self, obj: link_to_relation(self, obj, "useragent_set")
useragent_link.short_description = u"User Agent"
useragent_link.allow_tags = True
~~~

- これをUserAdminに追加してやる

~~~
UserAdmin.list_display = tuple(
    set(UserAdmin.list_display + ('useragent_link', )))
UserAdmin.useragent_link = useragent_link
~~~

- さらにUserAdminでUserAgent#agentでフィルタリングできるようにする

~~~
UserAdmin.list_filter = UserAdmin.list_filter + ('useragent__agent',)
~~~

- これで戻れる

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/django/ua/User.list.png)

