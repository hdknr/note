# smtp_generic_maps

- [Postfix manual - generic(5)](http://www.postfix-jp.info/trans-2.2/jhtml/generic.5.html)
- デフォルト: empty
- ローカルマシンが インターネットドメイン名を持たず、localdomain.local のような ものを使っている場合に必要です。

- [Postfix設定パラメータ](http://www.postfix-jp.info/trans-2.2/jhtml/postconf.5.html#smtp_generic_maps)

- [Why does postfix on AWS give me &quot;Invalid MAIL FROM address provided&quot;? I have production access | ServerfaultXchanger | QueryXchanger | QueryXchanger](https://www.queryxchange.com/q/1_639297/why-does-postfix-on-aws-give-me-quot-invalid-mail-from-address-provided-quot-i-have-production-access/)

## 501: invalid_hostname_reject_code

- クライアントの HELO または EHLO コマンドパラメータが reject_invalid_hostnam 制限で拒否された場合の、数字の Postfix SMTP サーバ応答コード。

- [【postfix】envelope-FROMを強制的に付与する | Linuxサーバ管理で困ったこと。](https://ameblo.jp/server-study/entry-10270572107.html)
- [AWS+PostfixでSMTPリレーの設定 - Qiita](https://qiita.com/mogetarou/items/3775c15badd1ddc7d9ee)

main.cf:

~~~
local_header_rewrite_clients = static:all
canonical_classes = envelope_sender
canonical_maps = regexp:/etc/postfix/canonical.regexp
~~~

/etc/postfix/canonical.regexp:

~~~
/.*/  admin@yourdomain.com
~~~

## 554: access_map_reject_code

- クライアントが [access(5)](http://www.postfix-jp.info/trans-2.2/jhtml/access.5.html) マップ制限により拒否された


Postfix -> SES でリレーしているが、`hdknr@shop.co.jp` から `inquiry@hosting.com` に送ろうとして、 `hdknr@shop.co.jp` が `verified` じゃないためにエラーとなっている。 

~~~
Sep 30 06:06:18 ip-172-31-47-57 postfix/smtp[3057]: 54819FFAE4: 
to=<inquiry@hosting.com>, 
relay=email-smtp.us-west-2.amazonaws.com[52.25.81.135]:587, 
delay=1, 
delays=0.02/0.02/0.64/0.37, 
dsn=5.0.0, 
status=bounced (
    host email-smtp.us-west-2.amazonaws.com[52.25.81.135] said: 
    554 Message rejected: Email address is not verified. 
    The following identities failed the check in region US-WEST-2:
         hdknr@shop.co.jp (in reply to end of DATA command)
)
~~~