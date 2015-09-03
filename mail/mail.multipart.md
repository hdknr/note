## multipart

- alternative, mixed, related をまず考える
- signed, encrypted はセキュアメールの時のみ
- digest, parallel は特殊用途

[RFC 2046 - Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types](https://www.ietf.org/rfc/rfc2046.txt)

- multipart/mixed  (個々のパートは、それぞれ異なるデータ)
- multipart/alternative (メールに含まれる全てのパートは形式が違えども同じ内容)
- multipart/digest(電子メールやネットニューズのメッセージを、複数個梱包するような用途)(mixedと同じ構文)
- multipart/parallel(メールに含まれる全てのパートを同時に利用する必要がある)

[RFC 1847 - Security Multiparts for MIME: Multipart/Signed and Multipart/Encrypted](https://www.ietf.org/rfc/rfc1847.txt)

- multipart/signed (署名付きのメッセージ)
- multipart/encrypted (暗号化されたメッセージ)

[RFC 2112 - The MIME Multipart/Related Content-type](https://www.ietf.org/rfc/rfc2112.txt)

- multipart/related (関連性が高いパートの集合によって構成されている)

## Link

- [SMTP multipart/alternative vs multipart/mixed](https://stackoverflow.com/questions/3902455/smtp-multipart-alternative-vs-multipart-mixed)

~~~
 mixed
   |
   +-- alternative
   |     +-- text/plain
   |     +-- related
   |           +-- text/html
   |           +-- image/{{type}}
   |           +-- image/{{type}}
   |
   +-- attachment
   +-- attachment
~~~

- 画像がない場合

~~~
alternative
  +-- text/plain
  +-- text/html
~~~
