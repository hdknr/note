sosreport:

# sosreport

- [sosreportについて(Red Hat Enterprise Linux)](http://cloud.nifty.com/cs/catalog/cloud_faq/catalog_130726001371_1.htm)


## sosreport とは

- sosreport はシステム情報を採取するスクリプトです。
- どのカーネルで起動しているのか、どういったドライバがロードされているのか、 一般的なサービスの設定ファイルなどの情報が採取されます。
- また、既知の問題パターンに対していくつかの簡単な診断を行います。

## sosreportの実行

~~~bash
$ sudo sosreport -a
~~~

- sosreportが終了すると/tmp配下に以下の形式でbz2ファイルが作成される

~~~
sosreport-<任意の文字列>.<任意の数字>-XXXXX-XXXXX.tar.bz2
~~~
