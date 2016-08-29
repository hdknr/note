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