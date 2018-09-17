[#80](https://github.com/hdknr/scriptogr.am/issues/80)

## 統計情報を出さない (-s)

```
$ curl -s https://accounts.google.com/.well-known/openid-configuration | jq ".issuer"

"accounts.google.com"
```

## 自分のグローバルアドレスを確認

- http://ifconfig.me/ サービス

~~~bash
$ curl -s ifconfig.me
~~~

## POST

- [curlコマンドから HTTP POST する方法
](https://qiita.com/letsspeak/items/8c7266742371699ab45e)

FORM:

~~~bash
$ curl -F "name1=value1" -F "name2=value2" http://yourdomain/execute.script
~~~

JSON:

~~~bash
$ curl -X POST -H "Content-Type: application/json" -d '
{
    "name": "Manager",
    "description": "someone who manages"
}'
~~~

## stdout

- [bash - curl .gz file and pipe it for decompression - Ask Ubuntu](https://askubuntu.com/questions/538637/curl-gz-file-and-pipe-it-for-decompression)

~~~bash 
$ curl "$URL" | gunzip -c > filename
~~~

~~~bash 
$ curl -L https://example.com/mygzip.tar.gz | tar zxv
~~~

## リンク

- [curlのオプション勉強したのでまとめ](http://d.hatena.ne.jp/hogem/20091122/1258863440)


