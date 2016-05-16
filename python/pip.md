## setuptools

- [Setuptools unable to use link from dependency_links](https://stackoverflow.com/questions/17366784/setuptools-unable-to-use-link-from-dependency-links)
- [Python setuptools: How can I list a private repository under install_requires?](https://stackoverflow.com/questions/18026980/python-setuptools-how-can-i-list-a-private-repository-under-install-requires)
(これはpipをos.systemでコールするやり方)

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

## 再インストール

~~~bash
$ pip --no-cache-dir install -I pillow
~~~
