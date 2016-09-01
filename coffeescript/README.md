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
