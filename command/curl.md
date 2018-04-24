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

## リンク

- [curlのオプション勉強したのでまとめ](http://d.hatena.ne.jp/hogem/20091122/1258863440)
