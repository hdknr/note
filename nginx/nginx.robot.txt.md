## 設定

~~~js
server {
    ....
       location /robots.txt {
           alias /vagrant/robots.txt;
       }
   }
}
~~~


## 完全拒否

~~~
user-agent:*
disallow: /
~~~
