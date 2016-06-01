## 参考

- [javascriptの連想配列と配列の違い](http://qiita.com/katsukii/items/168bee174073ae7ec7e4)

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
