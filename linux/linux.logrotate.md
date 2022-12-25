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


## 一般ユーザーのcrontabでローテーションする

ステータスファイルを作る

~~~bash
touch $HOME/bin/logrotate.status
~~~

設定(/home/ubuntu/bin/rotate/conf)

~~~bash
/home/ubuntu/backups/*.sql {
     daily
     rotate 7
     missingok
     compress
}
~~~

crontab:
~~~
00 5 *  * *  logrotate -s /home/ubuntu/bin/logrotate.status  /home/ubuntu/bin/rotate.conf 
~~~

## サンプル

- [Nginxログローテートの設定の実例](http://qiita.com/koudaiii/items/23322bf7037c6a7b1cea)
- [任意のログをlogrotateを使って管理する](https://qiita.com/Esfahan/items/a8058f1eb593170855a1)