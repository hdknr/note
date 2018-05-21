
[Cookies vs Tokens: The Definitive Guide]https://auth0.com/blog/cookies-vs-tokens-definitive-guide/



## クッキー vs. トークン まとめ


### クッキーベース認証

- よく使われている方法
- ステートフル。認証レコード/セッションをサーバー(セッションのデータをデータベースに保存)とクライアントサイド(セッションのキー情報をクッキーに)で保持する。


フロー:

1. ユーザーはログインクレデンシャルをを入力
2. サーバーは正しいクレデンシャルを受け取ったら署名されたらデータベースにセッションを作成。
3. このセッションのIDをブラウザのクッキーに返す。
4. 以降のリクエストでは、ブラウザがおくってくるセッションIDをデータベースから見つけて正しいセッションであれば正常な処理結果を返す
5. ユーザーがログアウトしたら、セッションをクライアント、サーバーサイドの両方で削除する

### トークンベース認証

- SPA(single page applications), IoT(Internet of Things)の隆盛と共に
- JWT(JSON Web Tokens) を使った認証(ほぼデファクトなので)
- ステートレス。サーバーはログインしたユーザー/JWTを所有しているユーザーののレコードを持たない
- リクエストのたびにトークンを検証して認証を行う
- ベアラートークン(`Authorization: Bearer {{token string}}`)   (あるいはPOST, もしくはクエリパラメータ) 

フロー:

1. ユーザーはログインクレデンシャルをを入力
2. サーバーは正しいクレデンシャルを受け取ったら署名されたトークンを返す
3. トークンはクライアントサイドに保存する。 
4. 以降のリクストでは、受け取ったトークンをベアラトークンで毎回渡す(あるいはPOST/クエリ)
5. サーバーはリクエストの度にJWTをデコードし、正しかったら正常な処理結果を返す
6. ユーザーがログアウトしたら、クライアントサイドに保存されているトークンを削除する

トークンの保存場所

1. ローカルストレージ
2. セッションストレージ
3. クッキー


## Where to Store Tokens?

通常はブラウザのローカルストレージ:

- ただし、ローカルストレージはドメインごとに分離されているので、別ドメインでの処理ではサクセスできない。(サブドメインは除く)

クッキー:

- JWTをクッキーに入れることもできる。が、サイズが4Kbyteであることに注意。

セッションストレージ:

- ローカルストレージと同様であるが、ブラウザを閉じると消えてしまうので注意。