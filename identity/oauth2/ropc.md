## RFC6749

- [1.3.3.  Resource Owner Password Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.3)
- [4.3.  Resource Owner Password Credentials Grant](https://tools.ietf.org/html/rfc6749#section-4.3)
- [10.7.  Resource Owner Password Credentials](https://tools.ietf.org/html/rfc6749#section-10.7)(セキュリティ考察)

v32:

- [10.2.  Client Impersonation](https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-10.2)

## SPAでの利用

[How secure is the OAuth2 "Resource Owner Password Credential" flow for single-page apps?](http://andyfiedler.com/2014/09/how-secure-is-the-oauth2-resource-owner-password-credential-flow-for-single-page-apps)

- SSL 必須: javascript 改ざんを防ぐ
- CORS ホワイトリスト: javascript クライアントのなりすましを防ぐ(client id と CORS許可ドメインとの検証(Originリクエストヘッダーの検証))
- IE9 以下ではCORSつかえないので無理
- リフレッシュトークンは使わない(トークン無効になったら再度ログインさせる)

Originヘッダーも詐称できるのでは？

- パスワードを知っているのは利用者本人だけなので、同時にパスワードも知らないと認証できないので問題ないのでは
- clinet_id もソースを読めばわかるし、つまりOriginヘッダーの検証はさほど意味がない
- 前提:  Authz(API)サーバーとSPAサーバーは高い信頼性がある


### SSR(Nuxt.jsなど)のサーバー環境

- フロントエンドはSSRサーバー(www.domain.com)で配信
- ログインはROPCでAPIサーバー(api.domain.com) で行う
- www.domain.com のストレージ(cookie/localStorage)にトークンを保存
- SSRサーバーでのセッション管理はROPCトークンを使う
- SSRサーバーからAPIサーバーへのサーバー間ではROPCトークンをフォワードして使う
- ページからの APIサーバーへのリクエストはストレージに保存したトークンを使う
 
 トークンはJWT:

 - SSRサーバーでの認証はJWTをサーバーサイドでも検証することで行う

 セッションタイムアウトをどうする?:

 - JWTの期限がきれたらログインしなおすのか？
 - トークンをリフレッシュした方がいいかも。この場合、 javascriptからリフレッシュトークのリクエストを行うときにOrginヘッダーを確認した方が良い


前提:

- 第３者にトークンが漏れないこと
- 第３者に利用者のパスワードが漏れないこと



## 記事

-  [JWT Token, Redux & SSR Patterns](https://spectrum.chat/thread/2dcd616b-0625-4293-adc1-eedd69e2d7ab)

- [Securing React Redux Apps With JWT Tokens](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0)

- [10 Things You Should Know about Tokens](https://auth0.com/blog/ten-things-you-should-know-about-tokens-and-cookies/#token-storage)

- [Cookies are bad for you: Improving web application security](http://sitr.us/2011/08/26/cookies-are-bad-for-you.html)