# コンテナのnginx設定

CloudFront -> ALB -> nginx(ECS) -> php-fpm(ECS):

## nginx.conf

~~~conf

upstream app {
    # php-fpm unix socket
    server unix:/usr/local/var/run/upstream.php-fpm.sock;
}

# URL protocol
map $http_cloudfront_forwarded_proto $protocol {
   ""           $http_x_forwarded_proto;
   default      $http_cloudfront_forwarded_proto;
}

# URL Port
map $protocol $port {
    https      443;
    default    $http_x_forwarded_port;
}

# HTTP or HTTPS 
map $port $https_on {
    443     'on';
    default $http;
}

server {
    listen 80 default_server;
    server_name localhost;
    index index.php index.html;
    root /var/www/html/public;

    # stdout for CloudWatch or Firelens Logging
    access_log /dev/stdout;
    error_log /dev/stdout warn;

    location ~ ^/consumer$ {
       # debug
       # add_header 'x-container-host' $protocol://$host;
       # add_header 'x-container-port' $port;

       # force to use Edge Scheme
       return 301 $protocol://$host/consumer/;       
    }

    location /consumer {
        alias /var/www/html/public;
        
        try_files $uri $uri/ @consumer;
        gzip_static on;

        location ~ \.php$ {
            include snippets/fastcgi-php.conf;

            # required for PHP compose valid URL
            fastcgi_param HTTP_X_FORWARDED_PROTO $protocol;
            fastcgi_param HTTP_X_FORWARDED_PORT $port;
            fastcgi_param HTTPS $https_on;

            fastcgi_pass app;
            fastcgi_param SCRIPT_FILENAME $request_filename;
        }
    }

    location @consumer {
        rewrite /consumer/(.*)$ /consumer/index.php?/$1 last;
    }
}
~~~

nginx/snippets/fastcgi-php.conf:

~~~
fastcgi_split_path_info ^(.+?\.php)(/.*)$;
try_files $fastcgi_script_name =404;
set $path_info $fastcgi_path_info;
fastcgi_param PATH_INFO $path_info;
fastcgi_index index.php;
include fastcgi.conf;
~~~


## php-fpm.conf

~~~ini
[global]

[www]
user = www-data
group = www-data
listen.owner = www-data
listen.group = www-data

; Unixソケットファイル名:
listen = var/run/upstream.php-fpm.sock
listen.allowed_clients = 127.0.0.1
listen.mode = 0660

clear_env = no

pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3

catch_workers_output = yes
php_admin_flag[log_errors] = on
~~~

## entrypoint スクリプト

~~~bash
#!/usr/bin/env bash

# sshd
if [ -f "/usr/sbin/sshd" ]; then
    service ssh restart
fi

# nginx
if [ -f "/usr/sbin/nginx" ]; then
    service nginx restart
fi

# php-fpm
if [ -f "/usr/local/etc/php-fpm-app.conf" ]; then
    # 
    php-fpm -F -O -y /usr/local/etc/php-fpm-app.conf
else
    php-fpm
fi
~~~