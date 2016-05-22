
# i18n

- [Translation](https://docs.djangoproject.com/ja/1.9/topics/i18n/translation/)
- [How to setup up Django translation in the correct way?](http://stackoverflow.com/questions/20467626/how-to-setup-up-django-translation-in-the-correct-way)
- [LocaleMiddleware](https://docs.djangoproject.com/ja/1.9/ref/middleware/#module-django.middleware.locale)

## ブラウザ言語で切り替える

- settings.py

~~~py
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',                # i18n
    ...
]
# LANGUAGE_CODE = 'ja'
LANGUAGE_CODE = 'en'          # デフォルトを英語とする
~~~

- views.py


~~~py
def detail(request):
  request.LANGUAGE_CODE == 'ja'
  # もしくは
  from django.utils import translation                                        
  print "LANGUAGE :", translation.get_language()        
~~~

- shell

~~~py
In [1]: from django.utils import translation
In [2]: print "LANGUAGE :", translation.get_language()
LANGUAGE : None
~~~

~~~py
In [2]: translation.activate('ja')
In [3]: translation.get_language()
Out[3]: 'ja'
~~~


## CommandError: Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed.

~~~
(tact)$ python ../manage.py  makemessages -l ja
CommandError: Can't find msguniq.
Make sure you have GNU gettext tools 0.15 or newer installed.


(tact)$ brew install gettext
Warning: gettext-0.19.4 already installed


(tact)$ brew link gettext
Warning: gettext is keg-only and must be linked with --force
Note that doing so can interfere with building software.

(tact)$ brew link --force gettext
Linking /usr/local/Cellar/gettext/0.19.4... 189 symlinks created

(tact)$ python ../manage.py makemessages -l ja
processing locale ja
~~~
