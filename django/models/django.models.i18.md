Django:国際化データの格納案

- 複数言語あるかもしれないのでフィールド追加ではなくリレーションモデルで保持させる

## settings.py

- 持ちたい言語一覧を設定できるようにする

~~~py
OTHER_LANGUAGE_CODES = ['en', ]
~~~


## models.py

- 国際データを持ちたいモデルと、フィールドの一覧を指定して動的にモデルを定義する

~~~py
I18N_LANG_CHOICES = tuple(
    ln for ln in settings.LANGUAGES if ln[0] in settings.OTHER_LANGUAGE_CODES)


def i18n(cls, *field_names):
    postfix = _('Translation')
    meta = type(
        'Meta', (object, ),
        dict(
            verbose_name="{} {}".format(cls._meta.verbose_name,  postfix),
            verbose_name_plural="{} {}".format(cls._meta.verbose_name_plural, postfix),
            unique_together=(('original', 'lang',),),
        )
    )
    fields = dict(                                                                  
        (name, cls._meta.get_field(name).clone()) for name in field_names)          
                                                                                    
    fields['__module__'] = cls.__module__                                           
    fields['Meta'] = meta                                                           
    fields['original'] = models.ForeignKey(                                         
        cls, verbose_name=cls._meta.verbose_name)                                   
    fields['lang'] = models.CharField(                                              
        _('Language'), choices=I18N_LANG_CHOICES, max_length=10)                    


    return type(cls._meta.object_name + "Trans", (models.Model,), fields)

~~~


### 例

~~~py
class Community(models.Model):
    area = models.CharField(
        _('Community Area'), max_length=10, null=True, default=None, blank=True,)
    name = models.CharField( _('Community Name'), max_length=50,)
    ...
~~~

~~~py
CommunityTrans = i18n(Community, 'area', 'name')
~~~

## admin.py

- インラインで編集できるようにする

~~~py
from django.utils.safestring import mark_safe as _S
from django import template

def _T(src, **ctx):
    return _S(template.Template(src).render(template.Context(ctx)))

def _CHANGE(instance):
    url = 'admin:{0}_change'.format(instance._meta.db_table)
    return _T('''<a href="{% url u o.id %}">{{o}}</a>''', u=url, o=instance)

class TransAdmin(admin.ModelAdmin):
    raw_id_fields = ('original', )

    def original_link(self, obj):
        return _CHANGE(obj.original)

    original_link.short_description = _('Original Model')
    original_link.allow_tags = True
~~~

~~~py
class CommunityTransAdmin(TransAdmin):
    pass

class CommunityTransAdminInline(admin.StackedInline):
    model = models.CommunityTrans
    extra = 0

class CommunityAdmin(admin.ModelAdmin):
    inlines = [CommunityTransAdminInline, ]
    ...
~~~

## テンプレートタグ

- 指定したモデルに Trans モデルがあったら、現在の言語で探す
- 見つかったら 指定されたフィールドの値を返す
- なかったら元のモデルのフィールドの値を返す

~~~py
from django import template
from django.utils import translation
register = template.Library()


@register.simple_tag
def trans_field(instance, field_name):
    lang = translation.get_language()
    name = instance._meta.object_name + "Trans"
    rels = [
        r for r in instance._meta.get_all_related_objects()
        if r.related_model._meta.object_name == name]
    if rels and lang:
        instance = rels[0].related_model.objects.filter(
            original=instance, lang=lang).first() or instance
    res = getattr(instance, field_name, None)
    return res or ''
~~~

## テンプレート

~~~html

<a href="{{ community.get_absolute_url }}">{% trans_field community 'name' %}</a>
~~~
