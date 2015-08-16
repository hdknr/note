## インストール

~~~bash
$ mkdir wphome && cd wphome
$ curl -sS https://getcomposer.org/installer | php
$ ./composer.phar require psy/psysh
$ ./composer.phar require wp-cli/wp-cli
~~~

## 確認(--version)

~~~
$ export WP_CLI_CONFIG_PATH=$PWD
~~~

確認(--versionで確認すること)

~~~bash
$ vendor/bin/wp --version
WP-CLI 0.19.2
~~~



## ダウンロード

- wordpress サブディレクトリ

~~~bash
$ vi wp-cli.yml
$ cat wp-cli.yml 

path: wordpress
~~~

- 前回落ちてるキャッシュを使う

~~~
$ mkdir wordpress
$ vendor/bin/wp core download --locale=ja
Downloading WordPress 4.2.4 (ja)...
Using cached file '/home/vagrant/.wp-cli/cache/core/ja-4.2.4.tar.gz'...
Success: WordPress downloaded.
~~~

~~~bash
$ vendor/bin/wp core version --extra
WordPress version: 4.2.4
Database revision: 31536
TinyMCE version:   4.109 (4109-20150505)
~~~

## wp-config.php

~~~bash
$ ls wordpress/wp-config.php
ls: wordpress/wp-config.php にアクセスできません: そのようなファイルやディレクトリはありません
~~~

~~~bash
$ vi wp-cli.yml
$ cat wp-cli.yml

core config:
    dbuser: wphome
    dbname: wphome
    dbpass: wphome
~~~

~~~bash
$ pip install shyaml
Collecting shyaml
  Downloading shyaml-0.3.4.tar.gz
Collecting pyyaml (from shyaml)
  Using cached PyYAML-3.11.tar.gz
Installing collected packages: pyyaml, shyaml
  Running setup.py install for pyyaml
  Running setup.py install for shyaml
Successfully installed pyyaml-3.11 shyaml-0.3.4
~~~

~~~bash
#!/bin/bash

NAME=$(cat wp-cli.yml | shyaml get-value "core config".dbname)
USER=$(cat wp-cli.yml | shyaml get-value "core config".dbuser)
PASSWORD=$(cat wp-cli.yml | shyaml get-value "core config".dbpass)
HOST=localhost

cat << EOF 
CREATE DATABASE $NAME
    DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL on $NAME.*
    to '$USER'@'$HOST'
    identified by '$PASSWORD' WITH GRANT OPTION;
EOF
~~~            

~~~bash
$ ./createdb.bash  | mysql -u root -p 
~~~

~~~bash
$ vendor/bin/wp core config
Success: Generated wp-config.php file.
~~~

## インストール

- wp-cli.yml 修正

~~~yaml
url: http://wp.deb/wordpress
title : Tiltle
admin_user: admin
admin_password: admin
admin_email: admin@admin.admin
~~~

~~~bash
$ cat install.bash 
#!/bin/bash

PARAMS=''
for i in url title admin_user admin_password admin_email ; do
    PARAMS="--$i=$(cat wp-cli.yml|shyaml get-value $i) $PARAMS"
done

vendor/bin/wp core install $PARAMS
~~~

~~~bash
$ ./install.bash 
Success: WordPress installed successfully.
~~~


## nginx

- nginx.bash

~~~bash
#!/bin/bash

mkdir -p nginx/run nginx/logs nginx/www

SERVER_NAME=$(cat wp-cli.yml | shyaml get-value url | sed -r 's/http:\/\///;s|\/.*||')
SOCK=$PWD/nginx/run/php-fpm.sock
LOGDIR=$PWD/nginx/logs
HOME=$PWD/nginx/www

if [ ! -L $HOME/wordpress ]; then
    ln -s $PWD/wordpress $HOME
fi

cat > nginx/php-fpm.conf << EOF
[wordpress]
listen = $SOCK
listen.mode = 0666
user = vagrant
group = vagrant
pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3

EOF

cat > nginx/httpd.conf << EOF
upstream php-fpm-wordpress {
  ip_hash;
  server unix:$SOCK;
}

server {
    listen 80;
    listen [::]:80;

    server_name $SERVER_NAME;

    root $HOME;
    index index.php index.html;

    access_log $LOGDIR/access.log;
    error_log  $LOGDIR/error.log debug;

    location ~ \.php$ {
        fastcgi_pass  php-fpm-wordpress;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME ¥$document_root¥$fastcgi_script_name;
        fastcgi_buffer_size  128k;
        fastcgi_buffers  256 16k;
        fastcgi_busy_buffers_size  256k;
        fastcgi_temp_file_write_size  256k;
        include  fastcgi_params;
    }
}

EOF
~~~
~~~bash
$ ./nginx.bash
~~~

- php-fpm起動

~~~bash
$ sudo $(phpenv prefix)/sbin/php-fpm -y nginx/php-fpm.conf
~~~

~~~
$ sudo ps aux | grep php                                                                          
vagrant    314  0.0  0.1  13688  2268 pts/17   S+   03:47   0:00 grep php
root     31982  0.0  0.4 203812  9680 ?        Ss   03:25   0:00 php-fpm: master process (nginx/php-fpm.conf)                                        
vagrant  31983  0.0  0.3 203812  7940 ?        S    03:25   0:00 php-fpm: pool wordpress                                                             
vagrant  31984  0.0  0.3 203812  7940 ?        S    03:25   0:00 php-fpm: pool wordpress   
~~~

- nginx 起動

~~~bash
$ sudo ln -s $PWD/nginx/httpd.conf /etc/nginx/sites-enabled/wp.deb.conf
~~~

~~~bash
$ sudo /etc/init.d/nginx restart
[ ok ] Restarting nginx (via systemctl): nginx.service.
~~~

## Resource

- [USING WP CLI TO SET UP A TEST VERSION OF YOUR SITE](http://torquemag.io/using-wp-cli-to-set-up-a-test-version-of-your-site/)
- [AUTOMATED WORDPRESS INSTALLATION WITH BASH & WP CLI](http://www.ltconsulting.co.uk/automated-wordpress-installation-with-bash-wp-cli/)

