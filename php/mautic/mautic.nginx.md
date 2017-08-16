mautic: nginx設定


## /client で動かす

- `/home/ubuntu/projects/bp-mautic/mautic` に mautic のソースを配置(git clone)
- `mautic` ディレクトリをシンボリックリンクを `client` で作成
- 名前付きロケーション([named location](http://nginx.org/en/docs/http/ngx_http_core_module.html#location))で php-fpm に流す
- ルートを `mautic` の親ディレクトリとする
- `mautic_upstream` でphp-fpm のアップストリーム設定されている


~~~
# location ~ ^/mautic(/.*)$ {
location ~ ^/client(/.*)$ {
   alias /home/ubuntu/projects/bp-mautic/mautic;        # スタティックファイルの配信に必要
   try_files $1 @mautic;
}


location @mautic {
   root /home/ubuntu/projects/bp-mautic;
   expires off;
   fastcgi_index   index.php;
   fastcgi_keep_conn on;
   fastcgi_pass   mautic_upstream;
   fastcgi_split_path_info ^(.+\.php)(/.+)$;
   include         fastcgi_params;
   fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
~~~

## Symfony

- https://stackoverflow.com/a/28269332

ポイント: app.php を　/front/app.php にある、と思わせる
~~~
set $frontRoot /your/project/path/web;
set $sfApp app_dev.php; # Change to app.php for prod

location /front/ { # Static files
    root $frontRoot;
    rewrite ^/front/(.*)$ /$1 break;                      # リライト(1)
    try_files $uri @sfFront;
}

location @sfFront { # Symfony
    fastcgi_pass phpfcgi;                                 # アップストリーム
    include fastcgi_params;
    fastcgi_param SCRIPT_FILENAME $frontRoot/$sfApp;      # PHPファイルの絶対 パス
    fastcgi_param SCRIPT_NAME /front/$sfApp;              # app.php(app_dev.php) のパスをだます
    fastcgi_param REQUEST_URI /front$uri?$args;           # ユーザーの入力したURLのパス。 明示的に /front を先頭に入れる : リライト(1) で抜かれているので
    fastcgi_param HTTPS off;
}
~~~
