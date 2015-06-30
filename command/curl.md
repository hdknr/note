## 統計情報を出さない (-s)

```
$ curl -s https://accounts.google.com/.well-known/openid-configuration | jq ".issuer"

"accounts.google.com"
```

## リンク

- [curlのオプション勉強したのでまとめ](http://d.hatena.ne.jp/hogem/20091122/1258863440)