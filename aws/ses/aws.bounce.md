# バウンス


## サプレッションリスト

一覧:

~~~bash
%  aws sesv2 list-suppressed-destinations --profile ictact | jq ".SuppressedDestinationSummaries[].EmailAddress"
~~~

削除:

~~~bash
%  aws sesv2 delete-suppressed-destination --email-address you-address@docomo.ne.jp --profile ictact
~~~


- [Amazon SES サプレッションリストに登録されている E メールアドレスを削除するにはどうすればよいですか?](https://aws.amazon.com/jp/premiumsupport/knowledge-center/ses-remove-email-from-suppresion-list/)
- [[アップデート] Amazon SES でサプレッションリストの登録と削除を一括で実行できるようになりました](https://dev.classmethod.jp/articles/amazon-ses-suppression-list-bulk-import/)


## SPF

`mydomain.com` (`TXT`):

~~~
v=spf1 +mx include:amazonses.com ~all
~~~

## DMARC

- [DMARCとは？](https://sendgrid.kke.co.jp/blog/?p=3137)


`_dmarc.mydomain.com` (`TXT`):

~~~
v=DMARC1;p=quarantine;pct=25;rua=mailto:admin@mydomain.com
~~~

## DKIM

| **name**                                                 | **CNAME値**                                         |
| -------------------------------------------------------- | --------------------------------------------------- |
| hmkuliesy2rmy3zlakcniy52fhjjkaak._domainkey.mydomain.com | hmkuliesy2rmy3zlakcniy52fhjjkaak.dkim.amazonses.com |
| hqyjmnm3zr25hhufitrqyksrjdxkavxf._domainkey.mydomain.com | hqyjmnm3zr25hhufitrqyksrjdxkavxf.dkim.amazonses.com |
| pdf7v6ptt3wwxzzrg3fzcpn6gz3f3a7l._domainkey.mydomain.com | pdf7v6ptt3wwxzzrg3fzcpn6gz3f3a7l.dkim.amazonses.com |
