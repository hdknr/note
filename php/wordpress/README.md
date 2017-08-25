## トピック

- [Composerから入れる](wordpress.composer.md)
- [wp-cliコマンド](wordpress.wp-cli.md)
- [パスワード](wordpress.password.md)


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

- 確認画面のスキップ [How to log out without confirmation 'Do you really want to log out?"?](http://wordpress.stackexchange.com/questions/67336/how-to-log-out-without-confirmation-do-you-really-want-to-log-out)

### ajax

- [Wordpress Logout Using Ajax](http://stackoverflow.com/questions/24590295/wordpress-logout-using-ajax)
- [check_ajax_referer](http://bit.ly/2b5vqEp) - ブログの外部からのリクエストを間違って処理しないように AJAX リクエストを検証します
