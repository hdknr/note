Wordpress: 同一サイトで動くWebアプリに認証を委任させる

## Wordpressでめんどくさい業務処理したくない

- PHPならびにWordpressプラグインめんどくさい
- 業務処理は別途メジャーなWebフレームワーク使ったアプリでやりたい
- 認証の連携はなんとかしたい

## 方針

- Cookie共有サイト(nginxとかでホスト)にWordpressとアプリ(Djangoとか)共有させる
- アプリ側でWordpressのユーザーのプロビジョニングを行う(wp_users)
- WordpressとアプリでCookieで共有データを渡す


## アプリ側(Django)

### WordpressのMySQLにアクセスできるようにする

- settings.DATABASESにデータベースを追加して、 settings. DATABASE_ROUTERS でモデルとストレージの連携を定義する ([settings](https://github.com/hdknr/djpress/blob/master/sample/app/settings.py), [DatabaseRouter](https://github.com/hdknr/djpress/blob/master/sample/app/databases.py))
- inspectdb してモデルクラスを[用意する](https://github.com/hdknr/djpress/blob/master/lib/djpress/wordpress.py)

### ユーザー追加, 削除で wp_usersを操作する

- `from django.db.models.signals import post_save, post_delete` のシグナルハンドラを定義して、 WpUsersモデル(wp_usersテーブル) の追加更新/削除する ([signals.py](https://github.com/hdknr/djpress/blob/master/lib/djpress/signals.py))

### ログインした時に共有Cookieデータを設定する

- `from django.contrib.auth.signals import user_logged_in` のシグナルハンドラで共有Cookieデータを用意する
- 今回は `{{ wp_users.ID }}:{{ sha256(django_session_key + wp_users.id + shared_secret)}}` という文字列にしてセッションデータに保存([signals.py](https://github.com/hdknr/djpress/blob/master/lib/djpress/signals.py))
- HTTPレスポンスを返す時に`WP_USER`というCookieにセット([middleware.py](https://github.com/hdknr/djpress/blob/master/lib/djpress/middleware.py))

## Wordpress側(wp-authmodプラグイン)

-  Djangoがセットした sessionidと WP_USERでログイン/ログアウトの処理をするプラグインを実装してみた([wp-authmod](https://github.com/hdknr/wp-authmod))
- Wordpressのプラグインはよくわからない

### send_headers アクションで処理

- Wordpressが何かしかストリームに書いてしまうと、Set-Cookieなどヘッダーの処理するとWarningでるので、send_headersアクションで強制ログイン/ログアウト処理をやるのがいいのか(よくわからない)([Authmod/App.php](https://github.com/hdknr/wp-authmod/blob/master/Authmod/App.php))
- 単純にCookieデータを読んで検証し、受け取った`wp_users.ID`で [wp_set_current_user](https://codex.wordpress.org/Function_Reference/wp_set_current_user) と [wp_set_auth_cookie](https://codex.wordpress.org/Function_Reference/wp_set_auth_cookie) すればログインできるっぽい。
- WP_USERクッキーにデータがなかったらログオフされたものとして [wp_logout](https://codex.wordpress.org/Function_Reference/wp_logout) させるようにしてみた

### 共有シークレットなどの設定情報

- [update_option](https://codex.wordpress.org/Function_Reference/update_option) / [get_option](https://codex.wordpress.org/Function_Reference/get_option) で指定したキーでPHP Arrayをシリアライズしてwp_optionsで読み書きできるっぽい([Authmod/Option.php](https://github.com/hdknr/wp-authmod/blob/master/Authmod/Option.php))

### ダッシュボードからの設定

- Wordpressはテンプレートエンジンみたいなものは標準で無いようです
- [Timber](https://github.com/jarednova/timber/wiki) というプラグインがあって、これで [Jinja2](http://jinja.pocoo.org/docs/dev/) っぽい [Twig](http://twig.sensiolabs.org/documentation) を使える！
- Timberは wp-content/plugins/timber-library というディレクトリにインストールされる。
- Twigとかはwp-content/plugins/timber-library/vendorの下に [Comoposer](https://getcomposer.org/)管理で入れられている。
- wp-content/plugins/timber-library/timber.php でTimber関連のオートロードがされている。
- [spl_autoload_register](https://secure.php.net/manual/ja/function.spl-autoload-register.php)は複数のオートロードのハンドラを定義できるっぽいので、ググったやつを修正したオレオレオートローダ([bootstrap.php](https://github.com/hdknr/wp-authmod/blob/master/bootstrap.php))でrequire_onceしてみたらアクセスできた
- `$_GET` で `get_option`, `$_POST` で `update_option`する処理をして、[Admin.html](https://github.com/hdknr/wp-authmod/blob/master/Authmod/Admin.html)にHTMLフォームをTimberでレンダリングするようにしたらできた([Authmod/Admin.php](https://github.com/hdknr/wp-authmod/blob/master/Authmod/Admin.php))

## nginx

- vagrant box の Debian Jessie で動作させた
- Django は `/apps/` で動かした
- PHPは `/` から動くようにしていて、 Wordpressは `/wordpress` にインストールした

~~~
upstream php-fpm-wordpress {
  ip_hash;
  server unix:/tmp/dev-php-fpm.sock;
}

upstream django-apps{
  ip_hash;
  server unix:/vagrant/projects/wpauth/djpress/sample/logs/gunicorn.sock;
}

server {
    listen 80;
    listen [::]:80;

    server_name wp.deb;

    root /vagrant/projects/wpauth/www;
    index index.php index.html;

    access_log /vagrant/projects/wpauth/logs/access.log;
    error_log  /vagrant/projects/wpauth/logs/error.log debug;


    location /apps/assets {
        alias /vagrant/projects/wpauth/djpress/sample/assets;
    }

    location /apps {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header SCRIPT_NAME /apps;
        proxy_redirect off;
        if (!-f $request_filename) {
            proxy_pass http://django-apps;
            break;
        }
    }
    
    location ~ \.php$ {
        fastcgi_pass  php-fpm-wordpress;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_buffer_size  128k;
        fastcgi_buffers  256 16k;
        fastcgi_busy_buffers_size  256k;
        fastcgi_temp_file_write_size  256k;
        include  fastcgi_params;
    }
}
~~~

## WP-CLI

- [WP-CLI](http://wp-cli.org/) は使える。Wordpressのインストールもこれからできる。
- wp-cli.yml のディレクトリを `WP_CLI_CONFIG_PATH` にセットすること!
- wp-cli.yml を読んで、nginx, php-fpm の設定ファイルの作成などを[スクリプト](https://github.com/hdknr/wp-authmod/blob/master/dev/scaffold.bash)でやるようにしてみた
- YAMLからパラメータ抜き出すのに[shyaml](https://github.com/0k/shyaml)をPYPIからいれてみた。Composerで入るPHPのツールは無いものか。
- `wp plugin saffold wp-authmod` でプラグインの雛形が生成されて、[phpunit](https://phpunit.de/)のテストプログラムも生成される！
- Composer で phpunit いれると普通にプラグインの単体テストっぽいことができる。


