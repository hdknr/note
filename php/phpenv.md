# phpenv

- [CHH/phpenv](https://github.com/CHH/phpenv)
- [Qiita](http://qiita.com/uchiko/items/5f1843d3d848de619fdf)
- http://y-uti.hatenablog.jp/entry/2014/10/13/232540

## 前提

### Debian

```
$ sudo apt-get install git git-core curl build-essential libxml2-dev \
libssl-dev libcurl4-gnutls-dev libjpeg-dev libpng12-dev libmcrypt-dev \
libreadline-dev libtidy-dev libxslt1-dev autoconf
```

## Install

```
sugar@wzy:~$ curl https://raw.githubusercontent.com/CHH/phpenv/master/bin/phpenv-install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3128  100  3128    0     0   7842      0 --:--:-- --:--:-- --:--:-- 11893
Installing phpenv in /home/sugar/.phpenv
remote: Counting objects: 2002, done.
remote: Total 2002 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (2002/2002), 318.88 KiB | 136 KiB/s, done.
Resolving deltas: 100% (1249/1249), done.
Success.

export PATH="/home/sugar/.phpenv/bin:$PATH"
eval "$(phpenv init -)"

Add above line at the end of your ~/.bashrc and restart your shell to use phpenv.
```

```
sugar@wzy:~$echo 'export PATH="$HOME/.phpenv/bin:$PATH"' >> ~/. bash_phpenv
sugar@wzy:~$echo 'eval "$(phpenv init -)"' >> ~/.bash_phpenv
sugar@wzy:~$ source ~/.bash_phpenv 
```

```
vagrant@10:~$ phpenv
rbenv 0.4.0-129-g7e0e85b
Usage: rbenv <command> [<args>]

Some useful rbenv commands are:
   commands    List all available rbenv commands
   local       Set or show the local application-specific Ruby version
   global      Set or show the global Ruby version
   shell       Set or show the shell-specific Ruby version
   rehash      Rehash rbenv shims (run this after installing executables)
   version     Show the current Ruby version and its origin
   versions    List all Ruby versions available to rbenv
   which       Display the full path to an executable
   whence      List all Ruby versions that contain the given executable

See `rbenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/sstephenson/rbenv#readme

```


```
sugar@wzy:~$ git clone git://github.com/CHH/php-build.git ~/.phpenv/plugins/php-build
Cloning into '/home/sugar/.phpenv/plugins/php-build'...
remote: Counting objects: 2626, done.
remote: Total 2626 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (2626/2626), 395.13 KiB | 95 KiB/s, done.
Resolving deltas: 100% (1374/1374), done.
```



# phpインストール

```
sugar@wzy:~$ phpenv install -l |& grep "5.5.1."
 5.5.10
 5.5.11
 5.5.12
 5.5.13
 5.5.14
 5.5.15
 5.5.16
 5.5.17
 5.5.18
 5.5.19
```

```
vagrant@10:~$ phpenv install 5.5.19
[Info]: Loaded apc Plugin.
[Info]: Loaded composer Plugin.
[Info]: Loaded pyrus Plugin.
[Info]: Loaded xdebug Plugin.
[Info]: Loaded xhprof Plugin.
[Info]: php.ini-production gets used as php.ini
[Info]: Building 5.5.19 into /home/vagrant/.phpenv/versions/5.5.19
[Downloading]: http://php.net/distributions/php-5.5.19.tar.bz2
[Preparing]: /tmp/php-build/source/5.5.19
[Compiling]: /tmp/php-build/source/5.5.19
[Pyrus]: Downloading from http://pear2.php.net/pyrus.phar
[Pyrus]: Installing executable in /home/vagrant/.phpenv/versions/5.5.19/bin/pyrus
[XDebug]: Downloading http://xdebug.org/files/xdebug-2.2.5.tgz
[XDebug]: Compiling in /tmp/php-build/source/xdebug-2.2.5
[XDebug]: Installing XDebug configuration in /home/vagrant/.phpenv/versions/5.5.19/etc/conf.d/xdebug.ini
[XDebug]: Cleaning up.
[Info]: Enabling Opcache...
[Info]: Done
[Info]: The Log File is not empty, but the Build did not fail. Maybe just warnings got logged. You can review the log in /tmp/php-build.5.5.19.20141202095109.log
[Success]: Built 5.5.19 successfully.
```

## オプション追加

```
sugar@wzy:~$ more .phpenv/plugins/php-build/share/php-build/default_configure_options
--without-pear
--with-gd
--enable-sockets
--with-jpeg-dir=/usr
--with-png-dir=/usr
--enable-exif
--enable-zip
--with-zlib
--with-zlib-dir=/usr
--with-kerberos
--with-openssl
--with-mcrypt=/usr
--enable-soap
--enable-xmlreader
--with-xsl
--enable-ftp
--enable-cgi
--with-curl=/usr
--with-tidy
--with-xmlrpc
--enable-sysvsem
--enable-sysvshm
--enable-shmop
--with-mysql=mysqlnd
--with-mysqli=mysqlnd
--with-pdo-mysql=mysqlnd
--with-pdo-sqlite
--enable-pcntl
--with-readline
--enable-mbstring
--disable-debug
--enable-fpm
--enable-bcmath
```

```
sugar@wzy:~$ sudo which apxs2
/usr/bin/apxs2
```
```
sugar@wzy:~$ echo configure_option '"--with-apxs2"' '"'`which apxs2`'"' >> .phpenv/plugins/php-build/share/php-build/definitions/5.5.19

```

```
sugar@wzy:~$ more .phpenv/plugins/php-build/share/php-build/definitions/5.5.19
install_package "http://php.net/distributions/php-5.5.19.tar.bz2"
install_pyrus
install_xdebug "2.2.5"
enable_builtin_opcache
configure_option "--with-apxs2" "/usr/bin/apxs2"
```

## ビルドエラー

- ライブラリが足りていない(Debian パッケージとか)

```
-----------------
|  BUILD ERROR  |
-----------------

Here are the last 10 lines from the log:

-----------------------------------------
configure: WARNING: You will need re2c 0.13.4 or later if you want to regenerate PHP parsers.
configure: error: mcrypt.h not found. Please reinstall libmcrypt.
-----------------------------------------

The full Log is available at '/tmp/php-build.5.5.19.20141129120732.log'.
[Warn]: Aborting build.

```


# バージョン切り替え

```
vagrant@10:~$ phpenv versions
  5.5.19
```

-  全ディレクトリ

```  
vagrant@10:~$ phpenv global 5.5.19
```

```
vagrant@10:~$ php -version
PHP 5.5.19 (cli) (built: Dec  2 2014 10:01:16) 
Copyright (c) 1997-2014 The PHP Group
Zend Engine v2.5.0, Copyright (c) 1998-2014 Zend Technologies
    with Zend OPcache v7.0.4-dev, Copyright (c) 1999-2014, by Zend Technologies
    with Xdebug v2.2.5, Copyright (c) 2002-2014, by Derick Rethans
```

# rbenv: version `system' is not installed

```
vagrant@10:~$ git clone https://github.com/laprasdrum/phpenv.git ~/.phpenv
Cloning into '/home/vagrant/.phpenv'...
remote: Counting objects: 92, done.
remote: Total 92 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (92/92), done.
Checking connectivity... done.
```

# composer

```
vagrant@10:~$ cd ~/.phpenv/plugins
vagrant@10:~/.phpenv/plugins$ git clone https://github.com/ngyuki/phpenv-composer.git
Cloning into 'phpenv-composer'...
remote: Counting objects: 34, done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 34 (delta 5), reused 33 (delta 5)
Unpacking objects: 100% (34/34), done.
Checking connectivity... done.
```