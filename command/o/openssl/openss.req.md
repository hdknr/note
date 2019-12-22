# req

## `-newkey` : キーも生成する

~~~bash
$ openssl req -out codesigning.csr -new -newkey rsa:2048 -nodes -keyout private.key
.
~~~

## `-subj`:  サブジェクトを指定する

SUBJECT情報：

~~~bash
$ openssl req -nodes -newkey rsa:2048 -keyout example.key -out example.csr -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=example.com"
.
~~~

## 例: `subject.txt` に書かれたサブジェクトでキーとCSRを生成する

~~~bash
#!/bin/bash
SUBJ=$(< subject.txt)
KEY=server.key
CSR=server.csr
KEYLEN=2048
openssl req -nodes -newkey rsa:$KEYLEN -keyout $KEY -out $CSR -subj "$SUBJ"
openssl req -in $CSR -text > dump.$CSR.txt
~~~

`subject.txt`:

~~~text
/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=example.com"
~~~
