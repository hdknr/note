タイムアウト対策

## conf.d: 時間を長くする

`/etc/nginx/conf.d/timout.conf` (Ubuntu):

~~~
proxy_connect_timeout       1200;
proxy_send_timeout          1200;
proxy_read_timeout          1200;
send_timeout                1200;
~~~

## アップロードサイズを大きくする

- [アップロードサイズ](http://qiita.com/n-oshiro/items/4816ad71b90a9967fa18)

`/etc/nginx/site-enabled/defaul` (Ubuntu):


~~~
server {
    ...
    client_max_body_size 300M
    ....
}
~~~
