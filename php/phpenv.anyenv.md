## anyenv でインストール
- [メモ](https://gist.github.com/hdknr/88c64685f14a93325062)

~~~
$ anyenv install phpenv
/tmp/phpenv.20150705045011.20654 ~
Cloning https://github.com/laprasdrum/phpenv.git...
Cloning into 'phpenv'...
remote: Counting objects: 92, done.
remote: Compressing objects: 100% (61/61), done.
remote: Total 92 (delta 27), reused 92 (delta 27), pack-reused 0
Unpacking objects: 100% (92/92), done.
Checking connectivity... done.
~
~/.anyenv/envs/phpenv/plugins ~
Cloning https://github.com/CHH/php-build.git...
Cloning into 'php-build'...
~~~

~~~
$ exec $SHELL -l
$ phpenv --version
phpenv 0.4.0
~~~

## 更新

~~~bash
$ git --git-dir=$(phpenv root)/.git pull
~~~

## PHP 5.6.10 インストール

~~~bash
$ phpenv install 5.6.10
[Info]: Loaded extension plugin
[Info]: Loaded apc Plugin.
[Info]: Loaded composer Plugin.
[Info]: Loaded pyrus Plugin.
[Info]: Loaded uprofiler Plugin.
[Info]: Loaded xdebug Plugin.
[Info]: Loaded xhprof Plugin.
[Info]: php.ini-production gets used as php.ini
[Info]: Building 5.6.10 into /home/vagrant/.anyenv/envs/phpenv/versions/5.6.10
[Downloading]: http://php.net/distributions/php-5.6.10.tar.bz2
[Preparing]: /tmp/php-build/source/5.6.10
[Compiling]: /tmp/php-build/source/5.6.10
[Pyrus]: Downloading from http://pear2.php.net/pyrus.phar
[Pyrus]: Installing executable in /home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/bin/pyrus
[xdebug]: Installing version 2.3.3
[xdebug]: Compiling xdebug in /tmp/php-build/source/xdebug-2.3.3
[xdebug]: Installing xdebug configuration in /home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/etc/conf.d/xdebug.ini
[xdebug]: Cleaning up.
[Info]: Enabling Opcache...
[Info]: Done
[Info]: The Log File is not empty, but the Build did not fail. Maybe just warnings got logged. You can review the log in /tmp/php-build.5.6.10.20150706032709.log
[Success]: Built 5.6.10 successfully.
~~~

~~~bash
$ phpenv global 5.6.10
$ phpenv versions
  system
* 5.6.10 (set by /home/vagrant/.anyenv/envs/phpenv/version)
~~~

### configure の確認

~~~bash

$ php -r "phpinfo();" | grep "Configure Command" | tr ' ' '\n'
~~~

~~~
'./configure'

'--with-config-file-path=/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/etc'
'--with-config-file-scan-dir=/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/etc/conf.d'
'--prefix=/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10'
'--libexecdir=/home/vagrant/.anyenv/envs/phpenv/versions/5.6.10/libexec'
'--without-pear'
'--with-gd'
'--enable-sockets'
'--with-jpeg-dir=/usr'
'--with-png-dir=/usr'
'--enable-exif'
'--enable-zip'
'--with-zlib'
'--with-zlib-dir=/usr'
'--with-kerberos'
'--with-openssl'
'--with-mcrypt=/usr'
'--enable-soap'
'--enable-xmlreader'
'--with-xsl'
'--enable-ftp'
'--enable-cgi'
'--with-curl=/usr'
'--with-tidy'
'--with-xmlrpc'
'--enable-sysvsem'
'--enable-sysvshm'
'--enable-shmop'
'--with-mysql=mysqlnd'
'--with-mysqli=mysqlnd'
'--with-pdo-mysql=mysqlnd'
'--with-pdo-sqlite'
'--enable-pcntl'
'--with-readline'
'--enable-mbstring'
'--disable-debug'
'--enable-fpm'
'--enable-bcmath
~~~

### apx2 の追加

~~~bash
$ sudo apt-get install apache2-dev
$ which apxs2
/usr/bin/apxs2
~~~

~~~bash
$ echo configure_option '"--with-apxs2"' '"'`which apxs2`'"' >> ~/.anyenv/envs/phpenv/plugins/php-build/share/php-build/definitions/5.6.10
~~~

~~~bash
$ phpenv install 5.6.10
[Info]: Loaded extension plugin
[Info]: Loaded apc Plugin.
[Info]: Loaded composer Plugin.
[Info]: Loaded pyrus Plugin.
[Info]: Loaded uprofiler Plugin.
[Info]: Loaded xdebug Plugin.
[Info]: Loaded xhprof Plugin.
[Info]: php.ini-production gets used as php.ini
[Info]: Building 5.6.10 into /home/vagrant/.anyenv/envs/phpenv/versions/5.6.10
[Info]: The Log File is not empty, but the Build did not fail. Maybe just warnings got logged. You can review the log in /tmp/php-build.5.6.10.20150706035512.log
[Success]: Built 5.6.10 successfully.
~~~

- 削除 & 再インストール

~~~
$ rm -rf /tmp/php-build*
$ rm -rf .anyenv/envs/phpenv/versions/5.6.10
~~~

~~~bash
$ phpenv install 5.6.10
~~~


# いろいろ

## 再インストール

- 消す

~~~bash
$ rm -rf .anyenv/envs/phpenv/versions/5.6.10
~~~

- もう一回

~~~bash
$ phpenv install 5.6.10
~~~

## ビルドが正常終了するのに versionsにできていない

- php-build/definitions がおかしくない？確認しよう

~~~bash
$ cat ~/.anyenv/envs/phpenv/plugins/php-build/share/php-build/definitions/5.6.10
~~~


## -bash: php5: command not found

~~~
$ php5
-bash: php5: command not found
~~~

~~~
$ phpenv rehash
~~~

~~~
$ php -v
PHP 5.6.10 (cli) (built: Jul  7 2015 03:05:11)
Copyright (c) 1997-2015 The PHP Group
Zend Engine v2.6.0, Copyright (c) 1998-2015 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2015, by Zend Technologies
    with Xdebug v2.3.3, Copyright (c) 2002-2015, by Derick Rethans
~~~

## デフォルト configure オプション

- $HOME/.anyenv/envs/phpenv/plugins/php-build/share/php-build/default_configure_options にあります


### カレントディレクトリのphp.iniを読ませる

~~~
configure_option "--with-config-file-scan-dir=.;/root/.phpenv/versions/5.5.22/etc/conf.d"
~~~
