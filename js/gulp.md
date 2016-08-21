- [glunt](glunt.md)
- [main-bower-filesを活用する](http://qiita.com/59naga/items/02ba2963fd957ef6cf36)
- [GruntとgulpでBower環境を作る](http://create-something.hatenadiary.jp/entry/2014/07/27/204633)
- [Node.js V6 系は新しすぎるので V5 系を使うことにする](http://neos21.hatenablog.com/entry/2016/05/27/102608)
- [gulp.js その4 プラグイン一覧](http://qiita.com/oreo3@github/items/0f037e7409be02336cb9)
- [gulp-main-bower-files](https://www.npmjs.com/package/gulp-main-bower-files)

# インストール

~~~bash
$ npm install bower gulp --save-dev -g
$ npm install gulp-main-bower-files --save-dev -g
$ npm install --save-dev gulp-uglify -g
~~~

- bower.json 作成

~~~bash
$ bower init
? name js
? description
? main file gulpfile.js
? keywords
? authors hdknr <gmail@hdknr.com>
? license ISC
? homepage
? set currently installed components as dependencies? Yes
? add commonly ignored files to ignore list? Yes
? would you like to mark this package as private which prevents it from being accidentally published to the registry? No

{
  name: 'js',
  description: '',
  main: 'gulpfile.js',
  authors: [
    'hdknr <gmail@hoge.com>'
  ],
  license: 'ISC',
  homepage: '',
  ignore: [
    '**/.*',
    'node_modules',
    'bower_components',
    'test',
    'tests'
  ],
  dependencies: {
    jquery: '^3.1.0'
  }
}

? Looks good? Yes
~~~

- gulpfile.js 作成

~~~bash
$ vi gulpfile.js
~~~

~~~js
var gulp = require('gulp');
var mainBowerFiles = require('gulp-main-bower-files');
var uglify = require('gulp-uglify');

// $ gulp uglify
gulp.task('uglify', function(){
    return gulp.src('./bower.json')
        .pipe(mainBowerFiles())
        .pipe(uglify())
        .pipe(gulp.dest('./libs'));
});
~~~

- 実行

~~~bash
$ gulp uglify
[04:52:35] Using gulpfile ~/Projects/HybridWebView/js/gulpfile.js
[04:52:35] Starting 'uglify'...
[04:52:36] Finished 'uglify' after 1.14 s
~~~

~~~bash
$ tree libs/
libs/
└── jquery
    └── dist
        └── jquery.js

2 directories, 1 file
~~~

## bootstrap : overrides が必要

- bootstrap 追加

~~~bash
$ bower install bootstrap --save
bower bootstrap#*               cached https://github.com/twbs/bootstrap.git#3.3.7
bower bootstrap#*             validate 3.3.7 against https://github.com/twbs/bootstrap.git#*
bower bootstrap#^3.3.7         install bootstrap#3.3.7

bootstrap#3.3.7 bower_components/bootstrap
└── jquery#3.1.0
~~~

- gulpfile.js 修正

~~~js
var gulp = require('gulp');
var mainBowerFiles = require('gulp-main-bower-files');
var uglify = require('gulp-uglify');
var gulpFilter = require('gulp-filter');

// $ gulp uglify
gulp.task('uglify', function(){
    var filterJS = gulpFilter('**/*.js', { restore: true });
    return gulp.src('./bower.json')
        .pipe(mainBowerFiles())
        .pipe(filterJS)
        .pipe(uglify())
        .pipe(filterJS.restore)
        .pipe(gulp.dest('./libs'));
});
~~~

- bower.json に overrides 追加

~~~js
{
  ...
  "overrides": {
    "bootstrap": {
       "main": ["./dist/js/bootstrap.js", "./dist/css/*.min.*", "./dist/fonts/*.*"]
    }
  },
  "dependencies": {
    "jquery": "^3.1.0",
    "bootstrap": "^3.3.7"
  }
}
~~~

- 実行/確認

~~~bash
$ gulp uglify
$ tree libs/
libs/
├── bootstrap
│   └── dist
│       ├── css
│       │   ├── bootstrap-theme.min.css
│       │   ├── bootstrap-theme.min.css.map
│       │   ├── bootstrap.min.css
│       │   └── bootstrap.min.css.map
│       ├── fonts
│       │   ├── glyphicons-halflings-regular.eot
│       │   ├── glyphicons-halflings-regular.svg
│       │   ├── glyphicons-halflings-regular.ttf
│       │   ├── glyphicons-halflings-regular.woff
│       │   └── glyphicons-halflings-regular.woff2
│       └── js
│           └── bootstrap.js
└── jquery
    └── dist
        └── jquery.js

7 directories, 11 files
~~~

## ファイルの一覧

- gulpfile.js にタスク追加

~~~js
gulp.task('files', function(){
    console.log(require('main-bower-files')());
});
~~~
~~~bash
$ gulp files
[05:19:25] Using gulpfile ~/Projects/HybridWebView/js/gulpfile.js
[05:19:25] Starting 'files'...
[ '/Users/hide/Projects/HybridWebView/js/bower_components/jquery/dist/jquery.js',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/js/bootstrap.js',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/css/bootstrap-theme.min.css',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/css/bootstrap-theme.min.css.map',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/css/bootstrap.min.css',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/css/bootstrap.min.css.map',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.eot',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.svg',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.ttf',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff',
  '/Users/hide/Projects/HybridWebView/js/bower_components/bootstrap/dist/fonts/glyphicons-halflings-regular.woff2' ]
[05:19:25] Finished 'files' after 40 ms
~~~

##  gulp-concat : ファイルを一つに

~~~bash
$ npm install --save-dev gulp-concat -g
~~~

- gulp のタスク修正

~~~js

var gulp = require('gulp');
var mainBowerFiles = require('gulp-main-bower-files');
var uglify = require('gulp-uglify');

var gulpFilter = require('gulp-filter');
var concat = require('gulp-concat');      // 追加

// $ gulp uglify
gulp.task('uglify', function(){
    var filterJS = gulpFilter('**/*.js', { restore: true });
    return gulp.src('./bower.json')
        .pipe(mainBowerFiles())
        .pipe(filterJS)
        .pipe(concat('vendor.js'))        // libs/vender.jsにまとめる
        .pipe(uglify())
        .pipe(filterJS.restore)
        .pipe(gulp.dest('./libs'));
});

~~~

- 実行/確認

~~~bash
$ gulp uglify
$ tree libs/
libs/
├── bootstrap
│   └── dist
│       ├── css
│       │   ├── bootstrap-theme.min.css
│       │   ├── bootstrap-theme.min.css.map
│       │   ├── bootstrap.min.css
│       │   └── bootstrap.min.css.map
│       └── fonts
│           ├── glyphicons-halflings-regular.eot
│           ├── glyphicons-halflings-regular.svg
│           ├── glyphicons-halflings-regular.ttf
│           ├── glyphicons-halflings-regular.woff
│           └── glyphicons-halflings-regular.woff2
└── vendor.js

4 directories, 10 files
~~~

- index.html で確認

~~~html
<html>

  <head>
    <link href="./libs/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
    <a href="#" class="btn btn-warning">Hello</a>

    <script src="./libs/vendor.js"></script>
    <script>
      $(function(){
        $('a').click(function(){ alert('Hello');});
      });
    </script>
  </body>
</html>
~~~
