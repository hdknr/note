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
