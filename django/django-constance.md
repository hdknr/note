## Constance

- [docs](http://django-constance.readthedocs.org/en/latest/#)
- [github](https://github.com/jezdez/django-constance)
- [transifex](https://www.transifex.com/jezdez/django-constance/)

## インストール

~~~bash
$ pip install django-constance
~~~

## 設定

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

## 実行

- 参照

~~~py
In [1]: from constance import config

In [2]: config.THE_ANSWER
Out[2]: 50
~~~

- デフォルトバックエンド = Redis

~~~
In [5]: from constance import settings
In [6]: settings.BACKEND
Out[6]: 'constance.backends.redisd.RedisBackend'
~~~

- redis確認

~~~bash

$ redis-cli keys "const*"
1) "constance:THE_ANSWER"

$ redis-cli get "constance:THE_ANSWER"
"I50\n."
~~~

## バックエンドをデータベース化

- settings.py

~~~
INSTALLED_APPS += (
    'constance',
    'constance.backends.database',
)
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
~~~


~~~bash$
python manage.py migrate database

Operations to perform:
  Apply all migrations: database
Running migrations:
  Rendering model states... DONE
  Applying database.0001_initial... OK
~~~


~~~bash$
echo "select * from constance_config;" | python manage.py dbshell

1|THE_ANSWER|gAJLZC4=

~~~
