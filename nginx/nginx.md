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
