# PHP 7.2


## mcrypto -> libsodium

- [Introduction - Libsodium documentation](https://download.libsodium.org/doc/)
- 使わないのがデフォルトの模様
- `libsodium-dev` を使う模様

記事:

- [PHP7.2で実装されたLibsodiumのサンプルコードまとめ - Qiita](https://qiita.com/fri13th/items/596de162c28d97d7aeed)
- [Install phpenv on Ubuntu 16.04 LTS (xenial)](https://gist.github.com/christopher-hopper/d3467ab87217dc1143f832ba7012c0f7)


## libzip

- [libzip](https://libzip.org/)

~~~
----------------------------------------------------------------------------------
configure: WARNING: Libzip >= 1.2.0 needed for encryption support
----------------------------------------------------------------------------------
~~~

ソースからインストール:

~~~bash
mkdir /tmp/libzip
cd /tmp/libzip
curl -sSLO https://libzip.org/download/libzip-1.4.0.tar.gz
tar zxf libzip-1.4.0.tar.gz
cd libzip-1.4.0
mkdir build
cd build
cmake ../
make > /dev/null
sudo make install
~~~

php-build オプション:

~~~
--with-libzip=/usr/local/lib/libzip.so
~~~

## Ubuntu 18.04.1 LTS

### (1) Vagrant OK

Vagrantで新規に `up` した場合、問題なくインストールされた:

~~~bash
$ phpenv install 7.2.10
[Info]: Appending build output to /tmp/php-build.7.2.10.20180922165732.log
[Info]: Loaded extension plugin
[Info]: Loaded apc Plugin.
[Info]: Loaded composer Plugin.
[Info]: Loaded github Plugin.
[Info]: Loaded uprofiler Plugin.
[Info]: Loaded xdebug Plugin.
[Info]: Loaded xhprof Plugin.
[Info]: Loaded zendopcache Plugin.
[Info]: php.ini-production gets used as php.ini
[Info]: Building 7.2.10 into /home/vagrant/.anyenv/envs/phpenv/versions/7.2.10
[Downloading]: https://secure.php.net/distributions/php-7.2.10.tar.bz2
[Preparing]: /tmp/php-build/source/7.2.10
[Compiling]: /tmp/php-build/source/7.2.10
[xdebug]: Installing version 2.6.1
[Downloading]: http://xdebug.org/files/xdebug-2.6.1.tgz
[xdebug]: Compiling xdebug in /tmp/php-build/source/xdebug-2.6.1
[xdebug]: Installing xdebug configuration in /home/vagrant/.anyenv/envs/phpenv/versions/7.2.10/etc/conf.d/xdebug.ini
[xdebug]: Cleaning up.
[Info]: Enabling Opcache...
[Info]: Done
[Info]: The Log File is not empty, but the Build did not fail. Maybe just warnings got logged. You can review the log in /tmp/php-build.7.2.10.20180922165732.log
[Success]: Built 7.2.10 successfully.
~~~

### (2) EC2 - No!

- ただし、新規に作成した 1804 インスタンスでやってみると 1604と同じようにAbortした。。。

### (3) パッケージの差分

~~~bash
$ dpkg --get-selections | grep -v deinstall | awk '{print $1}'| sort > ~/pkg.vagrant.txt
$ dpkg --get-selections | grep -v deinstall | awk '{print $1}'| sort > ~/pkg.aws.txt
$ diff pkg.vagrant.txt  pkg.aws.txt
~~~ 

~~~diff
62d61
< dkms
125a125
> hibagent
505a506,507
> linux-aws
> linux-aws-headers-4.15.0-1021
507,512c509,512
< linux-headers-4.15.0-34
< linux-headers-4.15.0-34-generic
< linux-headers-generic
< linux-headers-virtual
< linux-image-4.15.0-34-generic
< linux-image-virtual
---
> linux-headers-4.15.0-1021-aws
> linux-headers-aws
> linux-image-4.15.0-1021-aws
> linux-image-aws
514,515c514
< linux-modules-4.15.0-34-generic
< linux-virtual
---
> linux-modules-4.15.0-1021-aws
~~~

- [Debian -- sid の dkms パッケージに関する詳細](https://packages.debian.org/ja/sid/dkms)
- [Ubuntu – bionic の hibagent パッケージに関する詳細](https://packages.ubuntu.com/bionic/hibagent)

### (4) 正確には、同じ WARNINGがでている

- が、 Vagrantはその後ビルドに成功している

~~~
$ more php-build.7.2.10.20180923101344.log 
configure: WARNING: unrecognized options: --with-mcrypt
configure: WARNING: ========================================================
configure: WARNING: Use of bundled libzip is deprecated and will be removed.
configure: WARNING: Some features such as encryption and bzip2 are not available.
configure: WARNING: Use system library and --with-libzip is recommended.
configure: WARNING: ========================================================
configure: WARNING: unrecognized options: --with-mcrypt
Configuring for:
PHP Api Version:         20170718
Zend Module Api No:      20170718
Zend Extension Api No:   320170718
~~~

### (5) `-v` オプションでビルド

~~~bash
$ phpenv install -v 7.2.10
~~~

~~~
-----------------
|  BUILD ERROR  |
-----------------

Here are the last 10 lines from the log:
...

virtual memory exhausted: Cannot allocate memory
Makefile:894: recipe for target 'ext/fileinfo/libmagic/apprentice.lo' failed
make: *** [ext/fileinfo/libmagic/apprentice.lo] Error 1
-----------------------------------------

The full Log is available at '/tmp/php-build.7.2.10.20180923113345.log'.
[Warn]: Aborting build.
~~~

### (6) スワップを設定して再度ビルドしたら成功

~~~bash
$ sudo mkdir /var/swap/
$ sudo dd if=/dev/zero of=/var/swap/swap0 bs=2M count=512
$ sudo chmod 600 /var/swap/swap0
$ sudo mkswap /var/swap/swap0
$ sudo swapon /var/swap/swap0
~~~

## 記事

- [PHP7.2がリリースされたので野良ビルドしてみた - Qiita](https://qiita.com/m3m0r7/items/f1342bca10040cdff3ab)
- [How to install mcrypt in php7.2 | Lukáš Mešťan](https://lukasmestan.com/install-mcrypt-extension-in-php7-2/)
- [No sodium for 7.2 · Issue #101 · paragonie/halite](https://github.com/paragonie/halite/issues/101)
- [phpenvのよくあるエラーとその回答集 - ささきしき](https://siky.hateblo.jp/entry/2017/10/09/230633)
