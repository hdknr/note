# 引数

## bash スクリプト引数をJSON配列化


最初の引数に　`'a b c d e f g'`:

~~~bash
jq --compact-output --null-input '$ARGS.positional' --args -- $1
~~~ 

`a b c d e f g` をバラバラに引数 :
~~~bash
jq --compact-output --null-input '$ARGS.positional' --args -- "$@"
~~~ 

~~~json
["a","b","c","d","e","f","g"]
~~~
