## インストールと起動

ゲストのUbuntuのphpenv:

~~~bash
(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym/web$ echo $(phpenv prefix)
/home/vagrant/.anyenv/envs/phpenv/versions/7.0.6

(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym/web$ php -v
PHP 7.0.6 (cli) (built: Aug  4 2017 12:18:10) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2016, by Zend Technologies
    with Xdebug v2.5.5, Copyright (c) 2002-2017, by Derick Rethans
~~~

~~~bash
(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym$ mkdir bin
(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym$ curl -LsS https://symfony.com/installer -o bin/symfony
(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym$ chmod +x bin/symfony
(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym$ bin/symfony new web

 Downloading Symfony...

    5.8 MiB/5.8 MiB ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓46100

 Preparing project...

 ✔  Symfony 3.3.6 was successfully installed. Now you can:

    * Change your current directory to /vagrant/projects/samples/sym/web

    * Configure your application in app/config/parameters.yml file.

    * Run your application:
        1. Execute the php bin/console server:start command.
        2. Browse to the http://localhost:8000 URL.

    * Read the documentation at http://symfony.com/doc

(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym$ cd web/
(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym/web$ php bin/console server:start 0.0.0.0:8080

 [OK] Server listening on http://0.0.0.0:8080   

(p3_6_2) vagrant@ubuntu1704-64:/vagrant/projects/samples/sym/web$ lsof -i:8080
COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
php     5095 vagrant    9u  IPv4  26934      0t0  TCP *:http-alt (LISTEN)
~~~

ホストのmacOSより:

~~~bash
Peeko-2:docs hide$ curl -I http://ubuntu.local:8080/

HTTP/1.1 200 OK
Host: ubuntu.local:8080
Connection: close
X-Powered-By: PHP/7.0.6
Cache-Control: no-cache, private
Date: Thu, 17 Aug 2017 02:29:39 GMT
Content-Type: text/html; charset=UTF-8
X-Debug-Token: be7b69
X-Debug-Token-Link: http://ubuntu.local:8080/_profiler/be7b69
~~~
