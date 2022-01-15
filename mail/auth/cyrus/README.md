# Cyrus

## Cyrun IMAP

What is Cyrus IMAP:

- Cyrus IMAP(サイラス[キュロス]アイマップ)とは、「メール」「連絡先」「カレンダー」サーバで、エンタープライズグループウェアとして利用できます。
- 1994年 Cyrus Projectとして開発スタート: カーネギーメロン大学により開発が進められています。


##  Cyrus SASL

- https://www.cyrusimap.org/sasl/


## ライブラリ/パッケージ

### Ubuntu


#### libsasl2

- [libsasl2-2: Cyrus SASL - authentication abstraction library](https://packages.ubuntu.com/focal/libsasl2-2)
- [libsasl2-modules: Cyrus SASL - pluggable authentication modules](https://packages.ubuntu.com/focal/libsasl2-modules)
- [libsasl2-dev: Cyrus SASL - development files for authentication abstraction library](https://packages.ubuntu.com/focal/libsasl2-dev)


 Cyrus SASL - pluggable authentication modules:

| プロトコル/用途 | ライブラリ                  |
| --------------- | --------------------------- |
| GSS API         | libsasl2-modules-gssapi-mit |
| LDAP            | libsasl2-modules-ldap       |
| OTP             | libsasl2-modules-otp        |
| SQL             | libsasl2-modules-sql        |
| DB              | libsasl2-modules-db         |


#### sasl2-bin :Cyrus SASL - administration programs for SASL users database

| **コマンド**                                      | 用途                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------ |
| /usr/bin/gen-auth                                 | generate various authentication strings                                  |
| /usr/bin/sasl-sample-client                       | Sample client program for demonstrating and testing SASL authentication. |
| /usr/bin/saslfinger                               | A utility to collect SMTP AUTH relevant configuration for Postfix        |
| /usr/sbin/sasl-sample-server                      | Sample server program for demonstrating and testing SASL authentication. |
| /usr/sbin/saslauthd                               | sasl authentication server                                               |
| /usr/sbin/sasldbconverter2                        | /etc/sasldb2 への変換                                                    |
| [/usr/sbin/sasldblistusers2](sasldblistusers2.md) | list users in sasldb(/etc/sasldb2)                                       |
| /usr/sbin/saslpasswd2                             | set a user's sasl password                                               |
| /usr/sbin/saslpluginviewer                        | list loadable SASL plugins and their properties                          |
| /usr/sbin/[testsaslauthd](testsaslauthd.md)       | test utility for the SASL authentication server                          |



### Python 

- [python-sasl: sasl3](https://github.com/sparkur/python-sasl3) (cyrus-sasl-devel依存)

