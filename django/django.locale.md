~~~
>>> import locale                                                                                                                                                              
>>> locale.setlocale(locale.LC_NUMERIC,'ja')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/locale.py", line 579, in setlocale
    return _setlocale(category, locale)
Error: unsupported locale setting
~~~

~~~
$ locale -a
C
C.UTF-8
en_US.utf8
POSIX

~~~


~~~
# dpkg-reconfigure locales
~~~

~~~
ja_JP.UTF-8 UTF-8

Generating locales (this might take a while)...
  en_US.UTF-8... done
  ja_JP.UTF-8... done
Generation complete.
~~~

~~~
$ locale -a
C
C.UTF-8
en_US.utf8
ja_JP.utf8
POSIX
~~~

~~~
>>> import locale
>>> locale.setlocale(locale.LC_NUMERIC,'ja')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/locale.py", line 579, in setlocale
    return _setlocale(category, locale)
Error: unsupported locale setting
>>> locale.setlocale(locale.LC_NUMERIC,'ja_JP.utf8')
'ja_JP.utf8'
~~~

~~~
>>> from dolphin.models import *
>>> Material._meta.get_field_by_name('price')
(<django.db.models.fields.DecimalField: price>, None, True, False)
>>> Material._meta.get_field_by_name('price')[0]
<django.db.models.fields.DecimalField: price>
>>> f = _
>>> f.to_python('1,000.00')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/site-packages/django/db/models/fields/__init__.py", line 1602, in to_python
    params={'value': value},
ValidationError: [u"'1,000.00' value must be a decimal number."]
>>> f.to_python('1000.00')
Decimal('1000.00')
~~~

~~~
>>> import locale
>>> locale.atof('1,000')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/locale.py", line 316, in atof
    return func(string)
ValueError: invalid literal for float(): 1,000
>>> locale.setlocale(locale.LC_ALL, '')
'en_US.UTF-8'
>>> locale.atof('1,000')
1000.0
~~~