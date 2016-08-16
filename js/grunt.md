# grunt

- [Getting started](http://gruntjs.com/getting-started)
- [Gruntを試そう](https://app.codegrid.net/entry/grunt-introduction)
- [Gruntを使ってプロジェクトを自動化する、Myタスクメモ](http://tipsbear.com/grunt-task-memo/)
- [フロント開発をがんばるためにGulpとGruntに入門してみた](https://github.com/shoutakenaka/workshop-gulp-intro/blob/master/slide.md)

## インストール

~~~
$ npm install -g grunt-cli
$ npm install -g grunt
~~~

## Django Bower

- settings.py を編集

~~~
BOWER_INSTALLED_APPS = (
...
    'bootstrap',
...
)   
~~~

- インストール

~~~
$ ./manage.py bower install
~~~

- 確認

~~~
$ ls app/components/bower_components/bootstrap
Gruntfile.js  LICENSE  README.md  bower.json  dist  fonts  grunt  js  less  node_modules  package.js  package.json
~~~

もしかして、bowerでインストールしたbootstrapをDjangoのツリーから移動した方がいいかも。distだけあとで同期する。

- 初期化

~~~
$ cd app/components/bower_components/bootstrap
$ npm install
~~~

- 編集 & grunt

~~~
$ grunt
~~~

~~~
$ grunt dist
~~~

- 配置

~~~
$ ./manage.py collectstatic
~~~


## エラー

- [Fatal error: Unable to find local grunt.](http://qiita.com/ledsun/items/ea3038a28bc0bd50a1ac)
