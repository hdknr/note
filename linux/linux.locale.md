# locale

## Debian

~~~
$ sudo dpkg-reconfigure locales
~~~


Debian

~~~bash
$ sudo apt-get install task-japanese
$ sudo vim /etc/locale.gen
ja_JP.UTF-8の行のコメントを解除
$ sudo locale-gen
$ sudo update-locale LANG=ja_JP.UTF-8
~~~

Ubuntu

~~~bash
$ sudo apt-get install language-pack-ja
$ sudo update-locale LANG=ja_JP.UTF-8
~~~
