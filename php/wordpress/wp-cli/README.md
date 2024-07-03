# wp-cli

- [Config](https://make.wordpress.org/cli/handbook/references/config/) (wp-cli.yml に関して)

## インストール

- [WP-CLI の使い方](http://qiita.com/IK12_info/items/4a9190119be2a0f347a0)

```bash
$ mkdir bin
$ curl -o bin/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
$ chmod +x bin/wp-cli.phar
```

## Wordpress インストール

```bash
$ bin/wp-cli.phar core download  --locale=ja --path=$PWD/wordpress
```

バージョン指定:

```bash
$ bin/wp-cli.phar core download --version=4.7.10  --locale=ja --path=$PWD/wordpress
```

ビルトインサーバー:

```bash
$ cd wordpress; php -S 0.0.0.0:8800
```

### Pretty Permilnk

- `Settings` > `パーマリンク設定` : `共通設定` > `カスタム構造`: `/%postname%/`

## プラグインリスト

```bash
$ bin/wp plugin list

+-------------------------+----------+-----------+--------------+
| name                    | status   | update    | version      |
+-------------------------+----------+-----------+--------------+
| akismet                 | inactive | available | 3.1.11       |
.....
| rest-api                | active   | none      | 2.0-beta13.1 |
+-------------------------+----------+-----------+--------------+
```

## wp-config.php

```php
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
```

## アップデート

```bash
$ ../../bin/wp-cli.phar core update
PHP Notice:  Undefined index: HTTP_HOST in phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php(1197) : eval()'d code on line 87
PHP Stack trace:
PHP   1. {main}() /home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar:0
PHP   2. include() /home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar:4
PHP   3. include() phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/php/boot-phar.php:11
PHP   4. WP_CLI\bootstrap() phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/vendor/wp-cli/wp-cli/php/wp-cli.php:27
PHP   5. WP_CLI\Bootstrap\LaunchRunner->process() phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/vendor/wp-cli/wp-cli/php/bootstrap.php:74
PHP   6. WP_CLI\Runner->start() phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/vendor/wp-cli/wp-cli/php/WP_CLI/Bootstrap/LaunchRunner.php:23
PHP   7. WP_CLI\Runner->load_wordpress() phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php:1158
PHP   8. eval() phar:///home/vagrant/projects/sample/gpress/django-gpress/bin/wp-cli.phar/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php:1197
Updating to version 5.5 (ja)...
https://downloads.wordpress.org/release/ja/wordpress-5.5.zip から更新をダウンロード中...
更新を展開しています…
Cleaning up files...
No files found that need cleaning up.
Success: WordPress updated successfully.
```

## カスタムコマンド

- [【wp-cli の使い方】WordPress でバッチを作る方法](https://pecopla.net/web-column/wp-cli)
