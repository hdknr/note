## nginx

- https://gist.github.com/trdarr/9212351

~~~
location /slack/ {
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header Host $http_host;
       proxy_redirect off;
       proxy_pass http://127.0.0.1:8080/;
       break;
}
~~~

~~~bash
$ curl http://your.nginex.server.com/slack/change_later/C275U6VQS -X POST -F "key=value"  
OK
~~~
