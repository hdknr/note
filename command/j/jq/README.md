# jq

- [json #90](https://github.com/hdknr/note/issues/90)
- [github](https://stedolan.github.io/jq/)
- [インストール](jq.install.md)
- [基本フィルター](jq.basic_filter.md)

## オプション

- [--slup/-s](jq.select.md): 入力を一旦配列に変換してからフィルターを実行する (再JSON化ができる)

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


## Quick

オブジェクトに出力:


~~~bash
% .. | jq "{main: .category_code_main, sub:.category_code_sub, leaf: .category_code_leaf}"
~~~

~~~json
{
  "main": "C",
  "sub": "A",
  "leaf": "B"
}
...
~~~