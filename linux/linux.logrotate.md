## 強制ローテーション

- [[Linux]logrotateを手動で強制実行する方法](http://dqn.sakusakutto.jp/2012/03/linux_logrotate.html)

- /var/lib/logrotate.status  の日付を変更する


## 実行

- テスト

~~~
$ sudo  /usr/sbin/logrotate -fd /etc/logrotate.d/nginx
~~~

- 実行

~~~
$ sudo  /usr/sbin/logrotate -f /etc/logrotate.d/nginx
~~~

## サイズ

- notifempty : 空だとローテーションしない
- ifempty: ログファイルが空でもローテーションする


## 実行記録(`/var/lig/logrotate/status`)

~~~bash
# cat /var/lib/logrotate/status  | grep word

"/backups/exports/wordpress.log" 2017-8-26-6:25:2
~~~

## サンプル

- [Nginxログローテートの設定の実例
](http://qiita.com/koudaiii/items/23322bf7037c6a7b1cea)
