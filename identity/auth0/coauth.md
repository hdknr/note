## [Cross-Origin Authentication](https://auth0.com/docs/cross-origin-authentication)

Auth0認証手順:

- [ユニバーサルログイン]('')
- [クロスオリジン認証]('') - アプリケーションにログインフォームを直接埋め込む


### What is Cross-Origin Authentication?


- 3rd パーティクッキーが必須です

#### Security in deprecated library versions


- [Cross-Origin Resource Sharing (CORS) Vulnerability Vulnerability in the auth0-js library (+3 More)](https://www.sourceclear.com/vulnerability-database/security/cross-origin-resource-sharing-cors/javascript/sid-5538)

### Limitations of Cross-Origin Authentication

- 3rd パーティクッキーを無効にされると動きません

カスタムドメイン方式:

- カスタムドメインを auth0 に設定して、トップレベルドメインを同じにする
- 例えば、 www.yourdomain.com に対して auth.yourdomain.com を auth0に設定する
- 3rd パーティクッキー問題がおきない

クロスオリジン確認ページ方式:

- 3rdパーティクッキーがない場合でも動くようにする

ユニバーサルログインにする:

- 3rdパーティクッキー問題がおきない



### Configure Your Application for Cross-Origin Authentication

### Create a Cross-Origin Verification Page

- 3rdパーティクッキーが使えない場合
- https のページを用意すること

crossOriginVerification() 呼びだし:

- 3rdパーティクッキーが使えるときは何もしない
- Dashbord: `Advanced` > `OAuth` で、 `Cross-Origin Verification Fallback` に設定したURLが `iframe` で呼ばれる


### Error Codes and Descriptions


### Browser Testing Matrix