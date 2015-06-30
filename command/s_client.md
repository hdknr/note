## X.509 の情報
- [参考](http://www.shellhacks.com/en/HowTo-Check-SSL-Certificate-Expiration-Date-from-the-Linux-Shell)

### 接続

~~~
vagrant@10:~$ echo | openssl s_client -connect google.com:443 2>/dev/null

CONNECTED(00000003)
---
Certificate chain
 0 s:/C=US/ST=California/L=Mountain View/O=Google Inc/CN=*.google.com
   i:/C=US/O=Google Inc/CN=Google Internet Authority G2
 1 s:/C=US/O=Google Inc/CN=Google Internet Authority G2
   i:/C=US/O=GeoTrust Inc./CN=GeoTrust Global CA
 2 s:/C=US/O=GeoTrust Inc./CN=GeoTrust Global CA
   i:/C=US/O=Equifax/OU=Equifax Secure Certificate Authority
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIHgzCCBmugAwIBAgIIT28RbC47NwgwDQYJKoZIhvcNAQEFBQAwSTELMAkGA1UE

.....
~~~

### 有効期間
~~~
vagrant@10:~$ echo | openssl s_client -connect google.com:443 2>/dev/null | openssl x509 -noout -dates
notBefore=Dec 10 11:54:23 2014 GMT
notAfter=Mar 10 00:00:00 2015 GMT
~~~

### SHA1フィンガープリント

~~~
$ echo | openssl s_client -connect google.com:443 2>/dev/null | openssl x509 -noout -fingerprint

SHA1 Fingerprint=CA:C3:C2:A1:06:4E:14:D7:A2:9D:2B:7B:AB:91:25:64:6D:EC:96:C6
~~~

DERにダンプして計算

~~~
vagrant@10:~$ echo | openssl s_client -connect google.com:443 2>/dev/null | openssl x509  -outform DER | sha1sum 
cac3c2a1064e14d7a29d2b7bab9125646dec96c6  -
~~~

### 全て
~~~
echo | openssl s_client -connect google.com:443 2>/dev/null | openssl x509 -noout -text

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 8924155373108256736 (0x7bd8f8079682dfe0)
    Signature Algorithm: sha1WithRSAEncryption
        Issuer: C=US, O=Google Inc, CN=Google Internet Authority G2
        Validity
            Not Before: Dec 10 11:54:23 2014 GMT
            Not After : Mar 10 00:00:00 2015 GMT
        Subject: C=US, ST=California, L=Mountain View, O=Google Inc, CN=*.google.com
.......
~~~