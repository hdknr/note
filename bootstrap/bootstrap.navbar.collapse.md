Bootstrap: navbarをデフォルトでcollapseさせる

- [http://getbootstrap.com/customize/](http://getbootstrap.com/customize/) でも良いかとおもいますが

## bower インストール

- [anyenvでnpm install bower -g](http://qiita.com/hidelafoglia/items/e1e85a785f4e1d5d0b29)


## grunt インストール

~~~
$ npm install -g grunt-cli
~~~

## bootstrap インストール

~~~
$ bower install bootstrap
$ cd bower_components/bootstrap/
~~~

## 依存パッケージインストール

~~~
$ npm install
~~~

## variables.less:@grid-float-breakpointの修正

~~~
$ vi less/variables.less 
~~~

- デカめのスクリーンでもcollapseするように変数を修正

~~~
//@grid-float-breakpoint:     @screen-sm-min;
@grid-float-breakpoint:    2000px; 
~~~

## ビルド

~~~
$ grunt dist
~~~

## dist を配布

~~~
$ tree dist
dist
├── css
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   ├── bootstrap-theme.min.css
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   └── bootstrap.min.css
├── fonts
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   └── glyphicons-halflings-regular.woff2
└── js
    ├── bootstrap.js
    ├── bootstrap.min.js
    └── npm.js

3 directories, 14 files

~~~
