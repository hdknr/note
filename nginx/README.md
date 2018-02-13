nginx

## トピック

- [nginx.conf](nginx.conf.md)
- [502エラー](nginx.502.md)
- [allow/deny](nginx.access.md)
- [map](nginx.map.md)
- [fastcgi](nginx.fastcgi.md)
- [ログ](nginx.log.md)

## ビルド内容

~~~bash
$ sudo nginx -V  |& tr " " "\n"
~~~

## ビルド

- [ダウンロードページ](http://nginx.org/en/download.html) で確認

~~~
# curl http://nginx.org/download/nginx-1.9.2.tar.gz | tar xvfz -
~~~

- [configureオプション](http://nginx.org/en/docs/configure.html)

~~~
# ./confiture --prefix=/usr/local/nginx-1.9.2 --user=www-data --group=www-data --with-http_ssl_module --with-http_realip_module
~~~

~~~
# make && make install
~~~

~~~
# tree /usr/local/nginx-1.9.2/
/usr/local/nginx-1.9.2/
|-- conf
|   |-- fastcgi.conf
|   |-- fastcgi.conf.default
|   |-- fastcgi_params
|   |-- fastcgi_params.default
|   |-- koi-utf
|   |-- koi-win
|   |-- mime.types
|   |-- mime.types.default
|   |-- nginx.conf
|   |-- nginx.conf.default
|   |-- scgi_params
|   |-- scgi_params.default
|   |-- uwsgi_params
|   |-- uwsgi_params.default
|   `-- win-utf
|-- html
|   |-- 50x.html
|   `-- index.html
|-- logs
`-- sbin
    `-- nginx

4 directories, 18 files
~~~

## 基本

- 設定ファイルの読み込み

~~~
# nginx -s reload
~~~

- 確認

~~~
$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
~~~

現在の設定:

~~~
$ sudo nginx -T

$ sudo nginx -T | grep fastcgi | sort  | uniq
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
       fastcgi_param HTTP_HOST $my_host;
       fastcgi_param PATH_INFO $fastcgi_script_name;
       fastcgi_param SCRIPT_FILENAME $request_filename;
       fastcgi_pass phpfpm;
       fastcgi_read_timeout 1800;
       include fastcgi_params;
# configuration file /etc/nginx/fastcgi_params:
fastcgi_param  CONTENT_LENGTH     $content_length;
fastcgi_param  CONTENT_TYPE       $content_type;
fastcgi_param  DOCUMENT_ROOT      $document_root;
fastcgi_param  DOCUMENT_URI       $document_uri;
fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
fastcgi_param  HTTPS              $https if_not_empty;
fastcgi_param  QUERY_STRING       $query_string;
fastcgi_param  REDIRECT_STATUS    200;
fastcgi_param  REMOTE_ADDR        $remote_addr;
fastcgi_param  REMOTE_PORT        $remote_port;
fastcgi_param  REQUEST_METHOD     $request_method;
fastcgi_param  REQUEST_SCHEME     $scheme;
fastcgi_param  REQUEST_URI        $request_uri;
fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
fastcgi_param  SERVER_ADDR        $server_addr;
fastcgi_param  SERVER_NAME        $server_name;
fastcgi_param  SERVER_PORT        $server_port;
fastcgi_param  SERVER_PROTOCOL    $server_protocol;
fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;
~~~

## 1つのIPアドレスで、複数のSSLサイトを処理する:Server Name Identification (SNI)

- `disabled` だとSNIが使えない

~~~
# ../sbin/nginx -V
nginx version: nginx/0.7.67
TLS SNI support disabled
configure arguments: --with-http_ssl_module
~~~

-  `enabled` だと使える

~~~
# sbin/nginx -V
nginx version: nginx/1.9.2
built by gcc 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
built with OpenSSL 0.9.8g 19 Oct 2007
TLS SNI support enabled
configure arguments: --prefix=/usr/local/nginx-1.9.2 --user=www-data --group=www-data --with-http_ssl_module --with-http_realip_module
~~~


# 502

- [nginx リバースプロキシ設定時の502 Bad Gatewayエラーを解消する方法](http://www.crystalsnowman.com/?p=723)

supervisor: reread & restart だけだとだめで、reload

~~~
# supervisorctl reread
# supervisorctl reload
~~~


# その他

- [タイムアウト対策](nginx.timeout.md)
