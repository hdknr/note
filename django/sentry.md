## インストール
### Debian

~~~bash
$ sudo apt-get install libxml2-dev libxslt1-dev python-dev
$ sudo apt-get install redis-server
~~~

- Wheezy だとredisふるすぎます
~~~
# /etc/apt/sources.list
# backprots を追加
deb http://ftp.jp.debian.org/debian wheezy-backports main
deb-src http://ftp.jp.debian.org/debian wheezy-backports main
~~~

~~~bash
$ sudo apt-get update
$ sudo apt-get -t wheezy-backports install redis-server
~~~

### Django 1.6!

- 専用のVirtualenv
- Django 1.7 でもいける(sentry 7.7.1)

~~~bash
$ pyenv virtualenv sentry
New python executable in /home/vagrant/.anyenv/envs/pyenv/versions/sentry/bin/python2.7
Also creating executable in /home/vagrant/.anyenv/envs/pyenv/versions/sentry/bin/python
~~~


### Redis

- Redisのサーバーをを立ち上げておくこと

### pip でインストール

- [Install](https://sentry.readthedocs.org/en/stable/getting-started/index.html#install-sentry)


~~~bash
$  pip install sentry
~~~

- MySQLを使う

~~~bash
$ pip install -U sentry[mysql]
~~~

## 初期化

~~~
$ sentry init
Configuration file created at '/home/vagrant/.sentry/sentry.conf.py'
~~~

~~~
$ sentry init tracker/settings.py
Configuration file created at 'tracker/settings.py'
~~~

### app/tracker.py

~~~
$ sentry init app/tracker.py
Configuration file created at 'app/tracker.py'
~~~

- app/tracker.py

~~~
DATABASES = {                                                                                                                                                    
    'default': {                                                                    
        'ENGINE': 'django.db.backends.mysql',                                       
        'USER': 'pallet_tracker',                                                   
        'PASSWORD': 'pallet_tracker',                                               
        'NAME': 'pallet_tracker',                                                   
        'HOST': 'localhost',                                                        
    },                                                                              
}                          
~~~

## 最初のマイグレーション

~~~bash

$ SENTRY_CONF=~/projects/pallet/web/app/tracker.py sentry upgrade
~~~

## Web起動

- gunicorn

~~~
$ sentry --config=~/projects/pallet/web/app/tracker.py start

!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!
!! SENTRY_ADMIN_EMAIL is not configured !!
!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!

Running service: 'http'
[2015-07-23 06:21:04 +0000] [6909] [INFO] Starting gunicorn 19.3.0
[2015-07-23 06:21:04 +0000] [6909] [INFO] Listening at: http://0.0.0.0:9000 (6909)
[2015-07-23 06:21:04 +0000] [6909] [INFO] Using worker: sync
[2015-07-23 06:21:04 +0000] [6918] [INFO] Booting worker with pid: 6918
[2015-07-23 06:21:04 +0000] [6919] [INFO] Booting worker with pid: 6919
[2015-07-23 06:21:04 +0000] [6920] [INFO] Booting worker with pid: 6920
~~~

## ジョブキュー起動

- celery

~~~
$ sentry --config=~/projects/pallet/web/app/tracker.py celery worker -B                                    

!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!
!! SENTRY_ADMIN_EMAIL is not configured !!
!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!


 -------------- celery@jessie.local v3.1.18 (Cipater)
---- **** -----
--- * ***  * -- Linux-3.16.0-4-amd64-x86_64-with-debian-8.1
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         sentry:0x7f823458d390
- ** ---------- .> transport:   redis://localhost:6379//
- ** ---------- .> results:     disabled
- *** --- * --- .> concurrency: 1 (prefork)
-- ******* ----
--- ***** ----- [queues]
 -------------- .> alerts           exchange=default(direct) key=alerts
                .> auth             exchange=default(direct) key=auth
                .> cleanup          exchange=default(direct) key=cleanup
                .> counters-0       exchange=counters(direct) key=
                .> default          exchange=default(direct) key=default
                .> email            exchange=default(direct) key=email
                .> events           exchange=default(direct) key=events
                .> options          exchange=default(direct) key=options
                .> search           exchange=default(direct) key=search
                .> sourcemaps       exchange=default(direct) key=sourcemaps
                .> triggers-0       exchange=triggers(direct) key=
                .> update           exchange=default(direct) key=update

[2015-07-23 06:25:16,635: WARNING/MainProcess] celery@jessie.local ready.
~~~

## シェル

~~~
$ sentry --config=~/projects/pallet/web/app/tracker.py shell

!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!
!! SENTRY_ADMIN_EMAIL is not configured !!
!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!

Python 2.7.9 (default, Apr 24 2015, 02:28:37)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

~~~

## supervisor

- [supervisord conf](https://sentry.readthedocs.org/en/stable/getting-started/index.html#configure-supervisord)
- ログはsyslogへ振るのでローテーション考えない

~~~
[program:sentry-web]
directory=/home/vagrant/projects/pallet/web
command=/home/vagrant/.anyenv/envs/pyenv/versions/sentry/bin/sentry --config=/home/vagrant/projects/pallet/web/app/tracker.py start
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-worker]
directory=/home/vagrant/projects/pallet/web
command=/home/vagrant/.anyenv/envs/pyenv/versions/sentry/bin/sentry --config=/home/vagrant/projects/pallet/web/app/tracker.py celery worker -B
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog
~~~

## Raven Python

- [Doc](https://raven.readthedocs.org/en/latest/)

~~~bash
$ pip install raven --upgrade
~~~

- アクセス方法は、　sentryの Web管理画面にアクセスして /docs/platforms/python/, /docs/platforms/django/  をみる

### Django 設定

- 設定

~~~
try:
    import tracker
    DATABASES['tracker'] = tracker.DATABASES['default']
    RAVEN_CONFIG = {
        'dsn': 'http://{0}:{1}@{2}:{3}/{4}'.format(
            'f2dd9ab507b346f59160a6c036246816',
            '3df64af47a964d6fa15ca41a5d53c852',
            'wp.deb', '9000', '2')
    }

    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )
except:
    pass
~~~

- テスト

~~~
$ python manage.py raven test
Client configuration:
  base_url       : http://wp.deb:9000
  project        : 2
  public_key     : f2dd9ab507b346f59160a6c036246816
  secret_key     : 3df64af47a964d6fa15ca41a5d53c852

Sending a test message... Event ID was 'ca09576835824c5fb7dc4333fab14c55'
~~~

- Webで確認 (sentry/pallet/group/1/ とか)
- シェルで確認

~~~py
>>> from sentry.models import *
>>> Event.objects.filter(project__name='pallet')
[<Event at 0x7fe3649a3350: id=1L, project_id=2L, group_id=1L>]
>>> e =Event.objects.filter(project__name='pallet')[0]
>>> print e.message
This is an example Python exception

>>> e.project
<Project at 0x7fe363a1b790: id=2L, team_id=2L, slug=u'pallet'>
>>> e.project.team
<Team at 0x7fe363a1b910: id=2L, slug=u'pallet', owner_id=None, name=u'Pallet'>

~~~


## Bad Request(400)

- Django の問題

~~~py
ALLOWED_HOSTS = ['wp.deb', 'localhost', 'yourdomain.com', '127.0.0.1', ]
~~~
