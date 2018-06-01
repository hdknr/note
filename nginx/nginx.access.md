## IPアドレス

- [Module ngx_http_access_module](ngx_http_access_module.md) (ELBの考慮)
- [Nginx でIPアドレスによるアクセス制御を行う](http://dev.classmethod.jp/server-side/server/nginx-ip-access-control/)
- [Nginx Block And Deny IP Address OR Network Subnets](https://www.cyberciti.biz/faq/linux-unix-nginx-access-control-howto/)


## User Agent

- [HowTo: Nginx Block User Agent](https://www.cyberciti.biz/faq/unix-linux-appleosx-bsd-nginx-block-user-agent/)
- [How to block specific user agents on nginx web server](http://ask.xmodulo.com/block-specific-user-agents-nginx-web-server.html)

- /etc/nginx/useragent.rules ([Module ngx_http_map_module](http://nginx.org/en/docs/http/ngx_http_map_module.html) )

~~~
map $http_user_agent $badagent {
        default         0;
        ~*malicious     1;
        ~*backdoor      1;
        ~*netcrawler    1;
        ~Antivirx       1;
        ~Arian          1;
        ~webbandit      1;
}
~~~


- http セクション

~~~
http {
    .....
    include /etc/nginx/useragent.rules
}
~~~

- serverセクション

~~~
server {
    ....

    if ($badagent) {
        return 403;
    }

    ....
}
~~~
