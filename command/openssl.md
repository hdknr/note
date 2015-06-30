## SSLのハンドシェーク確認

- プロトコル指定

```
$ openssl s_client -connect db_vest:443 -ssl3

CONNECTED(00000003)
1478:error:14094410:SSL routines:SSL3_READ_BYTES:sslv3 alert handshake failure:/SourceCache/OpenSSL098/OpenSSL098-52/src/ssl/s3_pkt.c:1125:SSL alert number 40
1478:error:1409E0E5:SSL routines:SSL3_WRITE_BYTES:ssl handshake failure:/SourceCache/OpenSSL098/OpenSSL098-52/src/ssl/s3_pkt.c:546:

```

- 指定なし

```
$ openssl s_client -connect db_vest:443

CONNECTED(00000003)
depth=1 /C=JP/L=Academe2/O=National Institute of Hoge/OU=UPKI/OU=NII Open Domain CA - G2
verify error:num=20:unable to get local issuer certificate
verify return:0
---
Certificate chain
 0 s:/C=JP/L=Academe2/O=Tokyo Institute of Technology/OU=Information Planning Division/CN=hoge.ac.jp
   i:/C=JP/L=Academe2/O=National Institute of Hoge/OU=UPKI/OU=NIH Open Domain CA - G2
 1 s:/C=JP/L=Academe2/O=National Institute of HOge/OU=UPKI/OU=NIH Open Domain CA - G2
   i:/C=JP/O=SECOM Trust.net/OU=Security Communication RootCA1
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIE5DDDA8ygAwIBAgIINqM2VOTXFdIwDQYJKoZIhvcNAQEFBQAwfTELMAkGA1UE
...
mAO9K1/b4o4=
-----END CERTIFICATE-----
subject=/C=JP/L=Academe2/O=Tokyo Institute of Hoge/OU=Information Planning Division/CN=hoge.ac.jp
issuer=/C=JP/L=Academe2/O=National Institute of Hoge/OU=UPKI/OU=NIH Open Domain CA - G2
---
No client certificate CA names sent
---
SSL handshake has read 3070 bytes and written 328 bytes
---
New, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: 7F676E886855BA0BFDB6C1A5C48B2AE56D024055570676E1F3FA2DE760649ED5
    Session-ID-ctx: 
    Master-Key: E5D6856E19612E7B2CB5466F905D02EE3090967D5174030C11F965CB9196433561445824FA3A8A3566E6B717AB9644CF
    Key-Arg   : None
    Start Time: 1418857110
    Timeout   : 300 (sec)
    Verify return code: 0 (ok)
---

```

## プライベートキーからパスワードを抜く

~~~
$ sudo openssl rsa -in yourdomain.key -out yourdomain.key.nopass
~~~