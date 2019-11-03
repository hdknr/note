# zip/unzip

## stdin

ファイルのパーミッションは復元されないので注意:

~~~bash
$ curl https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip | jar xv
$ curl https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip | bsdtar -xvf-
~~~