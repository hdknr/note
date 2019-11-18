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
