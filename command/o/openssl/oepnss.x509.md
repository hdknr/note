# `x509`: 証明書

## `-text`: テキスト形式で表示

~~~bash
$ openssl x509 -noout -in server.crt -subject
.
~~~

## `-subject`: サブジェクトの表示

~~~bash
$ openssl x509 -noout -in server.crt -subject
subject= /businessCategory=Private Organization/jurisdictionC=JP/serialNumber=011001120891/C=JP/ST=Tokyo/L=Shibuya/O=My Site-works, Inc./CN=www.mysite-works.com
~~~

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

## 証明書, CSR, キーの付け合わせ

~~~bash
openssl x509 -noout -modulus -in 証明書ファイル.crt | openssl md5
openssl req -noout -modulus -in  CSR.csr | openssl md5
openssl rsa -noout -modulus -in プライベートキーファイル.key | openssl md5
~~~

動作中のサーバーの証明書のmodulusの確認:

~~~bash
openssl s_client -connect wwww.youdomain.com:443 -showcerts < /dev/null  | openssl x509 -noout -modulus | openssl md5
~~~

~~~txt
MD5(stdin)= 6f1652f55f53eaba8a7615e4ba98cd0b
~~~
