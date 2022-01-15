# Postfix

## アーキテクチャ

- [pipe](postfix.pipe.md)
- [canonical](postfix.canonical.md)

## Config

- [myhostname](postfix.myhostname.md)
- [virtual_mailbox_maps](postfix.virtual_mailbox_maps.md)
- [smtp_generic_maps](postfix.smtp_generic_maps.md)
- [smtp_sasl_password_maps](postfix.smtp_sasl_password_maps.md)

## Topic

- [Maildir](postfix.maildir.md)
- [maildrop](postfix.maildrop.md)
- [Jail環境](postfix.jail.md)
- [Postfix MySQL](postfix.mysql.md)
- [Postfix SASL: 認証](postfix.sasl.md)

## ログ

詳細のログを取りたい場合、 `stmpd -v` などと 冗長オプションで `master.cf` で起動する:

~~~
smtp      inet  n       -       y       -       -       smtpd -v
submission inet n       -       y       -       -       smtpd -v
~~~

- 平文認証の場合、パスワードなどがログに残るので注意

## Resource

- [Postfix/Mysql Virtual Mail How To](http://hostingsoftware.net/index.php?module=pagemaster&PAGE_user_op=view_page&PAGE_id=56)
- [ELB + PostfixでElasticなMTA(メール受信)システムの構築 – ELB Proxy Protocol Supportの活用 ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/build-elastic-mta-by-proxy-protocol-enabled-elb-and-postfix/)
- [Postfix から SES にリレーする](https://github.com/hdknr/scriptogr.am/blob/master/aws/ses/aws.postfix.md)