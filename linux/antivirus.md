

# Symantec AntiVirus for Linux

- ディスコン？ Symantec Endpoint Protection を使え？
- [Symantec Endpoint Protection](https://ja.wikipedia.org/wiki/Symantec_Endpoint_Protection)

## rtvscand

~~~
Nov 14 01:01:05 myserver3 symcfgd: subscriber 6 has left -- closed 0 remaining handles
Nov 14 01:01:06 myserver3 rtvscand: New virus definition file loaded. Version: 181113a.
Nov 14 01:01:06 myserver3 rtvscand: Download of virus definition file from LiveUpdate server succeeded.
Nov 14 02:00:38 myserver3 rtvscand: Scan started on selected drives and folders and all extensions.
Nov 14 02:01:22 myserver3 rtvscand: Could not scan 1 files inside /var/www/error/contact.html.var due to extraction errors encountered by the Decomposer Engines.
Nov 14 02:14:38 myserver3 rtvscand: Scan Complete:  Threats: 0   Scanned: 173368   Files/Folders/Drives Omitted: 1
~~~

~~~bash
$ sudo ps ax | grep sym
 3576 ?        S      2:10 /opt/Symantec/symantec_antivirus/symcfgd -l info
 4283 ?        Sl    42:59 /opt/Symantec/symantec_antivirus/rtvscand -l info
~~~


- [Symantec AntiVirus for Linux の運用コマンド](http://blog.torigoya.net/2012/02/19/sav-ope/)

~~~bash
# /opt/Symantec/symantec_antivirus/sav info --product
1.0.8.17
~~~

## 停止/起動

- [Symantec AntiVirus for Linux のデーモンを再起動する方法](https://support.symantec.com/ja_JP/article.TECH102181.html)

停止:
~~~bash
$ sudo /etc/init.d/symcfgd stop
~~~

起動:(symcfgd デーモンは rtvscand よりも先に開始する必要があります。)

~~~bash
$ sudo /etc/init.d/symcfgd start
$ sudo /etc/init.d/rtvscand start
~~~

# Symantec Endpoint Protection

## インストール条件

- [Symantec Endpoint Protection でサポートされる Linux のカーネル](https://support.symantec.com/ja_JP/article.TECH223240.html)
- [Symantec Endpoint Protection for Linux によく寄せられる質問](https://support.symantec.com/ja_JP/article.TECH231013.html)
- [Symantec AntiVirus for Linux はサポートされているか](http://d.hatena.ne.jp/bayan/20150129/1422536136)
