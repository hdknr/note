
## インストール

- ワンライナー

~~~bash
$ curl -s https://getcomposer.org/installer | php
~~~

- ダウンロード (https://getcomposer.org/download/)

~~~bash

$ php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
$ tree .
.
└── composer-setup.php

0 directories, 1 file

$ php -r "if (hash_file('SHA384', 'composer-setup.php') === '92102166af5abdb03f49ce52a40591073a7b859a86e8ff13338cf7db58a19f7844fbc0bb79b2773bf30791e935dbd938') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

Installer verified

$ php composer-setup.php
Downloading 1.1.1...

Composer successfully installed to: /home/vagrant/projects/researchdb/composer.phar
Use it: php composer.phar
Some settings on your machine may cause stability issues with Composer.
If you encounter issues, try to change the following:

The xdebug extension is loaded, this can slow down Composer a little.
Disabling it when using Composer is recommended.

$ php -r "unlink('composer-setup.php');"

$ tree .
.
└── composer.phar

0 directories, 1 file

$ ./composer.phar --version
You are running composer with xdebug enabled. This has a major impact on runtime performance. See https://getcomposer.org/xdebug
Composer version 1.1.1 2016-05-17 12:25:44

~~~

- [Composerをインストールしてみた](http://qiita.com/kakijin/items/02364adacf36410f449e)

## xdebug を無効にする

~~~bash
$ phpenv prefix
/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6

$ vi $(phpenv prefix)/etc/conf.d/xdebug.ini

;zend_extension="/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6/lib/php/extensions/no-debug-non-zts-20151012/xdebug.so"
;html_errors=on
~~~


## self-update

~~~
$ ./composer.phar self-update

Updating to version 00c26791faeb83da8476b54bcc20596cf754362e.
    Downloading: 100%         
Use composer self-update --rollback to return to version 4569f528f66739ec0a3be1075e2c01d6062b0b41
~~~


## ノート

- [composer 導入をまじめに考える](http://qiita.com/notona/items/c5a087d8dd446d315e6e)
