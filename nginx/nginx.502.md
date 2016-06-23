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


## 記事

- [How to Fix 502 Bad Gateway Error Using Nginx](https://www.scalescale.com/tips/nginx/502-bad-gateway-error-using-nginx/)
- [How to resolve the gunicorn critical worker timeout error?](http://serverfault.com/questions/490101/how-to-resolve-the-gunicorn-critical-worker-timeout-error)
