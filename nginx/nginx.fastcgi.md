## キャッシュ

### 設定

Ubuntu(Debian) だと conf.d にファイルを追加する

~~~bash
$ cat /etc/nginx/conf.d/cache.conf

fastcgi_cache_path      /var/cache/nginx/default_server levels=1:2 keys_zone=default_server:15m inactive=7d max_size=1000m;
fastcgi_temp_path       /var/cache/nginx/temp 1 2;
fastcgi_cache_valid     200 2h;
fastcgi_cache_valid     302 2h;
fastcgi_cache_valid     301 4h;
fastcgi_cache_valid     any 1m;
~~~

サイト設定(Wordpressの例):

~~~
   #  キャッシュさせない($do_not_cache == 1) 条件の判定
   set $do_not_cache 0;
   if ($request_method !~ ^(GET)$) {
     set $do_not_cache 1;
   }
   if ($request_uri ~* "/wp-admin/|/xmlrpc.php|wp-.*.php|/feed/|index.php|sitemap(_index)?.xml") {
     set $do_not_cache 1;
   }
   if ($http_cookie ~* "comment_author|wordpress_[a-f0-9]+|wp-postpass|wordpress_no_cache|wordpress_logged_in") {
     set $do_not_cache 1;
   }

   location ~ \.php$ {
      # fastcgi Wordpress向け設定
      expires off;
      fastcgi_pass   wp_upstream;
      fastcgi_split_path_info ^(.+\.php)(/.+)$;
      fastcgi_keep_conn on;
      fastcgi_index   index.php;
      fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include         fastcgi_params;

      # キャッシュの設定
      fastcgi_cache_bypass $do_not_cache;
      fastcgi_no_cache $do_not_cache;
      fastcgi_cache_key    $scheme://$host$request_uri;
      fastcgi_cache default_server;
      fastcgi_pass_header X-Accel-Expires;

      # ヘッダーにキャッシュ状況を出力(確認用)
      add_header Fastcgi-Cache $upstream_cache_status;
   }
~~~

### 確認

~~~bash
$ curl -I https://www.mercury-works.com/en/product
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Wed, 27 Sep 2017 07:51:46 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
X-Powered-By: PHP/7.1.8
Link: <https://www.mercury-works.com/en/wp-json/>; rel="https://api.w.org/"
Link: <https://www.mercury-works.com/en/?p=3185>; rel=shortlink
Fastcgi-Cache: HIT
~~~

### クリア

~~~bash
$ sudo rm -rf /var/cache/nginx/default_server/*
~~~


## fastcgi 関連

- [9 Tips for Improving WordPress Performance](https://www.nginx.com/blog/9-tips-for-improving-wordpress-performance-with-nginx/)
- [Nginxのfastcgi_cacheでWordPressを高速化](http://takayukii.me/post/20160218631)
- [Nginxのプロキシキャッシュで画面が真っ白になる](http://takayukii.me/post/20160224683)
