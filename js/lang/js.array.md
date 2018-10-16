# 配列

## 参考

- [underscore.js](../underscore)
- [javascriptの連想配列と配列の違い](http://qiita.com/katsukii/items/168bee174073ae7ec7e4)
- [JavaScriptでforEach, filter, map, reduceとか](http://qiita.com/itagakishintaro/items/29e301f3125760b81302)

## in

~~~js
> var dict = {};
undefined
> 'a' in dict
false
> dict['a'] = 1
1
> 'a' in dict
true
~~~

## splice: 要素操作

- [splice](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

~~~js
> a = ['a', 'b', 'c', 'd', 'e']
> var from = 4
> var to = 1
~~~

### ２つの要素を交換

~~~js
> a[from] = a.splice(to, 1, a[from])[0]
> a
[ 'a', 'e', 'c', 'd', 'b' ]
~~~

### 要素を移動挿入

~~~js
> a.splice(to, 0, a.splice(from, 1)[0])
> a
[ 'a', 'b', 'e', 'c', 'd' ]
~~~

## push

~~~js
> a = []
[]
> a.push(1)
1
> a.push(2)
2
> a.push(3)
3
> a
[ 1, 2, 3 ]

~~~

## map

~~~js
> a = [1, 2, 3]
[ 1, 2, 3 ]
> a.map(function(e){ return e * e; });
[ 1, 4, 9 ]
~~~

## forEach

- [Array.prototype.forEach()](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

~~~js
var fs = ['institute_code', 'school_code', 'course_code'];
 fs.forEach(function(value, index, ar){
    var cn = pascalCase("student_" + value);   
    $("#" + cn).val(user[value]);
 });
~~~

## filter : 間引く

最新の活動オブジェクトのタイトルが設定されているエントリのみ残す：

~~~js

$scope.activities = data.filter(
function(e) {
  return e.last_activity && e.last_activity.title ;
});
~~~

## sort

~~~js
data.sort(function(a, b){
  if (a.last_announce.updated_at == b.last_announce.updated_at )
    return 0;
  // 最新の告知を先にする
  return ( a.last_announce.updated_at > b.last_announce.updated_at ) ? -1 : 1;
});
~~~

## range(Python)

- [JavaScriptでPythonのrange関数のようにリスト作成](http://qiita.com/zuzu/items/d2befdb1e02506d11513)

~~~bash
$ npm install jsranger
jsranger@1.1.1 node_modules/jsranger
~~~

~~~bash
> var jsranger = require('jsranger');
undefined
> jsranger(2, 20);
[ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ]
~~~

- [Javascript で python の range() みたいのを書いてみるメモ](http://cortyuming.hateblo.jp/entry/20131223/p2)
- [JavaScript function similar to Python range()ll](http://stackoverflow.com/questions/8273047/javascript-function-similar-to-python-range/8273091#8273091)
