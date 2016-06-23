## インストール

- [nginx](https://webtatic.com/packages/nginx18/)


~~~bash
$ rpm -ql nginx18

/etc/logrotate.d/nginx
/etc/nginx
/etc/rc.d/init.d/nginx
/etc/sysconfig/nginx
/usr/sbin/nginx
/usr/share/doc/nginx18-1.8.0
/usr/share/nginx
/var/lib/nginx
/var/log/nginx
~~~


## ディレクトリのアクセス権に注意

ディレクトリに 読み取り+実行権限を付与すること

- static ファイルのアクセスが 403
- upstreamのunixソケットのDjangoアプリにアクセスできない
