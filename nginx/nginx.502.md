502 Bad Gateway

## タイムしている

- /etc/nginx/conf.d/timeout.conf

~~~
proxy_connect_timeout       1200;
proxy_send_timeout          1200;
proxy_read_timeout          1200;
send_timeout                1200;
~~~

### gunicorn のタイムアウト

- gunicorn.py

~~~py
timeout = 600     #default 30
~~~
