## 強制ローテーション

- [[Linux]logrotateを手動で強制実行する方法](http://dqn.sakusakutto.jp/2012/03/linux_logrotate.html)

- /var/lib/logrotate.status  の日付を変更する
-


## 実行

- テスト

~~~
$ sudo  /usr/sbin/logrotate -fd /etc/logrotate.d/nginx
~~~

- 実行

~~~
$ sudo  /usr/sbin/logrotate -f /etc/logrotate.d/nginx
~~~
