- [Webサイトで利用する](http://ja.onsen.io/guide/getting_started.html)

~~~
$ which npm
/Users/hide/.anyenv/envs/ndenv/shims/npm
~~~


~~~
$ npm install -g bower
/Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/bin/bower -> /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/bower/bin/bower
bower@1.6.5 /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/bower
~~~

~~~
$ npm root -g
/Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules
~~~

~~~
$ npm bin -g
/Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/bin
~~~

~~~
$ export PATH=$PATH:`npm bin -g`
~~~

~~~
$ which bower
/Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/bin/bower
~~~

~~~
$ tree .
.

0 directories, 0 files
~~~

~~~
$ bower install onsenui
bower onsenui#*             not-cached git://github.com/OnsenUI/OnsenUI-dist.git#*
bower onsenui#*                resolve git://github.com/OnsenUI/OnsenUI-dist.git#*
bower onsenui#*               download https://github.com/OnsenUI/OnsenUI-dist/archive/1.3.12.tar.gz
bower onsenui#*                extract archive.tar.gz
bower onsenui#*               resolved git://github.com/OnsenUI/OnsenUI-dist.git#1.3.12
bower angular#~1.4.3        not-cached git://github.com/angular/bower-angular.git#~1.4.3
bower angular#~1.4.3           resolve git://github.com/angular/bower-angular.git#~1.4.3
bower angular#~1.4.3          download https://github.com/angular/bower-angular/archive/v1.4.7.tar.gz
bower angular#~1.4.3           extract archive.tar.gz
bower angular#~1.4.3          resolved git://github.com/angular/bower-angular.git#1.4.7
bower onsenui#~1.3.12          install onsenui#1.3.12
bower angular#~1.4.3           install angular#1.4.7

onsenui#1.3.12 bower_components/onsenui
└── angular#1.4.7

angular#1.4.7 bower_components/angular
~~~

~~~bash
$ tree -d
.
└── bower_components
    ├── angular
    └── onsenui
        ├── css
        │   ├── font_awesome
        │   │   ├── css
        │   │   └── fonts
        │   └── ionicons
        │       ├── css
        │       └── fonts
        ├── js
        └── stylus
            └── components

13 directories
~~~

~~~
$ mkdir hello ; cd hello
$ ln -s ../bower_components components
~~~

- index.html

~~~html
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="components/onsenui/css/onsenui.css"/>
    <link rel="stylesheet" href="components/onsenui/css/onsen-css-components.css"/>
    <script src="components/angular/angular.js"></script>
    <script src="components/onsenui/js/onsenui.js"></script>

    <script>
      var module = ons.bootstrap('my-app', ['onsen']);
      module.controller('AppController', function($scope) { });
      module.controller('PageController', function($scope) {
        ons.ready(function() {
          console.log('initializing...');
        });
      });
    </script>

  </head>
  <body ng-controller="AppController">
    <ons-navigator>
      <ons-page ng-controller="PageController">
        <!-- Page content -->
      </ons-page>
    </ons-navigator>
  </body>
</html>
~~~
