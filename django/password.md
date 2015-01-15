# パスワードリセット

## 流れ

### リセット(password_reset())でトークンを発行する


### 確認(password\_reset\_confirm())でトークンを確認する



## トークンジェネレータ

### API

- make_token(user)
- check_token(user, token)


### デフォルトトークンジェネレータ(django.contrib.auth.tokens.PasswordResetTokenGenerator)のトークン

#### make_token(user)

- エンコード生成時刻(ts\_b36:django.utils.http.int\_to\_base36()): 生成時刻(timestamp)を作ってBASE36にします(int\_to\_base36)
- ソース文字列(value) : user.id + user.password + login_timestamp  + timestamp
- ハッシュ(hash): 塩ふりかけHMAC(salted_hmac)でMACを作成します。
- トークン = ts_b36 + '-' + hash

#### check_token(user, token)

- token == make_token(user) を確認します


### 塩ふりかけHMAC(django.utils.crypto.salted_hmac())

~~~
def salted_hmac(key_salt, value, secret= settings.SECRET_KEY)
~~~

- key_salt + secret の SHA1ダイジェストを生成し、派生キーとします
- この派生キーでvalueに対してHMACを作成して返します

