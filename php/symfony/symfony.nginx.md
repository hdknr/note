## `/front` で動かす

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
