## リンク

- http://roots.io/using-composer-with-wordpress/
- https://firegoby.jp/archives/4437


## ログアウト

- リダイレクト (functions.php)

~~~php
function redirect_logout_page(){
  $url = site_url('', 'http');
  wp_safe_redirect($url);
  exit();
}
add_action('wp_logout','redirect_logout_page');
~~~

### ajax

- [Wordpress Logout Using Ajax](http://stackoverflow.com/questions/24590295/wordpress-logout-using-ajax)
- [check_ajax_referer](http://bit.ly/2b5vqEp) - ブログの外部からのリクエストを間違って処理しないように AJAX リクエストを検証します
