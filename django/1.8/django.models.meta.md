

## Model._meta API

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#model-meta-api)
- [トピック](https://docs.djangoproject.com/en/1.8/ref/models/meta/#model-meta-field-api)
- 公式API化(0.96以前からあるけど)

### many_to_many, many_to_one

~~~
>>> from django.contrib.auth.models import *
>>> Group._meta.get_field('permissions').many_to_many
True
>>> Group._meta.get_field('permissions').many_to_one
False
>>> Permission._meta.get_field('content_type').many_to_one
True
>>> Permission._meta.get_field('content_type').many_to_many
False
~~~

### one_to_one, one_to_many

~~~
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation)
from django.contrib.contenttypes.models import ContentType


class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Profile(models.Model):
    user = models.OneToOneField(User)
    tags = GenericRelation(TaggedItem)
~~~

~~~
>>> from accounts.models import *
>>> Profile._meta.get_field('user').one_to_one
True

>>> Profile._meta.get_field('tags').one_to_many
True
~~~

### get_fields()

~~~
>>> set(TaggedItem._meta.get_fields(include_hidden=True)) - set(TaggedItem._meta.get_fields())
set([<GenericRel: accounts.profile>])
~~~

## テンプレートエンジン

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#multiple-template-engines)
- [トピック](https://docs.djangoproject.com/en/1.8/topics/templates/)
- デフォルトでJinja2も使える

デフォルトの settings.py

~~~
TEMPLATES = [                                                                       
    {                                                                               
        'BACKEND': 'django.template.backends.django.DjangoTemplates',               
        'DIRS': [],                                                                 
        'APP_DIRS': True,                                                           
        'OPTIONS': {                                                                
            'context_processors': [                                                 
                'django.template.context_processors.debug',                         
                'django.template.context_processors.request',                       
                'django.contrib.auth.context_processors.auth',                      
                'django.contrib.messages.context_processors.messages',              
            ],                                                                      
        },                                                                          
    },                                                                              
]        
~~~

## セキュリティ

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#security-enhancements)
- [django-secure](https://pypi.python.org/pypi/django-secure) を取り入れ
- [SecurityMiddleware](https://docs.djangoproject.com/en/1.8/ref/middleware/#django.middleware.security.SecurityMiddleware) 改善
- [manage.py check --deply](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-option---deploy)

## PostgreSQL

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#new-postgresql-specific-functionality)
- [ArrayField](https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/fields/#django.contrib.postgres.fields.ArrayField)
- [HStoreField](https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/fields/#django.contrib.postgres.fields.HStoreField) - pythond dict
- [unaccentルックアップ](https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/lookups/#std:fieldlookup-unaccent)
- [トピック](https://docs.djangoproject.com/en/1.8/ref/contrib/postgres/)

## データタイプ

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#new-data-types)
- [models.UUIDField](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.UUIDField)
- [forms.UUIDField](https://docs.djangoproject.com/en/1.8/ref/forms/fields/#django.forms.UUIDField)
- [Duration](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.DurationField) - python [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta)

## クエリとかデータ関連

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#query-expressions-conditional-expressions-and-database-functions)
- [Query表現](https://docs.djangoproject.com/en/1.8/ref/models/expressions/)
- [条件表現](https://docs.djangoproject.com/en/1.8/ref/models/conditional-expressions/)
- [データベース関数](https://docs.djangoproject.com/en/1.8/ref/models/database-functions/)

## TestCase データ

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#testcase-data-setup)
- [TestCase.setUpTestData()](https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.TestCase.setUpTestData)

## django.contrib.admin

- [リリースノート](https://docs.djangoproject.com/en/1.8/releases/1.8/#django-contrib-admin)
- [ModelAdmin.has_module_permission(request)](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.has_module_permission)
- [InlineModelAdmin.show_change_link](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin.show_change_link)
- [ModelAdmin.list_filter](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter) - リレーション先でフィルター
- [ModelAdmin.delete_view(request, object_id, extra_context=None)](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.delete_view) - 削除確認画面
- [AdminSite.site_url](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.AdminSite.site_url) - サイトのURL(デフォルト'/')
- [ModelAdmin.show_full_result_count](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.show_full_result_count) - 全件数を出さないようにできる(パフォーマンス改善)
- Admin UIへのパーミッション設定( [AdminSite.has_permission(request)](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.AdminSite.has_permission), [AdminSite.login_form](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.AdminSite.login_form) )

