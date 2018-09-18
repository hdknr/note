# オブジェクト

~~~js
> let o = Object.create({name: 'hdknr', age: 35});
undefined
> console.log(o.name, o.age);
hdknr 35
undefined
~~~

## [Object initializer/オブジェクト初期化子](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Operators/Object_initializer)

- [ES5での新しい表記法](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#New_notations_in_ECMAScript_2015)

~~~js
// Shorthand property names (ES2015)
var a = 'foo', b = 42, c = {};
var o = {a, b, c};                  // IE11 ではNGです
~~~

## 記事

- [オブジェクトの利用](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Working_with_Objects)