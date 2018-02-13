## 設定確認


~~~bash
$ sudo nginx -t -c /path/to/nginx.conf
~~~

Debian系の場合、設定ファイルは `/etc/nginx/nginx.conf` になります。
`include` などを相対パスで指定した場合は、　`/etc/nginx` からの相対パスになります。

~~~bash
$ sudo nginx -t -c /etc/nginx/nginx.conf
~~~

### コンパイルオプションの確認

[pam](nginx.auth.pam.md) が入っているかの確認:

~~~bash
$ sudo nginx -V  2>&1 |  sed 's/--/\n--/g' | grep pam
~~~

## default_server

- [How nginx processes a request](http://nginx.org/en/docs/http/request_processing.html)

- server_name が host と一致しない場合は、 一番最初に読み込まれた設定を使用。
- 嫌な場合は default_server と記述する。

## server_tokens

- [How to hide Nginx version](https://www.scalescale.com/tips/nginx/how-to-hide-nginx-version/)


## server_name

複数定義

~~~
server_name  ec.ic-tact.co.jp wp.deb;
~~~


## タイムアウト対応

- /etc/nginx/conf.d/timeout.conf

~~~
  proxy_connect_timeout       1200;
  proxy_send_timeout          1200;
  proxy_read_timeout          1200;
  send_timeout                1200;
~~~

## アップロードファイルサイズ

- /etc/nginx/site-enabled/yoursite.conf

~~~
server {
  client_max_body_size 30M;
  listen 80;
  ....
~~~

## ワーカープロセス数

自動:

~~~
worker_processes  auto;
~~~
