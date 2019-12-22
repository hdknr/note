## プロジェクト

~~~
$ mkdir hellofuel && cd hellofuel
$ which php
/home/vagrant/.anyenv/envs/phpenv/shims/php

$ php -v
PHP 5.6.10 (cli) (built: Jul 28 2015 21:11:18)
Copyright (c) 1997-2015 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2015 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2015, by Zend Technologies
    with Xdebug v2.3.3, Copyright (c) 2002-2015, by Derick Rethans
~~~

- もしかしてComposerはここでインストールしなくていいかも

~~~
$ curl -sS https://getcomposer.org/installer | php    

#!/usr/bin/env php
All settings correct for using Composer
Downloading...

Composer successfully installed to: /vagrant/projects/hellofuel/composer.phar
Use it: php composer.phar
~~~

## oil コマンド

~~~
$ curl get.fuelphp.com/oil | sh  
$ which oil
/usr/bin/oil

~~~

ちなみに /usr/bin/oil

~~~bash
#!/bin/bash

# if we have the oil script in the current directory, start that
if [ -f "./oil" ]; then
        php oil "$@" else

        # check for bash commandline options
        if [ "$1" == "create" ]; then

                # make sure git is installed
                if [ ! `which git` ]; then
                    echo "For this installer to work you'll need to install Git."
                    echo '        http://git-scm.com/'
                fi  

                # clone the repository, and make sure the latest master is active
                git clone --recursive git://github.com/fuel/fuel.git "./$2"
                cd ./$2
                branch=`git branch -a | grep -v "remote" | grep "master" | tail -1`
                branch=${branch#* }
                git checkout $branch
                git submodule foreach git checkout $branch

                # run composer
                php composer.phar self-update
                php composer.phar update

                # fix potential rights issues
                cd ..
                php "./$2/oil" refine install
        else
                echo 'This is not a valid Fuel installation so Oil is a bit lost.'
                echo '        http://fuelphp.com/docs/installation/instructions.html'

        fi  
fi
~~~

## 初期化

~~~
$ oil create hello

Cloning into './hello'...
remote: Counting objects: 15295, done.
remote: Total 15295 (delta 0), reused 0 (delta 0), pack-reused 15295
Receiving objects: 100% (15295/15295), 5.34 MiB | 391.00 KiB/s, done.
Resolving deltas: 100% (6153/6153), done.
Checking connectivity... done.
Already on '1.7/master'
Your branch is up-to-date with 'origin/1.7/master'.
Updating to version 66acee7feb51d4b30e8983c703bf07ce1d06883e.
    Downloading: 100%         
Use composer self-update --rollback to return to version e77435cd0c984e2031d915a6b42648e7b284dd5c
Loading composer repositories with package information
Updating dependencies (including require-dev)                          
  - Installing composer/installers (v1.0.21)
    Downloading: 100%         

  - Installing fuel/docs (dev-1.7/master 473174d)
    Cloning 473174da2cf503c60d4a9935b71acfc31f0906d0

  - Installing fuel/core (dev-1.7/master f614b30)
    Cloning f614b30e1f76389580c2d97991ab3f25c1533a29

    - Installing fuel/auth (dev-1.7/master aa9bd2e)
      Cloning aa9bd2e5104026814ff516aacf03258f62a94a55

    - Installing fuel/email (dev-1.7/master 8fbf378)
      Cloning 8fbf378d74bac170a96cad96ba0aed77e319a865

    - Installing fuel/oil (dev-1.7/master ea37c3a)
      Cloning ea37c3a7fe8675fb3327327213b2eca55303933a

    - Installing fuel/orm (dev-1.7/master 5e05c30)
      Cloning 5e05c3068562548657fea69850a23b23f65a5545

    - Installing fuel/parser (dev-1.7/master 0cacd10)
      Cloning 0cacd10d7b1b8f92a0eeddce75c6ba2c0c28112f

    - Installing fuelphp/upload (2.0.2)
      Downloading: 100%         

    - Installing psr/log (1.0.0)
      Downloading: 100%         

    - Installing monolog/monolog (1.5.0)
      Downloading: 100%         

    - Installing michelf/php-markdown (1.4.0)
      Downloading: 100%         

monolog/monolog suggests installing mlehner/gelf-php (Allow sending log messages to a GrayLog2 server)
monolog/monolog suggests installing raven/raven (Allow sending log messages to a Sentry server)
monolog/monolog suggests installing doctrine/couchdb (Allow sending log messages to a CouchDB server)
monolog/monolog suggests installing ext-amqp (Allow sending log messages to an AMQP server (1.0+ required))
monolog/monolog suggests installing ext-mongo (Allow sending log messages to a MongoDB server)
Writing lock file
Generating autoload files
Error - date_default_timezone_get(): It is not safe to rely on the system's timezone settings. You are *required* to use the date.timezone setting or the date_default_tim
ezone_set() function. In case you used any of those methods and you are still getting this warning, you most likely misspelled the timezone identifier. We selected the ti
mezone 'UTC' for now, but please set date.timezone to select your timezone. in COREPATH/classes/fuel.php on line 162
~~~

- timzone

~~~
$ vi $(phpenv prefix)/etc/php.ini
~~~

~~~
[Date]
; Defines the default timezone used by the date functions
; http://php.net/date.timezone
;date.timezone =
date.timezone = "Asia/Tokyo"
~~~

~~~bash
$ php -r "echo ini_get('date.timezone'), \"\n\";"
Asia/Tokyo
~~~

~~~
$ oil create hello
fatal: destination path './hello' already exists and is not an empty directory.
M       composer.phar
Already on '1.7/master'
Your branch is up-to-date with 'origin/1.7/master'.
You are already using composer version 66acee7feb51d4b30e8983c703bf07ce1d06883e.
Loading composer repositories with package information
Updating dependencies (including require-dev)                          
Nothing to install or update
Generating autoload files
        Made writable: /vagrant/projects/hellofuel/hello/fuel/app/cache
        Made writable: /vagrant/projects/hellofuel/hello/fuel/app/logs
        Made writable: /vagrant/projects/hellofuel/hello/fuel/app/tmp
        Made writable: /vagrant/projects/hellofuel/hello/fuel/app/config
~~~        

## ビルトインサーバー

~~~
$ cd hello/
$ oil server
Listening on http://localhost:8000
Document root is public
Press Ctrl-C to quit.

$ oil server host=0.0.0.0 post=8000
Listening on http://0.0.0.0:8000
Document root is public
Press Ctrl-C to quit.
.

~~~

## DB接続設定

~~~
$ vi  fuel/app/config/development/db.php
~~~
~~~php
<?php
/**
 * The development database settings. These get merged with the global settings.
 */

return array(
  'default' => array(
    'connection'  => array(
      'dsn'        => 'mysql:host=localhost;dbname=hello_fuel',
      'username'   => 'hello_fuel',
      'password'   => 'hello_fuel',
    ),
  ),
);
~~~

~~~
$ vi fuel/app/config/config.php
~~~
~~~php
<?php
  ....
'always_load'  => array(
  'packages'  => array(
  'orm',
  ),
),
~~~

## `post` アプリ

~~~bash
$ oil generate scaffold post title:string summary:varchar[64] body:text

Creating migration: /vagrant/projects/hellofuel/hello/fuel/app/migrations/001_create_posts.php
Creating model: /vagrant/projects/hellofuel/hello/fuel/app/classes/model/post.php
Creating controller: /vagrant/projects/hellofuel/hello/fuel/app/classes/controller/post.php
Creating view: /vagrant/projects/hellofuel/hello/fuel/app/views/post/index.php
Creating view: /vagrant/projects/hellofuel/hello/fuel/app/views/post/view.php
Creating view: /vagrant/projects/hellofuel/hello/fuel/app/views/post/create.php
Creating view: /vagrant/projects/hellofuel/hello/fuel/app/views/post/edit.php
Creating view: /vagrant/projects/hellofuel/hello/fuel/app/views/post/_form.php
Creating view: /vagrant/projects/hellofuel/hello/fuel/app/views/template.php
~~~

この時点ではテーブルつくられてません。


## マイグレーション

~~~
$ vi $(phpenv prefix)/etc/php.ini

pdo_mysql.default_socket=/var/run/mysqld/mysqld.sock
~~~

~~~bash
$ oil refine migrate post

Performed migrations for app:default:
001_create_posts
~~~

~~~
$ echo "show tables" | mysql  -u hello_fuel --password=hello_fuel hello_fuel -t
+----------------------+
| Tables_in_hello_fuel |
+----------------------+
| migration            |
| posts                |
+----------------------+
~~~

~~~
$ echo "desc migration" | mysql  -u hello_fuel --password=hello_fuel hello_fuel -t
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| type      | varchar(25)  | NO   |     | NULL    |       |
| name      | varchar(50)  | NO   |     | NULL    |       |
| migration | varchar(100) | NO   |     |         |       |
+-----------+--------------+------+-----+---------+-------+
~~~

~~~
$ echo "select * from migration"  | mysql  -u hello_fuel --password=hello_fuel hello_fuel -t
+------+---------+------------------+
| type | name    | migration        |
+------+---------+------------------+
| app  | default | 001_create_posts |
+------+---------+------------------+
~~~

~~~
$ echo "desc posts" | mysql  -u hello_fuel --password=hello_fuel hello_fuel -t                             
+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| id         | int(11) unsigned | NO   | PRI | NULL    | auto_increment |
| title      | varchar(255)     | NO   |     | NULL    |                |
| summary    | varchar(64)      | NO   |     | NULL    |                |
| body       | text             | NO   |     | NULL    |                |
| created_at | int(11)          | YES  |     | NULL    |                |
| updated_at | int(11)          | YES  |     | NULL    |                |
+------------+------------------+------+-----+---------+----------------+
~~~

## `post` 動作

- http://wp.deb:8000/post/ にアクセス

~~~
$ echo "select * from posts"  | mysql  -u hello_fuel --password=hello_fuel hello_fuel -t                   
+----+--------------+--------------+-----------------+------------+------------+
| id | title        | summary      | body            | created_at | updated_at |
+----+--------------+--------------+-----------------+------------+------------+
|  1 | ああああ     | ああああ     | あああああ      | 1442208980 | 1442208980 |
+----+--------------+--------------+-----------------+------------+------------+
~~~
