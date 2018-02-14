- [ngx_http_log_module](http://nginx.org/en/docs/http/ngx_http_log_module.html)


## リクスト処理時間 $request_time

~~~
request processing time in seconds with a milliseconds resolution;
time elapsed between the first bytes were read from the client
and the log write after the last bytes were sent to the client
~~~

~~~
log_format combined '$remote_addr - $remote_user [$time_local] '
       '"$request" $status $body_bytes_sent '
       '"$http_referer" "$http_user_agent $request_time"';
~~~       


##  $upstream_response_time


- [ngx_http_upstream_module](http://nginx.org/en/docs/http/ngx_http_upstream_module.html)


## LTSV

- [ltsv.org](http://ltsv.org/)
- [hekyou/python-ltsv](https://github.com/hekyou/python-ltsv)
- [LTSV FAQ - LTSV って何? どういうところが良いの?](http://d.hatena.ne.jp/naoya/20130209/1360381374)


/etc/nginx/conf.d/log_format.conf:

~~~
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

/etc/nginx/sites-enabled/your_site.conf

~~~
access_log /var/log/nginx/access.log ltsv;
~~~
