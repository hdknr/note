
~~~bash

$ phpenv install 7.0.6

[Info]: Loaded extension plugin
[Info]: Loaded apc Plugin.
[Info]: Loaded composer Plugin.
[Info]: Loaded github Plugin.
[Info]: Loaded uprofiler Plugin.
[Info]: Loaded xdebug Plugin.
[Info]: Loaded xhprof Plugin.
[Info]: php.ini-production gets used as php.ini
[Info]: Building 7.0.6 into /home/vagrant/.anyenv/envs/phpenv/versions/7.0.6
[Downloading]: https://secure.php.net/distributions/php-7.0.6.tar.bz2
[Preparing]: /tmp/php-build/source/7.0.6
[Compiling]: /tmp/php-build/source/7.0.6
[xdebug]: Installing version 2.4.0
[xdebug]: Compiling xdebug in /tmp/php-build/source/xdebug-2.4.0
[xdebug]: Installing xdebug configuration in /home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/etc/conf.d/xdebug.ini
[xdebug]: Cleaning up.
[Info]: Enabling Opcache...
[Info]: Done
[Info]: The Log File is not empty, but the Build did not fail. Maybe just warnings got logged. You can review the log in /tmp/php-build.7.0.6.20160522035054.log
[Success]: Built 7.0.6 successfully.
~~~

~~~bash
$ phpenv global 7.0.6

$ phpenv versions
  system
  5.6.10
  5.6.11
  5.6.9
* 7.0.6 (set by /home/vagrant/.anyenv/envs/phpenv/version)

$ php -v
PHP 7.0.6 (cli) (built: May 22 2016 04:03:44) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2016, by Zend Technologies
    with Xdebug v2.4.0, Copyright (c) 2002-2016, by Derick Rethans
~~~

~~~bash
$ php -r "phpinfo();" | grep "Configure Command" | tr ' ' '\n'
Configure
Command
=>

'./configure'

'--with-config-file-path=/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/etc'
'--with-config-file-scan-dir=/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/etc/conf.d'
'--prefix=/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6'
'--libexecdir=/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/libexec'
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
'--enable-bcmath'
'--with-gettext'
~~~

# 追加オプション

- [intl  - 国際化 ](http://php.net/manual/ja/book.intl.php)
