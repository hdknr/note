# OpenSSL

## サブコマンド

[x509: 証明書](openssl.x509.md)

- テキストダンプ
- サブジェクトの表示
- 証明書から公開鍵を抜く

[req: CSR](openssl.req.md):

- サブジェクトを指定する(非インタラクティブ生成)
- プライベートキーも同時に作成する

[s_client](openssl.s_client.md)

- SSL/TLSクライアント

## `sha1` / `dgst -sha1`: SHA-1 ダイジェスト

### フィンガープリント確認

プライベートキー:

~~~bash
$ openssl pkcs8 -in ~/.ssh/private.pem -inform PEM -outform DER -topk8 -nocrypt | openssl sha1 -c
.
~~~

## `rsa`: キー

### 秘密鍵から公開鍵を生成する

~~~bash
$ openssl rsa -in key.txt -pubout -out pub.txt
.
~~~

### キーからパスワードを抜く

~~~bash
$ openssl rsa -in yourdomain.key -out yourdomain.key.nopass
.
~~~

### キーサイズの確認

~~~bash
$ openssl rsa -text -in sites-available/mysite/keys/server.key.nopass | grep Key
Private-Key: (4096 bit)
writing RSA key
~~~

## `x509`: 証明書

### 証明書から公開鍵を抜く

~~~bash
$ openssl x509 -pubkey -noout -in cer.txt  > cert.pub.txt
.
~~~

### X.509 をテキスト形式にする

~~~bash
$ openssl x509 -text -noout -in cer.txt  > cer.x509.txt
.
~~~

### DER -> PEM

~~~bash
$ openssl x509 -inform DER -outform PEM -text -in ~/Downloads/DigiCertSHA2ExtendedValidationServerCA.crt
.
~~~

## `pkcs12`: [RFC7292](https://tools.ietf.org/html/rfc7292)

- Javaキーストア

### PKCS12 作成

~~~bash
$ openssl pkcs12 -export -inkey private.pem -in cert.pem -out dist.p12
.
~~~
