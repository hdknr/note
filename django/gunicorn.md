# いろいろ

## コマンドで起動すると動くが、supervisorの起動に失敗する

- root でコマンド実行した結果、ログファイルが root で出来てしまっていない？
- iniファイルで指定したuserの権限が不足していて、ログファイルに書き込めないで起動に失敗しているのでは。
- `--preload` [オプション](https://gunicorn-docs.readthedocs.org/en/develop/configure.html#preload-app)で動かしてみると、Djangoのアプリのロード時のエラーがわかる
- supervisrod のcommandにあるgunicornのパスがvirtualenvの元のことなる(のでPYPIのパッケージが不足しているとか)

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

- `/var/lib/logrotate/status` で確認 (Debian)

~~~
# grep guni /var/lib/logrotate/status
"/home/system/projects/mysite/web/logs/gunicorn.access.log" 2015-9-17
"/home/system/projects/mysite/web/logs/gunicorn.error.log" 2015-9-17
~~~

- CentOS

~~~
# tail /var/lib/logrotate.status

"/var/log/redis/redis.log" 2015-11-1
~~~


## ログがフラッシュされていない？

~~~bash
$ lsof -p $(cat gunicorn.pid) | grep log

gunicorn 883 user    3w   REG              253,2      906 12722437 /home/user/projects/web/logs/gunicorn.error.log
gunicorn 883 user    4w   REG              253,2        0 12722069 /home/user/projects/web/logs/gunicorn.access.log
gunicorn 883 user    7u  unix 0xffff8803fe09d240      0t0   819232 /home/user/projects/web/logs/gunicorn.sock

~~~

- [Can't get access log to work for gunicorn](http://stackoverflow.com/questions/13472842/cant-get-access-log-to-work-for-gunicorn)
- [Python の logging を設定するときは disable_existing_loggers に注意](http://qiita.com/methane/items/42978b7f51b4c4eb34d4)
- [Can't see errors in log #708](https://github.com/benoitc/gunicorn/issues/708)

- Django のLOGGINGの設定を、`'disable_existing_loggers': False ` にして supervisorctrl relead したら記録されたっぽい
