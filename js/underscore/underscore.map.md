# _.map


~~~js
> var _ = require('underscore')
undefined
~~~

## リストの場合

~~~js
> _.map([1, 2, 3], function(num){
...  return num * 11;
... });
[ 11, 22, 33 ]
~~~

## オブジェクトの場合

コールバック引数は、 `値`, `キー` の順番

~~~js
> _.map({x:1, y:2, z:3}, function(val, key){
...  return key +"=" + val * 11;
... });
[ 'x=11', 'y=22', 'z=33' ]
~~~