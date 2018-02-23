- https://github.com/vuejs/vue-cli

## インストール: vue-cli + yarn

~~~~bash
$ npm install -g vue-cli
$ npm install -g yarn
~~~~


## 初期化

~~~bash
$ vue init webpack-simple theme
~~~


## npm packages

~~~bash
$ cd theme
$ npm install
~~~

## webpack.config.js 設定

[webapck.config.js](webpack.config.js):

~~~bash
$ vim webpack.config.js  
~~~

この例だと、 modules.json に リゾルバが検索するディレクトリを設定、
sources.json に バンドルするソースファイルをmodules.json のディレクトリより相対パスで設定する。
