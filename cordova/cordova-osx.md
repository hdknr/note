Cordova: cordova-osx  

- [apache/cordova-osx](https://github.com/apache/cordova-osx)のREADME.mdの写経

## Install

- [anyenv](https://github.com/riywo/anyenv) で ndenv 環境インストール済み

~~~bash
$ anyenv versions
ndenv:
  system
  v0.12.4
* v0.12.7 (set by /Users/hide/.anyenv/envs/ndenv/version)
pyenv:
  system
* 2.7.10 (set by /Users/hide/.anyenv/envs/pyenv/version)
  django
~~~

### Checkout

~~~bash
$ for i in lib plugman cli; do git clone https://github.com/apache/cordova-$i.git ; done
~~~

### cordova-lib

~~~bash
$ cd cordova-lib/cordova-lib
~~~

- install

~~~bash
$ npm install

npm WARN package.json cordova-lib@5.3.2-dev No license field.
npm WARN engine xmlbuilder@2.2.1: wanted: {"node":"0.8.x || 0.10.x"} (current: {"node":"0.12.7","npm":"2.11.3"})
npm WARN prefer global jasmine-node@1.14.5 should be installed with -g
npm WARN prefer global jshint@2.5.8 should be installed with -g
npm WARN engineStrict Per-package engineStrict (found in this package's package.json)
npm WARN engineStrict won't be used in npm 3+. Use the config setting `engine-strict` instead.
valid-identifier@0.0.1 node_modules/valid-identifier

osenv@0.1.0 node_modules/osenv

properties-parser@0.2.3 node_modules/properties-parser

underscore@1.7.0 node_modules/underscore

bplist-parser@0.0.6 node_modules/bplist-parser

q@1.0.1 node_modules/q

unorm@1.3.3 node_modules/unorm

rewire@2.1.3 node_modules/rewire

shelljs@0.3.0 node_modules/shelljs

semver@4.3.6 node_modules/semver

rc@0.5.2 node_modules/rc
├── strip-json-comments@0.1.3
├── deep-extend@0.2.11
├── ini@1.1.0
└── minimist@0.0.10

dep-graph@1.1.0 node_modules/dep-graph
└── underscore@1.2.1

npmconf@2.1.2 node_modules/npmconf
├── inherits@2.0.1
├── uid-number@0.0.5
├── ini@1.3.4
├── once@1.3.2 (wrappy@1.0.1)
├── nopt@3.0.4 (abbrev@1.0.7)
├── config-chain@1.1.9 (proto-list@1.2.4)
└── mkdirp@0.5.1 (minimist@0.0.8)

xcode@0.8.0 node_modules/xcode
├── node-uuid@1.3.3
└── pegjs@0.6.2

elementtree@0.1.6 node_modules/elementtree
└── sax@0.3.5

request@2.47.0 node_modules/request
├── caseless@0.6.0
├── aws-sign2@0.5.0
├── stringstream@0.0.4
├── tunnel-agent@0.4.1
├── forever-agent@0.5.2
├── oauth-sign@0.4.0
├── json-stringify-safe@5.0.1
├── node-uuid@1.4.3
├── qs@2.3.3
├── mime-types@1.0.2
├── combined-stream@0.0.7 (delayed-stream@0.0.5)
├── form-data@0.1.4 (mime@1.2.11, async@0.9.2)
├── http-signature@0.10.1 (assert-plus@0.1.5, asn1@0.1.11, ctype@0.5.3)
├── bl@0.9.4 (readable-stream@1.0.33)
├── tough-cookie@2.0.0
└── hawk@1.1.1 (cryptiles@0.2.2, sntp@0.2.4, boom@0.4.2, hoek@0.9.1)

glob@4.0.6 node_modules/glob
├── inherits@2.0.1
├── graceful-fs@3.0.8
├── once@1.3.2 (wrappy@1.0.1)
└── minimatch@1.0.0 (sigmund@1.0.1, lru-cache@2.7.0)

init-package-json@1.9.1 node_modules/init-package-json
├── promzard@0.3.0
├── read@1.0.7 (mute-stream@0.0.5)
├── validate-npm-package-name@2.2.2 (builtins@0.0.7)
├── npm-package-arg@4.0.2 (hosted-git-info@2.1.4)
├── validate-npm-package-license@3.0.1 (spdx-correct@1.0.1, spdx-expression-parse@1.0.0)
├── glob@5.0.14 (path-is-absolute@1.0.0, inherits@2.0.1, once@1.3.2, inflight@1.0.4, minimatch@2.0.10)
└── read-package-json@2.0.1 (graceful-fs@4.1.2, json-parse-helpfulerror@1.0.3, normalize-package-data@2.3.4)

cordova-registry-mapper@1.1.12 node_modules/cordova-registry-mapper
└── tape@3.5.0 (inherits@2.0.1, resumer@0.0.0, defined@0.0.0, deep-equal@0.2.2, through@2.3.8, object-inspect@0.4.0, glob@3.2.11)

tar@1.0.2 node_modules/tar
├── inherits@2.0.1
├── block-stream@0.0.8
└── fstream@1.0.8 (graceful-fs@4.1.2, mkdirp@0.5.1, rimraf@2.4.3)

cordova-serve@0.1.3 node_modules/cordova-serve
├── mime@1.3.4
├── combined-stream@1.0.5 (delayed-stream@1.0.0)
├── q@1.4.1
├── chalk@1.1.1 (escape-string-regexp@1.0.3, supports-color@2.0.0, ansi-styles@2.1.0, strip-ansi@3.0.0, has-ansi@2.0.0)
├── shelljs@0.5.3
└── d8@0.4.4 (m8@0.4.4)

jasmine-node@1.14.5 node_modules/jasmine-node
├── mkdirp@0.3.5
├── walkdir@0.0.10
├── jasmine-growl-reporter@0.0.3 (growl@1.7.0)
├── coffee-script@1.10.0
├── gaze@0.3.4 (minimatch@0.2.14, fileset@0.1.8)
├── requirejs@2.1.20
└── jasmine-reporters@1.0.2

jshint@2.5.8 node_modules/jshint
├── strip-json-comments@1.0.4
├── underscore@1.6.0
├── exit@0.1.2
├── minimatch@1.0.0 (sigmund@1.0.1, lru-cache@2.7.0)
├── console-browserify@1.1.0 (date-now@0.1.4)
├── cli@0.6.6 (glob@3.2.11)
└── htmlparser2@3.8.3 (domelementtype@1.3.0, entities@1.0.0, domhandler@2.3.0, readable-stream@1.1.13, domutils@1.5.1)

aliasify@1.7.2 node_modules/aliasify
└── browserify-transform-tools@1.3.3 (through@2.3.8, falafel@1.0.1)

plist@1.1.0 node_modules/plist
├── util-deprecate@1.0.0
├── base64-js@0.0.6
├── xmldom@0.1.19
└── xmlbuilder@2.2.1 (lodash-node@2.4.1)

cordova-js@4.1.1 node_modules/cordova-js
└── browserify@10.1.3 (builtins@0.0.7, https-browserify@0.0.1, tty-browserify@0.0.0, htmlescape@1.1.0, isarray@0.0.1, inherits@2.0.1, string_decoder@0.10.31, constants-browserify@0.0.1, path-browserify@0.0.0, os-browserify@0.1.2, browser-resolve@1.9.1, commondir@0.0.1, through2@1.1.1, process@0.11.2, stream-browserify@1.0.0, xtend@4.0.0, shell-quote@0.0.1, defined@1.0.0, punycode@1.3.2, domain-browser@1.1.4, shallow-copy@0.0.1, duplexer2@0.0.2, deep-equal@1.0.1, querystring-es3@0.2.1, assert@1.3.0, timers-browserify@1.4.1, deps-sort@1.3.9, util@0.10.3, events@1.0.2, console-browserify@1.1.0, concat-stream@1.4.10, vm-browserify@0.0.4, has@1.0.1, parents@1.0.1, readable-stream@1.1.13, subarg@1.0.0, http-browserify@1.7.0, read-only-stream@1.1.1, url@0.10.3, shasum@1.0.1, resolve@1.1.6, labeled-stream-splicer@1.0.2, buffer@3.5.0, JSONStream@1.0.6, syntax-error@1.1.4, crypto-browserify@3.9.14, browser-pack@4.0.4, browserify-zlib@0.1.4, insert-module-globals@6.6.0, module-deps@3.9.1)

istanbul@0.3.21 node_modules/istanbul
├── abbrev@1.0.7
├── async@1.4.2
├── nopt@3.0.4
├── wordwrap@1.0.0
├── once@1.3.2 (wrappy@1.0.1)
├── supports-color@3.1.1 (has-flag@1.0.0)
├── mkdirp@0.5.1 (minimist@0.0.8)
├── esprima@2.5.0
├── resolve@1.1.6
├── fileset@0.2.1 (glob@5.0.14, minimatch@2.0.10)
├── which@1.1.2 (is-absolute@0.1.7)
├── escodegen@1.6.1 (esutils@1.1.6, estraverse@1.9.3, optionator@0.5.0, source-map@0.1.43, esprima@1.2.5)
├── js-yaml@3.4.2 (esprima@2.2.0, argparse@1.0.2)
└── handlebars@4.0.3 (source-map@0.4.4, optimist@0.6.1, uglify-js@2.4.24)

cordova-app-hello-world@3.9.0 node_modules/cordova-app-hello-world

npm@2.14.6 node_modules/npm
~~~

- link

~~~
$ npm link
npm WARN engineStrict Per-package engineStrict (found in this package's package.json)
npm WARN engineStrict won't be used in npm 3+. Use the config setting `engine-strict` instead.
/Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/cordova-lib -> /Users/hide/Projects/cordova-osx/cordova-lib/cordova-lib
~~~

### cordova-cli

~~~bash
$ cd ../../cordova-cli
~~~

- cordova-lib のリンク

~~~bash
$ npm link cordova-lib
/Users/hide/Projects/cordova-osx/cordova-cli/node_modules/cordova-lib -> /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/cordova-lib -> /Users/hide/Projects/cordova-osx/cordova-lib/cordova-lib
~~~

- install

~~~bash
$ npm install

npm WARN package.json cordova@5.3.2-dev license should be a valid SPDX license expression
npm WARN prefer global jasmine-node@1.14.5 should be installed with -g
npm WARN engineStrict Per-package engineStrict (found in this package's package.json)
npm WARN engineStrict won't be used in npm 3+. Use the config setting `engine-strict` instead.
ansi@0.3.0 node_modules/ansi

underscore@1.7.0 node_modules/underscore

q@1.0.1 node_modules/q

nopt@3.0.1 node_modules/nopt
└── abbrev@1.0.7

update-notifier@0.5.0 node_modules/update-notifier
├── is-npm@1.0.0
├── chalk@1.1.1 (escape-string-regexp@1.0.3, supports-color@2.0.0, ansi-styles@2.1.0, has-ansi@2.0.0, strip-ansi@3.0.0)
├── string-length@1.0.1 (strip-ansi@3.0.0)
├── repeating@1.1.3 (is-finite@1.0.1)
├── semver-diff@2.0.0 (semver@4.3.6)
├── configstore@1.2.1 (object-assign@3.0.0, os-tmpdir@1.0.1, graceful-fs@4.1.2, uuid@2.0.1, xdg-basedir@2.0.0, osenv@0.1.3, write-file-atomic@1.1.3, mkdirp@0.5.1)
└── latest-version@1.0.1 (package-json@1.2.0)

grunt@0.4.5 node_modules/grunt
├── which@1.0.9
├── dateformat@1.0.2-1.2.3
├── getobject@0.1.0
├── eventemitter2@0.4.14
├── rimraf@2.2.8
├── colors@0.6.2
├── async@0.1.22
├── hooker@0.2.3
├── grunt-legacy-util@0.2.0
├── exit@0.1.2
├── nopt@1.0.10 (abbrev@1.0.7)
├── minimatch@0.2.14 (sigmund@1.0.1, lru-cache@2.7.0)
├── glob@3.1.21 (inherits@1.0.2, graceful-fs@1.2.3)
├── lodash@0.9.2
├── coffee-script@1.3.3
├── underscore.string@2.2.1
├── iconv-lite@0.2.11
├── findup-sync@0.1.3 (glob@3.2.11, lodash@2.4.2)
├── grunt-legacy-log@0.1.2 (grunt-legacy-log-utils@0.1.1, underscore.string@2.3.3, lodash@2.4.2)
└── js-yaml@2.0.5 (argparse@0.1.16, esprima@1.0.4)

jasmine-node@1.14.5 node_modules/jasmine-node
├── mkdirp@0.3.5
├── jasmine-growl-reporter@0.0.3 (growl@1.7.0)
├── walkdir@0.0.10
├── coffee-script@1.10.0
├── gaze@0.3.4 (minimatch@0.2.14, fileset@0.1.8)
├── requirejs@2.1.20
└── jasmine-reporters@1.0.2

istanbul@0.3.21 node_modules/istanbul
├── abbrev@1.0.7
├── async@1.4.2
├── wordwrap@1.0.0
├── supports-color@3.1.1 (has-flag@1.0.0)
├── once@1.3.2 (wrappy@1.0.1)
├── which@1.1.2 (is-absolute@0.1.7)
├── mkdirp@0.5.1 (minimist@0.0.8)
├── esprima@2.5.0
├── resolve@1.1.6
├── fileset@0.2.1 (glob@5.0.14, minimatch@2.0.10)
├── escodegen@1.6.1 (esutils@1.1.6, estraverse@1.9.3, optionator@0.5.0, source-map@0.1.43, esprima@1.2.5)
├── js-yaml@3.4.2 (esprima@2.2.0, argparse@1.0.2)
└── handlebars@4.0.3 (source-map@0.4.4, optimist@0.6.1, uglify-js@2.4.24)

grunt-retire@0.3.7 node_modules/grunt-retire
├── async@0.9.2
├── grunt-contrib-clean@0.6.0 (rimraf@2.2.8)
├── request@2.51.0 (caseless@0.8.0, aws-sign2@0.5.0, forever-agent@0.5.2, stringstream@0.0.4, tunnel-agent@0.4.1, oauth-sign@0.5.0, json-stringify-safe@5.0.1, qs@2.3.3, node-uuid@1.4.3, mime-types@1.0.2, combined-stream@0.0.7, bl@0.9.4, http-signature@0.10.1, form-data@0.2.0, hawk@1.1.1, tough-cookie@2.0.0)
├── retire@0.3.8 (commander@2.5.1, walkdir@0.0.7, read-installed@3.1.5)
├── grunt-contrib-jshint@0.10.0 (hooker@0.2.3, jshint@2.5.11)
└── grunt-contrib-nodeunit@0.4.1 (hooker@0.2.3, nodeunit@0.9.1)

~~~

### cordova-plugman

~~~bash
$ cd ../cordova-plugman
~~~

- cordova-lib リンク

~~~bash
$ npm link cordova-lib

/Users/hide/Projects/cordova-osx/cordova-plugman/node_modules/cordova-lib -> /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/cordova-lib -> /Users/hide/Projects/cordova-osx/cordova-lib/cordova-lib
~~~

- install

~~~bash
$ npm install

npm WARN package.json plugman@1.0.3-dev No license field.
npm WARN prefer global jasmine-node@1.14.5 should be installed with -g
npm WARN prefer global jshint@2.5.8 should be installed with -g
npm WARN engineStrict Per-package engineStrict (found in this package's package.json)
npm WARN engineStrict won't be used in npm 3+. Use the config setting `engine-strict` instead.
q@1.0.1 node_modules/q

nopt@1.0.9 node_modules/nopt
└── abbrev@1.0.7

jasmine-node@1.14.5 node_modules/jasmine-node
├── mkdirp@0.3.5
├── underscore@1.8.3
├── walkdir@0.0.10
├── coffee-script@1.10.0
├── jasmine-growl-reporter@0.0.3 (growl@1.7.0)
├── requirejs@2.1.20
├── jasmine-reporters@1.0.2
└── gaze@0.3.4 (minimatch@0.2.14, fileset@0.1.8)

jshint@2.5.8 node_modules/jshint
├── strip-json-comments@1.0.4
├── underscore@1.6.0
├── exit@0.1.2
├── shelljs@0.3.0
├── console-browserify@1.1.0 (date-now@0.1.4)
├── minimatch@1.0.0 (sigmund@1.0.1, lru-cache@2.7.0)
├── cli@0.6.6 (glob@3.2.11)
└── htmlparser2@3.8.3 (domelementtype@1.3.0, entities@1.0.0, domhandler@2.3.0, readable-stream@1.1.13, domutils@1.5.1)

~~~

## cordova-osx: hello - HelloWorld

~~~bash
$ ls
cordova-cli     cordova-lib     cordova-plugman
~~~

~~~bash
$ cordova-cli/bin/cordova --help
Synopsis

    cordova command [options]

Global Commands

    create ............................. Create a project
    help ............................... Get help for a command

Project Commands

    info ............................... Generate project information
    requirements ....................... Checks and print out all the requirements
                                            for platforms specified

    platform ........................... Manage project platforms
    plugin ............................. Manage project plugins

    prepare ............................ Copy files into platform(s) for building
    compile ............................ Build platform(s)
    clean .............................. Cleanup project from build artifacts

    run ................................ Run project
                                            (including prepare && compile)
    serve .............................. Run project with a local webserver
                                            (including prepare)

aliases:
    build -> cordova prepare && cordova compile
    emulate -> cordova run --emulator

Command-line Flags/Options

    -v, --version ...................... prints out this utility's version
    -d, --verbose ...................... debug mode produces verbose log output for all activity,
                                         including output of sub-commands cordova invokes
    --no-update-notifier ............... disables check for CLI updates
~~~

- cordova-osx

~~~bash
$ git clone https://github.com/apache/cordova-osx.git
~~~

- プロジェクト作成

~~~bash
$ cordova-cli/bin/cordova create hello com.example.hello HelloWorld

LOG  : Creating a new cordova project.
~~~

~~~bash
$ tree hello/

hello/
├── config.xml
├── hooks
│   └── README.md
├── platforms
├── plugins
└── www
    ├── css
    │   └── index.css
    ├── img
    │   └── logo.png
    ├── index.html
    └── js
        └── index.js

7 directories, 6 files
~~~

- cordova-osx をプラットフォーム追加

~~~bash
$ cd hello/

$ ../cordova-cli/bin/cordova platform add ../cordova-osx
LOG  : Adding osx project...
LOG  : Running command: /Users/hide/Projects/cordova-osx/cordova-osx/bin/create /Users/hide/Projects/cordova-osx/hello/platforms/osx com.example.hello HelloWorld
OS X project created with cordova-osx@4.0.0-dev
LOG  : Discovered plugin "cordova-plugin-whitelist" in config.xml. Installing to the project
LOG  : Fetching plugin "cordova-plugin-whitelist@1" via npm
LOG  : Installing "cordova-plugin-whitelist" for osx
~~~

- ビルド & ラン

~~~bash
$ ../cordova-cli/bin/cordova run osx
LOG  : Running command: /Users/hide/Projects/cordova-osx/hello/platforms/osx/cordova/run
Building project  : /Users/hide/Projects/cordova-osx/hello/platforms/osx/HelloWorld.xcodeproj
        Configuration : Debug


Agreeing to the Xcode/iOS license requires admin privileges, please re-run as root via sudo.


Error code 69 for command: xcodebuild with args: -xcconfig,/Users/hide/Projects/cordova-osx/hello/platforms/osx/cordova/build-debug.xcconfig,-project,HelloWorld.xcodeproj,-target,HelloWorld,-configuration,Debug,build,CONFIGURATION_BUILD_DIR=/Users/hide/Projects/cordova-osx/hello/platforms/osx/build,SHARED_PRECOMPS_DIR=/Users/hide/Projects/cordova-osx/hello/platforms/osx/build/sharedpch
LOG  : ERROR running one or more of the platforms: Error: /Users/hide/Projects/cordova-osx/hello/platforms/osx/cordova/run: Command failed with exit code 2
You may not have the required environment or OS to run this project
~~~

- ライセンスに同意するために初回はsudo

~~~bash
$ sudo ../cordova-cli/bin/cordova run osx
~~~

- ファイルがいろいろできている

~~~bash
$ tree -d .

.
├── hooks
├── platforms
│   └── osx
│       ├── CordovaLib
│       │   ├── CordovaLib
│       │   │   └── Classes
│       │   │       ├── Commands
│       │   │       └── Utils
│       │   ├── CordovaLib.xcodeproj
│       │   └── build
│       │       └── CordovaLib.build
│       │           └── Debug
│       │               └── Cordova.build
│       │                   └── Objects-normal
│       │                       └── x86_64
│       ├── HelloWorld
│       │   ├── Classes
│       │   ├── Images.xcassets
│       │   │   └── AppIcon.appiconset
│       │   ├── Plugins
│       │   └── en.lproj
│       ├── HelloWorld.xcodeproj
│       ├── build
│       │   ├── HelloWorld.app
│       │   │   └── Contents
│       │   │       ├── MacOS
│       │   │       └── Resources
│       │   │           ├── en.lproj
│       │   │           └── www
│       │   │               ├── cordova-js-src
│       │   │               │   └── plugin
│       │   │               │       └── osx
│       │   │               ├── css
│       │   │               ├── img
│       │   │               └── js
│       │   ├── HelloWorld.build
│       │   │   └── Debug
│       │   │       └── HelloWorld.build
│       │   │           └── Objects-normal
│       │   │               └── x86_64
│       │   ├── include
│       │   │   └── Cordova
│       │   │       └── Private
│       │   └── sharedpch [error opening dir]
│       ├── cordova
│       │   ├── lib
│       │   └── node_modules
│       │       ├── glob
│       │       │   └── node_modules
│       │       │       ├── inflight
│       │       │       │   └── node_modules
│       │       │       │       └── wrappy
│       │       │       │           └── test
│       │       │       ├── inherits
│       │       │       ├── minimatch
│       │       │       │   └── node_modules
│       │       │       │       └── brace-expansion
│       │       │       │           ├── node_modules
│       │       │       │           │   ├── balanced-match
│       │       │       │           │   │   └── test
│       │       │       │           │   └── concat-map
│       │       │       │           │       ├── example
│       │       │       │           │       └── test
│       │       │       │           └── test
│       │       │       ├── once
│       │       │       │   ├── node_modules
│       │       │       │   │   └── wrappy
│       │       │       │   │       └── test
│       │       │       │   └── test
│       │       │       └── path-is-absolute
│       │       ├── nopt
│       │       │   ├── lib
│       │       │   └── node_modules
│       │       │       └── abbrev
│       │       ├── q
│       │       └── shelljs
│       ├── platform_www
│       │   └── cordova-js-src
│       │       └── plugin
│       │           └── osx
│       └── www
│           ├── cordova-js-src
│           │   └── plugin
│           │       └── osx
│           ├── css
│           ├── img
│           └── js
├── plugins
│   └── cordova-plugin-whitelist
│       ├── doc
│       │   ├── de
│       │   ├── es
│       │   ├── fr
│       │   ├── it
│       │   ├── ja
│       │   ├── ko
│       │   ├── pl
│       │   └── zh
│       └── src
│           ├── android
│           └── ios
└── www
    ├── css
    ├── img
    └── js

105 directories
~~~

- 再配布フォルダー

~~~bash
$ open platforms/osx/build/HelloWorld.app
~~~

- 所有権を自分に再変更しておく

~~~bash
$ sudo chown -R hide:staff ~/.config
$ sudo chown -R hide:staff .
~~~

- XCode でひらく

~~~bash
$ find . -name "*.xcodeproj" -print
./platforms/osx/CordovaLib/CordovaLib.xcodeproj
./platforms/osx/HelloWorld.xcodeproj
~~~

- プラグイン(file-plugin)追加

~~~bash
$../cordova-cli/bin/cordova plugin add https://github.com/apache/cordova-plugin-file.git

LOG  : Fetching plugin "https://github.com/apache/cordova-plugin-file.git" via git clone
LOG  : Repository "https://github.com/apache/cordova-plugin-file.git" checked out to git ref "master".
LOG  : Installing "cordova-plugin-file" for osx

The Android Persistent storage location now defaults to "Internal". Please check this plugins README to see if you application needs any changes in its config.xml.

If this is a new application no changes are required.

If this is an update to an existing application that did not specify an "AndroidPersistentFileLocation" you may need to add:

     "<preference name="AndroidPersistentFileLocation" value="Compatibility" />"

to config.xml in order for the application to find previously stored files.
~~~
