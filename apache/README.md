# apache メモ

## SSL

- [ApacheでOpenSSLのセキュリティを強化する](http://qiita.com/sion_cojp/items/99fee211ceace3f76cff)

## NameVirtualHost は不要になります

~~~bash
# dpkg -l | grep apache
ii  apache2                             2.4.7-1ubuntu4.1              amd64        Apache HTTP Server
~~~

~~~bash
AH00548: NameVirtualHost has no effect and will be removed in the next release
~~~
