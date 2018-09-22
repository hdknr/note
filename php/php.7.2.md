# PHP 7.2

Ubuntu 1604 でうまくいっていない

## mcrypto -> libsodium

- [Introduction - Libsodium documentation](https://download.libsodium.org/doc/)
- 使わないのがデフォルトの模様
- `libsodium-dev` を使う模様

記事:

- [PHP7.2で実装されたLibsodiumのサンプルコードまとめ - Qiita](https://qiita.com/fri13th/items/596de162c28d97d7aeed)

## libzip

- [libzip](https://libzip.org/)

~~~
----------------------------------------------------------------------------------
configure: WARNING: Libzip >= 1.2.0 needed for encryption support
----------------------------------------------------------------------------------
~~~

ソースからインストール:

~~~bash
mkdir /tmp/libzip
cd /tmp/libzip
curl -sSLO https://libzip.org/download/libzip-1.4.0.tar.gz
tar zxf libzip-1.4.0.tar.gz
cd libzip-1.4.0
mkdir build
cd build
cmake ../
make > /dev/null
sudo make install
~~~

php-build オプション:

~~~
--with-libzip=/usr/local/lib/libzip.so
~~~


## 記事

- [PHP7.2がリリースされたので野良ビルドしてみた - Qiita](https://qiita.com/m3m0r7/items/f1342bca10040cdff3ab)
- [How to install mcrypt in php7.2 | Lukáš Mešťan](https://lukasmestan.com/install-mcrypt-extension-in-php7-2/)
- [No sodium for 7.2 · Issue #101 · paragonie/halite](https://github.com/paragonie/halite/issues/101)
- [phpenvのよくあるエラーとその回答集 - ささきしき](https://siky.hateblo.jp/entry/2017/10/09/230633)
