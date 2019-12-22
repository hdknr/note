# Install

## Swap

- `php-build` でエラーがおきないように

~~~bash
$ sudo mkdir /var/swap/
$ sudo dd if=/dev/zero of=/var/swap/swap0 bs=2M count=512
$ sudo chmod 600 /var/swap/swap0
$ sudo mkswap /var/swap/swap0
$ sudo swapon /var/swap/swap0
~~~

/etc/fstab:

~~~
/var/swap/swap0 swap swap defaults 0 0
~~~

## Ubuntu Packages

~~~bash
$ bin/ubuntu.bash
~~~

## Anyenv

~~~bash 
$ bin/anyenv.bash
~~~

## PHP

最新をいれる
~~~bash 
$ phpenv install 7.2.10
~~~

- もしもMautic をいれるのであれば、 7.0.30 以下のPHPを別にインストールする

## php.ini


### 1) memory

~~~ini
memory_limit = 512M
~~~


## nginx

~~~bash 
$ sudo cp -r etc/nginx/sites-available/phprun /etc/nginx/sites-available/
~~~

## supervisor

~~~bash 
$ sudo cp -r etc/supervisor/conf.d/phprun.conf  /etc/supervisor/conf.d/
~~~

~~~bash
$ pushd .; cd /etc/nginx/sites-enabled
$ sudo ln -s ../sites-available/shaperweb/server.conf default
$ ls -al
合計 8
drwxr-xr-x 2 root root 4096  9月 23 01:06 .
drwxr-xr-x 6 root root 4096 12月 17  2017 ..
lrwxrwxrwx 1 root root   40  9月 23 01:06 default -> ../sites-available/phprun/server.conf
~~~

~~~bash 
$ sudo supervisorctl reload
Restarted supervisord

$ sudo supervisorctl status
phprun RUNNING   pid 2457, uptime 0:00:05
~~~
