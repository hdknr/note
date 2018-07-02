## PATCHがMETHOD_OTHERに変換されてしまうファイアウォール対応

- `METHOD_OTHER` 要求がきたら `418` を返す
- `418` エラーページとして、 名前付きロケーション(`@patch_backoffice`) に飛ばす

~~~
    location ^~ /backoffice/ {
        error_page 418 = @patch_backoffice;
        if ($request_method = "METHOD_OTHER") {
            return 418;
        }
        include /etc/nginx/sites-available/yoursite/backoffice.conf ;
    }
~~~

- 名つきロケーションの中で は同じアプリケーションにリバースプロキシする
- ただし、 `proxy_method` を強制的に `PATCH` にする

~~~
    location @patch_backoffice {
        proxy_method PATCH;
        include /etc/nginx/sites-available/yoursite/backoffice.conf ;
    }
~~~