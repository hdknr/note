# Webサイト TODO

## nginx

### スタティックファイル

#### favicon.ico

#### apple-touch-icon.png

- [サーバログにapple-touch-icon系URLの404エラーが多数記録されるので対策をしてみた記録 - Sakura scope](https://www.nishishi.com/blog/2017/07/apple_touch_ico.html)

### rotbot.txt

- [djang-robotsで配信管理](https://github.com/hdknr/annotated-django/blob/2.1.x/markdown/django/django.robots.md)

### sitemap.xml

- [Django sitemapフレームワーク](https://github.com/hdknr/annotated-django/blob/2.1.x/markdown/django/django.sitemap.md)

### ログ

ltsv形式で記録(/etc/nginx/conf.d/log_format.conf):

~~~conf
log_format ltsv 'time:$time_iso8601\t'
                'remote_addr:$remote_addr\t'
                'request_method:$request_method\t'
                'request_length:$request_length\t'
                'request_uri:$request_uri\t'
                'https:$https\t'
                'uri:$uri\t'
                'query_string:$query_string\t'
                'status:$status\t'
                'bytes_sent:$bytes_sent\t'
                'body_bytes_sent:$body_bytes_sent\t'
                'referer:$http_referer\t'
                'useragent:$http_user_agent\t'
                'forwardedfor:$http_x_forwarded_for\t'
                'request_time:$request_time\t'
                'upstream_response_time:$upstream_response_time';
~~~

~~~conf
server {
    ....
    access_log /var/log/nginx/yourweb.access.ltsv.log ltsv;
}
~~~


- cloudwatch にシッピング
- elasticsearch + kibana にシッピング

## gunicorn

### ログ

ローテーション(/etc/logrotate.d/gunicorn):

~~~conf
/data/projects/yourweb/logs/*.log /data/projects/yourweb/logs/*.sql {
    daily
    missingok
    rotate 104
    compress
    delaycompress
    notifempty
    su ubuntu ubuntu
    create 0640 ubuntu ubuntu
    sharedscripts
    postrotate
        kill -USR1 $(cat /data/projects/yourweb/logs/gunicorn.pid)
    endscript
}
~~~

- `gunicorn.pid` は 起動ファイル(gunicorn.pyとか) で指定

~~~py
pidfile = os.path.join(LOGS, "gunicorn.pid")
~~~

## アプリケーション

### ログ

### キャッシュ