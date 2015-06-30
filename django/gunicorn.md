# いろいろ

## コマンドで起動すると動くが、supervisorの起動に失敗する

- root でコマンド実行した結果、ログファイルが root で出来てしまっていない？
- iniファイルで指定したuserの権限が不足していて、ログファイルに書き込めないで起動に失敗しているのでは。

## ログローテーション

- gunicorn.py でPIDファイルのパスを指定する

~~~
pidfile = os.path.join(LOGS, "gunicorn.pid")
~~~

- ローテーションスクリプトファイル

	- su user group で gunicron の起動ユーザーのファイル権限を指定する
	- create はこれと同じ user group にする
	- postrotate で `kill -USER1 $(cat pidffile)` させる([ドキュメント](https://gunicorn-docs.readthedocs.org/en/latest/deploy.html#logging))
	
~~~
/home/system/projects/mysite/web/logs/gunicorn.*.log {
        weekly
        missingok
        rotate 104
        compress
        delaycompress
        notifempty
        su system users
        create 0640 system users
        sharedscripts
        postrotate
            kill -USR1 $(cat /home/system/projects/mysite/web/logs/gunicorn.pid)
        endscript
}
~~~

- ローテーションスクリプトファイルの権限は root にすること

~~~
$ sudo logrotate -d etc/logrotate.d/gunicorn 

Ignoring etc/logrotate.d/gunicorn because the file owner is wrong (should be root).
~~~

- `/var/lib/logrotate/status` で確認