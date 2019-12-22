# SSL

## http -> https を強制する

- `$http_x_forwarded_proto` で判定

~~~
    location / {
            if ($http_x_forwarded_proto != 'https') {
                return 301 https://$host$request_uri;
            }
            try_files $uri $uri/ =404;
            include sites-available/home/root.conf;
    }
~~~

## Let's Encrypt

- [Let's Encrypt](letsencrypt.md)