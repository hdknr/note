# Let's Encrypt

## Ubuntu

~~~bash
$ sudo apt-get install letsencrypt
~~~

~~~bash 
$ dpkg -L letsencrypt

/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/letsencrypt
/usr/share/doc/letsencrypt/README.rst.gz
/usr/share/doc/letsencrypt/copyright
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/letsencrypt.1.gz
/usr/bin
/usr/bin/letsencrypt
/usr/share/doc/letsencrypt/changelog.Debian.gz
~~~

~~~bash
$ sudo letsencrypt certonly --standalone -d {{ ドメイン名前 }}
~~~

## 記事

- [Let’s encryptを利用して、https通信を構築する - Qiita](https://qiita.com/kouji555/items/4dbccc6aad32278e2cc6)
- [Let’s Encryptの使い方。standaloneとwebroot - Qiita](https://qiita.com/f_uto/items/4178a9fdd657b78672ea)
- [Let's Encrypt でワイルドカード証明書を発行してみる - Qiita](https://qiita.com/noumia/items/64d8bb59e35151fc4fd6)
- [let's encrypt で複数ホスト名対応な証明書を作る - 日記](https://tnamao.hatenablog.com/entry/2016/08/21/173521)
