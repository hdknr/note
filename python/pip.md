## connection error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed

- virtualenv の作成の時にエラー

~~~
Could not fetch URL https://pypi.python.org/simple/virtualenv/: 
connection error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)
~~~

- cacert.pem を落とす

~~~
$ mkdir etc ; cd etc
$ wget http://curl.haxx.se/ca/cacert.pem
~~~

- pip.conf を設定

~~~
$ cd; mkdir .pip 
$ vi .pip/pip.conf
~~~

~~~
[global]
cert = /home/system/etc/cacert.pem 
~~~