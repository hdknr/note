# dig コマンド

~~~bash
$ dig +nocmd +noall +answer www.icloud.com

www.icloud.com.		3081	IN	CNAME	www-cdn.icloud.com.akadns.net.
www-cdn.icloud.com.akadns.net. 119 IN	CNAME	www.icloud.com.edgekey.net.
www.icloud.com.edgekey.net. 21097 IN	CNAME	e4478.a.akamaiedge.net.
e4478.a.akamaiedge.net.	19	IN	A	23.34.104.90
~~~

## soa

~~~bash
$ dig +nocmd +multiline +noall +answer soa icloud.com

icloud.com.             85850 IN SOA adns1.apple.com. hostmaster.apple.com. (
                                2011081885 ; serial
                                1800       ; refresh (30 minutes)
                                900        ; retry (15 minutes)
                                2592000    ; expire (4 weeks 2 days)
                                1800       ; minimum (30 minutes)
                                )
~~~


項目     | 内容
--------|-------
refresh | ゾーンの情報をリフレッシュするまでの時間
retry   | REFRESHでゾーン情報の更新ができなかった場合に、RETRYで指定された時間後に再度リフレッシュを試みる
expire  | 何らかの理由でゾーン情報のリフレッシュができない状態が続いた場合、セカンダリネームサーバが持っているデータをどれだけの時間利用してもよいか
minimum | Negative cache TTL: ネガティブキャッシュとは、存在しないドメイン名であるという情報のキャッシュを意味する

## ANY

~~~bash
$ dig @ns-1143.awsdns-14.org. yourdomain.jp ANY +noall +answer
~~~

### ネガティブキャッシュ

- [route53のネガティブキャッシュについて](https://siguniang.wordpress.com/2014/05/22/notes-on-route53-negative-caching/)
- 存在しないドメイン(NXDOMAIN)を問い合わせた時は、「そのドメインが存在しない」ということを一定期間キャッシュしてくれる。
- ドメイン追加前にうっかりフライングで新規ドメインを名前解決しようとするとネガティブキャッシュされていまい、ドメイン追加してもキャッシュが expire されるまでは名前解決できなくなってしまう。
