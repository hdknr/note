![image](./php.png)

## 基本
- [PHPの基礎まとめ（メモ）](http://qiita.com/kimriwon/items/85e92d29af34af804e7b)

### @ :エラー識別演算子

- [それでも僕が、エラー制御(抑制)演算子"@"を使う理由](http://d.hatena.ne.jp/noopable/20090726/1248589117)
- [PHP プログラマが "@" を使うべきでない 5 つの理由](http://sotarok.hatenablog.com/entry/20090721/1248112106)
- [php5.4で@(エラー制御演算子)はどう進化したのか？](http://blog.tamazawa.net/2011/12/php54.html)

## スクリプトのパス

```
$p = pathinfo(realpath(__FILE__));
echo $p["dirname"];
```


## Compared to Python

| | Python	| PHP	|
|:-------------|:----------------| :-------------|
| 型 | type(obj) | [get_class](http://php.net/manual/ja/function.get-class.php)($obj) |
| Loop |  for i in collection | foreach($collection as &$i) |


### Loop

-  python

```
a = [80, 100, 120]
for i in a:
   print a

```

- PHP

```
$a = array(80, 100, 120);
foreach($a as &$i){
    echo "{$i}¥n";
};
```

### 配列

#### 追加

~~~
<?php

$params = array();
$params['conditions'][] = "string1";
$params['conditions'][] = "string2";
echo json_encode($params, JSON_PRETTY_PRINT), "\n";
~~~
~~~
{
    "conditions": [
        "string1",
        "string2"
    ]
}
~~~

~~~
echo $params['conditions'][0],"\n";
echo $params['conditions'][1],"\n";
~~~

~~~
string1
string2
~~~

ところが、

~~~
$params['conditions'][4] = "string3";
echo json_encode($params, JSON_PRETTY_PRINT), "\n";
echo $params['conditions'][2],"\n";
echo $params['conditions'][3],"\n";
echo $params['conditions'][4],"\n";
~~~

~~~
{
    "conditions": {
        "0": "string1",
        "1": "string2",
        "4": "string3"
    }
}
PHP Notice:  Undefined offset: 2 in /tmp/x.php on line 13

PHP Notice:  Undefined offset: 3 in /tmp/x.php on line 14

string3
~~~

### 連想配列/dict : ポジションインデクシング

- PHP, Python ともにkeysをポジションインデクシングしてからvalueを取る

~~~
$columns = array(
    '名前' => 'name',
    '生年月日' => 'birthdate',
);
$keys = array_keys($columns);

for($i=0; $i < count(array_keys($keys)) ; $i++){
    echo $i, $columns[$keys[$i]], "\n";
}

~~~

~~~
# -*- coding: utf-8 -*-
profile = {
    '名前': 'name',
    '誕生日': 'birthdate',
}

keys = profile.keys()
for i in range(len(keys)):
    print i, profile[keys[i]]
~~~    