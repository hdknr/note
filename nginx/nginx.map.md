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
