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