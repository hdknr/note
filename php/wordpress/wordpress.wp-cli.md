## インストール

- [WP-CLIの使い方](http://qiita.com/IK12_info/items/4a9190119be2a0f347a0)


~~~bash 
$ mkdir bin
$ curl -o bin/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
$ chmod +x bin/wp-cli.phar
~~~

## Wordpressインストール

~~~bash 
$ bin/wp-cli.phar core download  --locale=ja --path=$PWD/wordpress
~~~

バージョン指定:
~~~bash
$ bin/wp-cli.phar core download --version=4.7.10  --locale=ja --path=$PWD/wordpress
~~~

ビルトインサーバー:

~~~bash 
$ cd wordpress; php -S 0.0.0.0:8800
~~~

### Pretty Permilnk

- `Settings` > `パーマリンク設定` : `共通設定` > `カスタム構造`: `/%postname%/`

## プラグインリスト

~~~bash
$ bin/wp plugin list

+-------------------------+----------+-----------+--------------+
| name                    | status   | update    | version      |
+-------------------------+----------+-----------+--------------+
| akismet                 | inactive | available | 3.1.11       |
.....
| rest-api                | active   | none      | 2.0-beta13.1 |
+-------------------------+----------+-----------+--------------+
~~~


## wp-config.php

~~~php
if ( defined( 'WP_CLI' ) ) {
    $_SERVER['HTTP_HOST'] = 'localhost';
}

if ( !defined( 'WP_CLI' ) ) {
    // remove x-pingback HTTP header
    add_filter('wp_headers', function($headers) {
        unset($headers['X-Pingback']);
        return $headers;
    });
    // disable pingbacks
    add_filter( 'xmlrpc_methods', function( $methods ) {
            unset( $methods['pingback.ping'] );
            return $methods;
    });
    add_filter( 'auto_update_translation', '__return_false' );
}
~~~
