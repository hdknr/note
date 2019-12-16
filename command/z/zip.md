# zip/unzip

## stdin

ファイルのパーミッションは復元されないので注意:

~~~bash
$ curl https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip | jar xv
$ curl https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip | bsdtar -xvf-
~~~

## `-j`: ファイル名のみ

~~~bash
TODAY=`date '+%Y-%m-%d'`
zip $LOCAL/nginx.access.$TODAY.zip -j /var/log/nginx/access.log
~~~

## リソース

- [【 zip 】コマンド（基礎編）――ファイルをZIP形式で圧縮する：Linux基本コマンドTips（34） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1607/25/news021.html)
