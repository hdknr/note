Django: INSTALLED_APPS を動的に変更できるようにする
- Django実行中にアプリを追加するとか

# settings.py : local_settings.py を読みむ

- settings.py の最後に追加

~~~py
try:
    import local_settings
    globals().update(
        dict((k, v) for k, v in local_settings.__dict__.items()
             if not k.startswith('_'))
    )
except:
    pass
~~~    

# local\_settings.py: INSTALLED_APPSを動的に変更

- apps以下にカスタムアプリケーションがある

~~~
(wordpress)vagrant@10:~/projects/dynamics/web$ tree apps
apps
├── app1
│   ├── __init__.py
│   └── __init__.pyc
├── __init__.py
└── __init__.pyc

1 directory, 4 files
~~~

- local_settings.py で設定を修正する

~~~py
CUSTOM_APPS = (
    'dynamics',
   	# ....		# apps.* 以外のカスタムアプリ
)

from django.conf import Settings
from types import MethodType
import os

BASE_DIR = os.path.dirname(
	os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, 'apps')


# 入れ替えメソッド定義
def _attr(self, name):
	# オリジナルの__getattribute__ を呼ぶ
    ret = super(type(self), self).__getattribute__(name)

    # INSTALLED_APPS だったら、 appsディレクトリ以下を追加
    if name == "INSTALLED_APPS":
        return ret + CUSTOM_APPS + tuple(
            "apps.{0}".format(d) for d in os.listdir(APPS_DIR)
            if os.path.isdir(os.path.join(APPS_DIR, d))
        )
    # それ以外は普通に返す
	retrun ret      

# メソッドを入れ替える
Settings.__getattribute__ = MethodType(_attr, None, Settings)
~~~

## データベースに保存

- https://www.djangopackages.com/grids/g/live-setting/

### Constance

- [docs](http://django-constance.readthedocs.org/en/latest/#)
- [github](https://github.com/jezdez/django-constance)

~~~bash
$ pip install django-constance[database]
~~~

- settings.py

~~~py
INSTALLED_APPS += (
    'constance',
)
CONSTANCE_CONFIG = {
    'THE_ANSWER': (
        42,
        'Answer to the Ultimate Question of Life, '
        'The Universe, and Everything'),
}
~~~

~~~py
from constance import config



### Siteprefs

- [django-siteprefs](http://django-siteprefs.readthedocs.org/en/latest/index.html)

- settings.py

~~~py
INSTALLED_APPS += (
  'siteprefs',
)
~~~

~~~bash
$ python manage.py migrate
~~~

- urls.py

~~~py
from siteprefs.toolbox import autodiscover_siteprefs                             
autodiscover_siteprefs()             
~~~

- app/admin.py

~~~py
from siteprefs.models import Preference


class PreferenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Preference, PreferenceAdmin)
~~~~


### Livesettings
- [bkroeze/django-livesettings](https://bitbucket.org/bkroeze/django-livesettings/)
- [docs](https://django-livesettings.readthedocs.org/en/latest/)
- [PYPI](https://pypi.python.org/pypi/django-livesettings)
- [demo](https://bitbucket.org/chris1610/satchmo/src)

keycache:

- [keycache](https://pypi.python.org/pypi/django-keyedcache)
- [django-keyedcache](https://bitbucket.org/bkroeze/django-keyedcache/)

~~~bash
$ pip install django-keyedcache
~~~

- settings.py

~~~py
INSTALLED_APPS += (
    'django.contrib.sites',
    'livesettings',
)
SITE_ID = 1
~~~

### others
- [sciyoshi/django-dbsettings](https://github.com/sciyoshi/django-dbsettings)
