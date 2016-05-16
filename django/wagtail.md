# Wagtail Vagrant PYPI

## Unidecode

- https://pypi.python.org/pypi/Unidecode
- wagtail/wagtailforms/models.py の依存です

## sqlparse

- https://pypi.python.org/pypi/sqlparse
- debug_toolbar の依存です


## unicodecsv

- [https://github.com/jdunck/python-unicodecsv](https://github.com/jdunck/python-unicodecsv)
- wagtail/wagtailforms/views.py
- python csv の代わりで使える


## Django


### django-appconf

- https://github.com/jezdez/django-appconf


### django-compressor

- http://django-compressor.readthedocs.org/en/latest/
- http://www.18th-technote.com/django_compressor


### django-debug-toolbar

- https://github.com/django-debug-toolbar/django-debug-toolbar
- http://qiita.com/seizans/items/ff9da996070105707bcc

### django-libsass

- https://github.com/torchbox/django-libsass
- djago-compressor 必要
- https://github.com/dahlia/libsass-python


### django-modelcluster

- https://pypi.python.org/pypi/django-modelcluster
- https://github.com/torchbox/django-modelcluster

### django-taggit

- http://django-taggit.readthedocs.org/en/latest/

### django-treebeard

- django-treebeard is a library that implements efficient tree implementations for the Django Web Framework 1.4+. It includes 3 different tree implementations: Adjacency List, Materialized Path and Nested Sets.
- https://pypi.python.org/pypi/django-treebeard
- https://github.com/tabo/django-treebeard
- https://tabo.pe/projects/django-treebeard/docs/tip/


## インストール

```
(wagtail-torchbox)vagrant@precise32:~$ mkdir sandbox
(wagtail-torchbox)vagrant@precise32:~/sandbox$ wagtail start lafoglia
Creating a wagtail project called lafoglia
Success! lafoglia is created
```

```
(wagtail-torchbox)vagrant@precise32:~/sandbox$ tree .
.
└── lafoglia
    ├── core
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_create_homepage.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── lafoglia.scss
    │   │   └── js
    │   │       └── lafoglia.js
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── 500.html
    │   │   ├── base.html
    │   │   └── core
    │   │       └── home_page.html
    │   └── templatetags
    │       ├── core_tags.py
    │       └── __init__.py
    ├── lafoglia
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── base.py
    │   │   ├── dev.py
    │   │   ├── __init__.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── readme.rst
    ├── requirements.txt
    ├── vagrant
    │   └── provision.sh
    └── Vagrantfile

12 directories, 25 files

```


## torchbox

### データベース作成

~~~
$ psql -U postgres -h localhost

postgres=# CREATE ROLE vagrant superuser;
CREATE ROLE

postgres=# ALTER ROLE vagrant WITH LOGIN;
ALTER ROLE


postgres=# CREATE DATABASE torchbox;
CREATE DATABASE

postgres=# ALTER DATABASE torchbox OWNER TO vagrant;                                                         
ALTER DATABASE
~~~
