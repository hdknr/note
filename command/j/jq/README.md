# jq

- [json #90](https://github.com/hdknr/note/issues/90)
- [github](https://stedolan.github.io/jq/)
- [インストール](jq.install.md)
- [基本フィルター](jq.basic_filter.md)

## Cookbook

- [Wordpress](jp.wordpress.md)

### pretty print ( jq ".")

- デフォルトです

~~~bash
$ curl -s https://accounts.google.com/.well-known/openid-configuration | jq "."
.
~~~

## 関連

- [curl](../../c/curl)
- [pup](../../p/pup.md) - HTMLのパーサー
