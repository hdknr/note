#  jq `Basic filters`

| 名称                                     | 表現                | 補足                           |
| --------------------------------------- | ------------------- | ----------------------------- |
| `identity`                              | `.`                 |
| `Object Identifier-Index`               | `.foo` , `.foo.bar` |
| `Object Identifier-Index(Optional)`     | `.foo?`             |
| `Generic Object Index`                  | `.[<string>]`       |
| `Array Index`                           | `.[2]`              |
| `Array/Object Value Iterator`           | `.[]`               |
| `Array/Object Value Iterator(Optional)` | `.[]?`              |
| `Comma`                                 | `,`                 | 二つのフィルタのデリミタ          |
| `Pipe`                                  | `|`                 | 二つのフィルタの結合              |
| `Parenthesis`                           | `(     )`           | グルーピング                     |

## データソース

|　データソース     | コマンド                  |
| --------------- | ------------------------ |
| JSONオブジェクト  | `jq '.'`                 |
| JSONリスト       | `jq '.'` , `jq '.[]'`    |
| 改行区切りJSON    | JSONオブジェクトと扱いが同じ |

obj.json:

~~~json
{
  "levelname": "DEBUG",
  "asctime": "2019-05-14 11:38:08,307",
  "module": "<ipython-input-2-8eff1fd6171a>",
  "process": 12031,
  "thread": 140688013074560,
  "message": "xxxx"
}
~~~

list.json:

~~~json
[
  {
    "levelname": "DEBUG",
    "asctime": "2019-05-14 11:38:08,307",
    "module": "<ipython-input-2-8eff1fd6171a>",
    "process": 12031,
    "thread": 140688013074560,
    "message": "xxxx"
  },
  {
    "levelname": "DEBUG",
    "asctime": "2019-05-14 11:39:28,057",
    "module": "<ipython-input-3-8eff1fd6171a>",
    "process": 12031,
    "thread": 140688013074560,
    "message": "xxxx"
  },
  {
    "levelname": "DEBUG",
    "asctime": "2019-05-14 11:43:55,643",
    "module": "<ipython-input-2-8eff1fd6171a>",
    "pathname": "<ipython-input-2-8eff1fd6171a>",
    "lineno": 1,
    "process": 12246,
    "thread": 140069537325184,
    "message": "xxxx"
  }
]

~~~

cr.json:

~~~json
{
  "levelname": "DEBUG",
  "asctime": "2019-05-14 11:38:08,307",
  "module": "<ipython-input-2-8eff1fd6171a>",
  "process": 12031,
  "thread": 140688013074560,
  "message": "xxxx"
}
{
  "levelname": "DEBUG",
  "asctime": "2019-05-14 11:39:28,057",
  "module": "<ipython-input-3-8eff1fd6171a>",
  "process": 12031,
  "thread": 140688013074560,
  "message": "xxxx"
}
{
  "levelname": "DEBUG",
  "asctime": "2019-05-14 11:43:55,643",
  "module": "<ipython-input-2-8eff1fd6171a>",
  "pathname": "<ipython-input-2-8eff1fd6171a>",
  "lineno": 1,
  "process": 12246,
  "thread": 140069537325184,
  "message": "xxxx"
}
~~~

~~~bash
$ cat cr.json  | jq ".levelname"
"DEBUG"
"DEBUG"
"DEBUG"

$ cat cr.json  | jq ".[].levelname"
jq: error (at <stdin>:1): Cannot index string with string "levelname"
jq: error (at <stdin>:2): Cannot index string with string "levelname"
jq: error (at <stdin>:3): Cannot index string with string "levelname"

$ cat cr.json  | jq ".[]"
"DEBUG"
"2019-05-14 11:38:08,307"
"<ipython-input-2-8eff1fd6171a>"
12031
140688013074560
"xxxx"
"DEBUG"
"2019-05-14 11:39:28,057"
"<ipython-input-3-8eff1fd6171a>"
12031
140688013074560
"xxxx"
"DEBUG"
"2019-05-14 11:43:55,643"
"<ipython-input-2-8eff1fd6171a>"
"<ipython-input-2-8eff1fd6171a>"
1
12246
140069537325184
"xxxx"
~~~

~~~bash
$ cat list.json | jq ".levelname"
jq: error (at <stdin>:5): Cannot index array with string "levelname"

$ cat list.json | jq ".[].levelname"
"DEBUG"
"DEBUG"
"DEBUG"
~~~
