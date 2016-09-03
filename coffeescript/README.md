## インストール

~~~bash
$ npm install coffee-script
~~~

~~~bash$
cat /tmp/test.coffee
~~~

### コンパイル

~~~coffee
hello = ->
  console.log("Hello World!")

hello()
~~~

~~~bash
$ coffee -c /tmp/test.coffee
$ node /tmp/test.js
Hello World!
~~~

### 直接実行

~~~bash
$ coffee /tmp/test.coffee
Hello World!
~~~



# リファレンス

- [CoffeeScript 言語リファレンス](http://memo.sappari.org/coffeescript/coffeescript-langref)
- [CoffeeScriptとJavaScriptやPythonやRubyの文法の比較](http://qiita.com/yuku_t/items/f2530dfe7ba71e9073929)

## ファイル分割

- [CoffeeScriptでclassをファイル分割する方法](http://qiita.com/mrpepper/items/e9643bdcc8f127fdacba)

## 記事

- [CoffeeScriptを使う理由](http://qiita.com/asaake/items/9462844b049900ffb22c)
- https://axiacore.com/blog/using-coffeescript-in-django-projects/
