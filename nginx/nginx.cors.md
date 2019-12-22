# CORS

- [APIサーバを立てるためのCORS設定決定版 - Qiita](https://qiita.com/hirohero/items/886733f50f37404235db)
- [CORSまとめ - Qiita](https://qiita.com/tomoyukilabs/items/81698edd5812ff6acb34)

site-availables/app/cors.conf:

~~~conf
add_header Access-Control-Allow-Origin '*';
add_header Access-Control-Allow-Methods 'GET, POST, PUT, DELETE';
add_header Access-Control-Allow-Headers 'Origin, Authorization, Accept, Content-Type';
add_header Access-Control-Max-Age 3600;             # ブラウザがpreflight リクストをキャッシュ保持可能な期間

add_header Content-Type 'text/plain charset=UTF-8';
add_header Content-Length 0;
~~~

~~~conf
server {
    ...
    location / {
        if ($request_method = 'OPTIONS') {
            include 'site-availables/app/cors.conf';
            return 204;
        }
        ...
    }

    location ~ \.php$ {
        # alwaysオプションを付けて、常にヘッダが出力されるようにする
        add_header Access-Control-Allow-Origin '*' always;          # `*` だけだと許可されないケースがある。この場合、ホワイトリストをアプリ(この場合PHP)で管理して、ドメインを返す
        include 'site-availables/app/fastcgi.conf';
    }
}
~~~
