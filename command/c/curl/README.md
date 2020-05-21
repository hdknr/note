# curl  ([#80](https://github.com/hdknr/scriptogr.am/issues/80))

## トピック

- [認証](curl.auth.md)
- [クッキー](curl.cookie.md)
- [CORS](curl.cors.md)
- [OPTIONS](curl.options.md)

## 統計情報を出さない (-s)

~~~bash
$ curl -s https://accounts.google.com/.well-known/openid-configuration | jq ".issuer"

"accounts.google.com"
~~~

## 自分のグローバルアドレスを確認

- http://ifconfig.me/ サービス

~~~bash
$ curl -s ifconfig.me
.
~~~

## stdout

- [bash - curl .gz file and pipe it for decompression - Ask Ubuntu](https://askubuntu.com/questions/538637/curl-gz-file-and-pipe-it-for-decompression)

~~~bash 
$ curl "$URL" | gunzip -c > filename
.
~~~

~~~bash 
$ curl -L https://example.com/mygzip.tar.gz | tar zxv
.
~~~

Zip:

~~~bash
$ curl https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip | jar xv
$ curl https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip | bsdtar -xvf-
.
~~~

## macos: curl: (35) SSL peer handshake failed, the server most likely requires a client certificate to connect

- [homebrewでinstallしたcurlがbrew cask install時のTLS1.2ではOSX標準のcurlが邪魔をしてうまく反映されなかった時の対処法 - production.log](http://blog.naoshihoshi.com/entry/2016/11/10/083000)

## Cookie

- [curl - HTTP Cookies](https://curl.haxx.se/docs/http-cookies.html)
- [curlでcookie情報を取得し利用する | 森の人ブログ](https://morinohito.site/it/command/curl-cookie)

## リンク

- [curlのオプション勉強したのでまとめ](http://d.hatena.ne.jp/hogem/20091122/1258863440)
- [curlコマンドをPythonやnode.jsのコードに変換する方法 - Qiita](https://qiita.com/tottu22/items/9112d30588f0339faf9b)

## 関連

- [pup](pup.md) : HTML の抜きだし
- [jq](jq.md): JSONの整形