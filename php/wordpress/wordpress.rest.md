## WP REST API

- 4.7 以降で Coreに組み込まれている
- https://ja.wp-api.org/
- [WP Query](https://wpdocs.osdn.jp/%E9%96%A2%E6%95%B0%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9/WP_Query) の HTTPインターフェース
- [Class Reference/WP Query](https://codex.wordpress.org/Class_Reference/WP_Query)

REST:

- `GET /wp-json/wp/v2/posts`
- `POST /wp-json/wp/v2/users/4` 
- `GET /wp-json/wp/v2/posts?search=awesome`
- ....

## Pretty Permlinks


- `Settings` > `パーマリンク設定` : `共通設定` > `カスタム構造`: `/%postname%/`

~~~bash 
$ curl  http://localhost:8800/wp-json/wp/v2/posts/1 | jq ".content"
~~~

ページの `link[rel='https://api.w.org/']` を確認:

~~~html
<link rel="https://api.w.org/" href="http://develop.local:8800/wp-json/">
~~~


## 確認

~~~bash 
$ cd wordpress; php -S 0.0.0.0:8800
$ curl  http://localhost:8800/wp-json/wp/v2/posts/1 | jq ".content"
~~~

~~~json
{
  "rendered": "<p>WordPress へようこそ。これは最初の投稿です。編集もしくは削除してブログを始めてください !</p>\n",
  "protected": false                       
}
~~~