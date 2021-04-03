- [nginxでmapモジュールを使って301リダイレクトを行う](http://polidog.jp/2015/02/09/nginx/)


- [nginxの301リダイレクト(ティレクトリマッピング)設定例](http://zuntan02.hateblo.jp/entry/2015/08/13/115810)

リダイレクトルール: (/etc/nginx/redirect_list.map)

~~~
~^/dir1/dir2/index.html$ /dir1/index2.html;
~^/2015/01/06/.* http://polidog.jp/2015/01/06/akeome/;
~^/2015/12/31/.* http://polidog.jp/2015/12/31/fruikaeri/;
~~~

設定:

~~~
map $request_uri $new {
  include /etc/nginx/redirect_list.map;
}
server {
  listen 80;

  if ($new) {
    rewrite ^ $new permanent;
  }
}
~~~

## `$proxy_add_x_forwarded_for` にカンマ区切りで複数のアドレスが指定された時の最初のアドレス

~~~
map $proxy_add_x_forwarded_for $client_ip {
    "~(?<IP>([0-9]{1,3}\.){3}[0-9]{1,3}),.*" $IP;
    default '';
}

server {
    ...
            location ~ \.php$ {
            include snippets/fastcgi-php.conf;

            fastcgi_param REMOTE_ADDR  $client_ip;
            fastcgi_param HTTP_X_FORWARDED_PROTO $protocol;
            fastcgi_param HTTP_X_FORWARDED_PORT $port;
            fastcgi_param HTTP_X_FORWARDED_FOR $proxy_add_x_forwarded_for;
            fastcgi_param HTTPS $https_on;

            fastcgi_pass app;
            fastcgi_param SCRIPT_FILENAME $request_filename;
        }
}
~~~