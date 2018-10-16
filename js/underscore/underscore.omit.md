# [_.ommit](https://underscorejs.org/#omit)

## nullフィールドをオブジェクト(辞書)から抜く

[omit](http://underscorejs.org/#omit) + [isNull](http://underscorejs.org/#isNull): 

~~~js
> const _ = require('underscore')
undefined

> _.omit([1, 2, null, 3, 4, null, 5], _.isNull)
{ '0': 1, '1': 2, '3': 3, '4': 4, '6': 5 }

> _.omit({a: 3, b: null, c: 5}, _.isNull)
{ a: 3, c: 5 }
~~~