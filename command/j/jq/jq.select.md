# `select(boolean_expression)`

## 文字列一致

INPUT:

~~~json
[{"id": "first", "val": 1}, {"id": "second", "val": 2}]
~~~

コマンド:

~~~bash
$ cat input | jq '.[] | select(.id == "second")'
.
~~~

Output:

~~~json
{"id": "second", "val": 2}
~~~

## 結果をリスト化 (jq -s)

~~~bash
$ cat input | jq '.[] | select(.id == "second")' | jq -s

[
  {
    "id": "second",
    "val": 2
  }
]
~~~


## 記事

- [jqを使って少し複雑な条件式でフィルタリングする方法をまとめてみた](https://qiita.com/ttiger55/items/150e9a18313a55841a32)