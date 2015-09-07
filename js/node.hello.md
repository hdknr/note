# Hello

~~~bash
$ mkdir hello && cd hello
~~~

~~~bash
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg> --save` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
name: (hello)
version: (1.0.0)
description: hello
entry point: (index.js)
test command:
git repository: https://github.com/hdknr/hello.git
keywords: hello
author: hdknr.com
license: (ISC)
About to write to /Users/hide/Dropbox/アプリ/scriptogram/hello/package.json:

{
  "name": "hello",
  "version": "1.0.0",
  "description": "hello",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/hdknr/hello.git"
  },
  "keywords": [
    "hello"
  ],
  "author": "hdknr.com",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/hdknr/hello/issues"
  },
  "homepage": "https://github.com/hdknr/hello#readme"
}


Is this ok? (yes)
~~~

~~~bash
$ tree .
.
└── package.json

0 directories, 1 file
~~~

~~~bash
$ cat package.json
{
  "name": "hello",
  "version": "1.0.0",
  "description": "hello",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/hdknr/hello.git"
  },
  "keywords": [
    "hello"
  ],
  "author": "hdknr.com",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/hdknr/hello/issues"
  },
  "homepage": "https://github.com/hdknr/hello#readme"
}
~~~

~~~bash
$ npm install keypair -S
npm WARN package.json hello@1.0.0 No README data
keypair@1.0.0 node_modules/keypair
~~~

~~~bash
$ tree .
.
├── node_modules
│   └── keypair
│       ├── LICENSE
│       ├── README.md
│       ├── example.js
│       ├── index.js
│       ├── package.json
│       └── test.js
└── package.json

2 directories, 7 files
~~~~

~~~bash
$ jq ".dependencies" package.json
{
  "keypair": "^1.0.0"
}
~~~

- 名前でrequire すると node_modues からロードしてくれる

~~~bash
$ node
> var keypair = require('keypair');
undefined
> keypair()
{ public: '-----BEGIN RSA PUBLIC KEY-.......'}
~~~

- グローバルインストール

~~~bash
$ npm install request -S -g
request@2.61.0 /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/request
├── forever-agent@0.6.1
├── aws-sign2@0.5.0
├── stringstream@0.0.4
├── oauth-sign@0.8.0
├── caseless@0.11.0
├── tunnel-agent@0.4.1
├── isstream@0.1.2
├── json-stringify-safe@5.0.1
├── extend@3.0.0
├── node-uuid@1.4.3
├── qs@4.0.0
├── form-data@1.0.0-rc3 (async@1.4.2)
├── tough-cookie@2.0.0
├── http-signature@0.11.0 (assert-plus@0.1.5, asn1@0.1.11, ctype@0.5.3)
├── mime-types@2.1.5 (mime-db@1.17.0)
├── hawk@3.1.0 (cryptiles@2.0.4, sntp@1.0.9, boom@2.8.0, hoek@2.14.0)
├── combined-stream@1.0.5 (delayed-stream@1.0.0)
├── bl@1.0.0 (readable-stream@2.0.2)
└── har-validator@1.8.0 (commander@2.8.1, bluebird@2.9.34, is-my-json-valid@2.12.1, chalk@1.1.1)
~~~

~~~bash
$ tree -d
.
└── node_modules
    └── keypair

2 directories
~~~

~~~js
> var request = require('request');
> request('http://www.google.com', function(err, res, body){
    console.log(res.statusCode);
    console.log(body.length);
  });
> 200
52837

undefined  
~~~

~~~bash
$ npm install soupselect -S -g
soupselect@0.2.0 /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/soupselect
├── htmlparser@1.7.7
└── nodeunit@0.9.1 (tap@0.7.1)

$ npm install htmlparser -S -g
htmlparser@1.7.7 /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/htmlparser
~~~

~~~bash
$ atom index.js
~~~
~~~js
var request = require('request');
var select = require('soupselect').select;
var htmlparser = require("htmlparser");

var handler = new htmlparser.DefaultHandler(function (error, dom) { });
var parser = new htmlparser.Parser(handler);

var request = require('request');
request('https://twitter.com', function(err, res, body){
    parser.parseComplete(body);
    console.log(select(handler.dom, "title")[0].children[0].data);
});
~~~

~~~bash
$ node index.js
Twitter
~~~
