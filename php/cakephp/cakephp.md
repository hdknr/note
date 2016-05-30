## 注意

- キャッシュ！ モデル、ビューなどを修正したらキャッシュのクリアが必要


## キャメルケース とスネークケース変換

- [javascriptでキャメルケースとスネークケースの相互変換](http://qiita.com/thelarch/items/cc4707e1c7ef0d73ba73)


- [JavaScriptを使ってスネークケース・キャメルケース・パスカルケースの変換](http://webdesign-dackel.com/2015/05/15/js-change-case/)

~~~javascript
function camelCase(str){
  str = str.charAt(0).toLowerCase() + str.slice(1);
  return str.replace(/[-_](.)/g, function(match, group1) {
      return group1.toUpperCase();
  });
}

function snakeCase(str){
  var camel = camelCase(str);
  return camel.replace(/[A-Z]/g, function(s){
    return "_" + s.charAt(0).toLowerCase();
  });
}

function pascalCase(str){
  var camel = camelCase(str);
  return camel.charAt(0).toUpperCase() + camel.slice(1);
}
~~~
