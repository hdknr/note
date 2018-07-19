## mautic

- https://jp.mautic.org/
- [メールサービス](https://github.com/hdknr/scriptogr.am/blob/master/php/mautic/mautic.email.md)


## インストール

- PHP環境の用意( <= 7.0.30)
- [mautic/mautic](https://github.com/mautic/mautic)`@stagin` をクローン
- compposerのインストール

~~~bash 
$ curl -sS https://getcomposer.org/installer | php
~~~

- 依存パッケージインストール:

~~~bash
$ ./composer.phar install
~~~

- nginxの設定
- MySQLのデータベース作成
- ブラウザでアクセスしてインストール(データベースは`localhost` ではなく `127.0.0.1` とする)


## nginx 設定

`/pr` というパスで動かす例(この場合、root(`/data/projects/taberu/landing`) の下に `pr` という名前で mauticをチェックアウトする必要あり/シンボリックリンクもあり):

~~~
include sites-available/landing/mautic_upstream.conf;


server {
    client_max_body_size 300M;

    error_page 404 /index.php;
    error_page 405 = $uri;

    listen 80;
    server_name taberu.shaper.co.jp;

    #######################################
    ##  Start Mautic Specific config #####
    #######################################


    location ~* /wp-config.php {
        deny all;
    }

    # Don't log favicon
    location = /favicon.ico {
        log_not_found off;
        access_log off;
    }

    # Don't log robots
    location = /robots.txt  {
        access_log off;
        log_not_found off;
    }

    # Deny yml, twig, markdown, init file access
    location ~* /(.*)\.(?:markdown|md|twig|yaml|yml|ht|htaccess|ini)$ {
        deny all;
        access_log off;
        log_not_found off;
    }

    # Deny all attempts to access hidden files/folders such as .htaccess, .htpasswd, .DS_Store (Mac), etc...
    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }

    # Deny all grunt, composer files
    location ~* (Gruntfile|package|composer)\.(js|json)$ {
        deny all;
        access_log off;
        log_not_found off;
    }

    include sites-available/landing/mautic_alias.conf;

    ## CORS 
    add_header 'Access-Control-Allow-Origin' "*";
}
~~~

mautic_upstream.conf:

~~~
upstream mautic_upstream {
  server unix:/home/ubuntu/.anyenv/envs/phpenv/versions/7.0.30/var/run/mautic_phpfpm.sock;
}
~~~

mautic_alias.conf:

~~~
## 名前付きロケーション
location @pr_app {
   rewrite  ^/pr(.*)$  /pr/index.php$1;
}

## pr 配下のPHPの処理
location ~ ^/pr(.*).php {
   root /data/projects/taberu/landing;     
   fastcgi_pass   mautic_upstream;

   fastcgi_split_path_info ^(.+\.php)(/.+)$;
   include         fastcgi_params;
   fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
   # fastcgi_param   SCRIPT_NAME $document_root$request_filename;
}

location ~ ^/pr(.*) {
   alias /data/projects/taberu/landing;
   try_files $uri @pr_app;
}
~~~