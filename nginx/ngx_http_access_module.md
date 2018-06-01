
[Module ngx_http_access_module](http://nginx.org/en/docs/http/ngx_http_access_module.html)

## IPアドレス制限する 

/etc/nginx/sites-enabled/defualt:

~~~
server {

    location ^~ /admin/ {
        include /etc/nginx/sites-available/yourapp/admin.conf ;
    }
    ..
}
~~~


admin.conf:

~~~
....
allow 211.130.200.5;            # My Home
deny all;
break;
~~~

### ELB(ALB) 配下でリバースプロキシされている環境


- [ngx_http_realip_module](https://nginx.org/en/docs/http/ngx_http_realip_module.html) を使う

~~~bash 
$ nginx -T

...
 --with-http_realip_module
~~~

~~~
server {
    ...
    ## ELB: allowip のを判定するために必要
    # 
    set_real_ip_from 172.30.0.0/16;
    real_ip_header X-Forwarded-For;
    real_ip_recursive on;

    ...
}
~~~