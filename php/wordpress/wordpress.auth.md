## wp_set_current_user

- プラグインで強制ログイン状態にさせる
- ただし、認証Cookieを出すわけではないので、ブラウザにはCookieはこれだけでは帰らない

~~~php
    function action_pre_get_posts(){
        error_log("action:pre_get_posts");
        wp_set_current_user(1, 'supersupersuperuser');
    } 
~~~      


- プライベートポスト(ログインしないと見れない)

~~~
$ WP post get 4
+-----------------------+------------------------------+
| Field                 | Value                        |
+-----------------------+------------------------------+
| ID                    | 4                            |
| post_author           | 1                            |
| post_date             | 2015-08-13 09:29:20          |
| post_date_gmt         | 2015-08-13 00:29:20          |
| post_content          | 限定になります               |
| post_title            | 会員限定                     |
| post_excerpt          |                              |
| post_status           | private                      |
| comment_status        | open                         |
| ping_status           | open                         |
| post_password         |                              |
| to_ping               |                              |
| pinged                |                              |
| post_modified         | 2015-08-13 09:31:18          |
| post_modified_gmt     | 2015-08-13 00:31:18          |
| post_content_filtered |                              |
| post_parent           | 0                            |
| guid                  | http://wp.deb/wordpress/?p=4 |
| menu_order            | 0                            |
| post_type             | post                         |
| post_mime_type        |                              |
| comment_count         | 0                            |
+-----------------------+------------------------------+
~~~

~~~
$ curl -I http://wp.deb/wordpress/?p=4
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Thu, 13 Aug 2015 00:46:12 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
X-Powered-By: PHP/5.6.10
X-Pingback: http://wp.deb/wordpress/xmlrpc.php
Link: <http://wp.deb/wordpress/?p=4>; rel=shortlink
~~~

- コメントアウトすると

~~~
$ curl -I http://wp.deb/wordpress/?p=4
HTTP/1.1 404 Not Found
Server: nginx/1.6.2
Date: Thu, 13 Aug 2015 00:47:01 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
X-Powered-By: PHP/5.6.10
X-Pingback: http://wp.deb/wordpress/xmlrpc.php
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
Pragma: no-cache
~~~

## wp_set_auth_cookie
- 認証Cookieを返す

~~~php
    function action_pre_get_posts(){
        error_log("action:pre_get_posts");
        wp_set_current_user(1, 'supersupersuperuser');
        wp_set_auth_cookie(1);
    }  
~~~    

~~~bash
$ curl -I http://wp.deb/wordpress/?p=4
HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Thu, 13 Aug 2015 00:48:11 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
X-Powered-By: PHP/5.6.10
X-Pingback: http://wp.deb/wordpress/xmlrpc.php
Set-Cookie: wordpress_1814bead0024b3556916d6745e1e9b1f=admin%7C1439599691%7C9pIPXVJEaTf5uw3u3Azyet9Hs0unuBNXNuv37LFVtde%7C4d7653a1e0ef4773a65e273863ebb7c89dc76f201df512c424ccd001a6ea2382; path=/wordpress/wp-content/plugins; httponly
Set-Cookie: wordpress_1814bead0024b3556916d6745e1e9b1f=admin%7C1439599691%7C9pIPXVJEaTf5uw3u3Azyet9Hs0unuBNXNuv37LFVtde%7C4d7653a1e0ef4773a65e273863ebb7c89dc76f201df512c424ccd001a6ea2382; path=/wordpress/wp-admin; httponly
Set-Cookie: wordpress_logged_in_1814bead0024b3556916d6745e1e9b1f=admin%7C1439599691%7C9pIPXVJEaTf5uw3u3Azyet9Hs0unuBNXNuv37LFVtde%7Ce65938b26bdbd6c37d384bc5fe3d0e6e60bdcf9c1630e7e3793c5e5bcb6c92f0; path=/wordpress/; httponly
Link: <http://wp.deb/wordpress/?p=4>; rel=shortlink
~~~


## Resource

- [How to Set and Get or Delete Cookies with WordPress](http://www.codecheese.com/2013/11/how-to-set-and-get-or-delete-cookies-with-wordpress/)
- [PHPUnit Tests for WordPress Plugins: wp_redirect() and expected PHP errors](http://www.analysisandsolutions.com/blog/html/writing-phpunit-tests-for-wordpress-plugins-wp-redirect-and-continuing-after-php-errors.htm)