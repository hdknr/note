electron: HelloElectron.app 

## electron

写経元:

- [electron.atom.io](http://electron.atom.io/)
- [Electronでアプリケーションを作ってみよう](http://qiita.com/Quramy/items/a4be32769366cfe55778)
- [Electronでアプリケーションをつくる](http://tech.sanwasystem.com/entry/2015/05/29/225731)
- [electron-packager](https://www.npmjs.com/package/electron-packager)

## install

~~~
$ npm -g install electron-prebuilt

/usr/local/bin/electron -> /usr/local/lib/node_modules/electron-prebuilt/cli.js

> electron-prebuilt@0.27.2 postinstall /usr/local/lib/node_modules/electron-prebuilt
> node install.js

Downloading electron-v0.27.2-darwin-x64.zip
[=================================================>] 100.0% of 36.8 MB (2.83 MB/s)
electron-prebuilt@0.27.2 /usr/local/lib/node_modules/electron-prebuilt
├── extract-zip@1.0.3 (debug@0.7.4, minimist@0.1.0, async@0.9.0, yauzl@2.3.1, mkdirp@0.5.0, concat-stream@1.4.8, through2@0.6.3)
└── electron-download@1.0.5 (path-exists@1.0.0, home-path@0.1.2, mkdirp@0.5.1, mv@2.0.3, nugget@1.5.2)
~~~

## hello

~~~
$ mkdir app;cd app
~~~

### init

~~~
$ npm init -y
author: hdknr.com
Wrote to /Users/hide/Documents/Projects/app/package.json:

{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "hdknr.com",
  "license": "ISC"
}
~~~

~~~
$ tree .
.
└── package.json

0 directories, 1 file
~~~

### index.js

~~~
$ vi index.js
~~~

~~~js
'use strict';

var app = require('app');
var BrowserWindow = require('browser-window');

require('crash-reporter').start();

var mainWindow = null;

app.on('window-all-closed', function() {
  if (process.platform != 'darwin')
    app.quit();
});

app.on('ready', function() {
  mainWindow = new BrowserWindow({width: 800, height: 600});
  mainWindow.loadUrl('file://' + __dirname + '/index.html');
  mainWindow.on('closed', function() {
    mainWindow = null;
  });
});
~~~

### index.html

~~~
$ vi index.html
~~~

~~~html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Electron Read Us</title>
  </head>
  <body>
    <h1>Hello, electron!</h1>
  </body>
</html>
~~~

### 起動

~~~
$ electron .
~~~

~~~
[55465:0609/210710:INFO:renderer_main.cc(200)] Renderer process started
[55465:0609/210715:WARNING:channel.cc(549)] Failed to send message to ack remove remote endpoint (local ID 2147483648, remote ID 2)
~~~

## 配布

### asar インストール

~~~
$ npm install -g asar
~~~

~~~
/usr/local/bin/asar -> /usr/local/lib/node_modules/asar/bin/asar
asar@0.7.1 /usr/local/lib/node_modules/asar
├── chromium-pickle-js@0.1.0
├── commander@2.3.0
├── cuint@0.1.5
├── mkdirp@0.5.1 (minimist@0.0.8)
├── minimatch@2.0.4 (brace-expansion@1.1.0)
├── glob@5.0.10 (path-is-absolute@1.0.0, inherits@2.0.1, inflight@1.0.4, once@1.3.2)
└── mksnapshot@0.1.0 (fs-extra@0.18.2, request@2.55.0, decompress-zip@0.1.0)
~~~

#### アーカイブ化

- アーカイブ

~~~
$ asar pack . ~/Downloads/app.asar
~~~

~~~
$ file ~/Downloads/app.asar 
/Users/hide/Downloads/app.asar: X11 SNF font data, LSB first
~~~

- 起動

~~~
$ electron ~/Downloads/app.asar 
[55810:0609/212530:INFO:renderer_main.cc(200)] Renderer process started
[55810:0609/212533:WARNING:raw_channel_posix.cc(283)] sendmsg/write/writev: Socket is not connected
[55810:0609/212533:WARNING:channel.cc(549)] Failed to send message to ack remove remote endpoint (local ID 1, remote ID 1)
[55810:0609/212533:WARNING:channel.cc(549)] Failed to send message to ack remove remote endpoint (local ID 2147483648, remote ID 2)
~~~

### electron-packager 

~~~
$ npm i electron-packager -g
npm WARN engine xmlbuilder@2.2.1: wanted: {"node":"0.8.x || 0.10.x"} (current: {"node":"0.12.0","npm":"2.5.1"})
/usr/local/bin/electron-packager -> /usr/local/lib/node_modules/electron-packager/cli.js
electron-packager@4.1.2 /usr/local/lib/node_modules/electron-packager
├── rcedit@0.3.0
├── minimist@1.1.1
├── ncp@2.0.0
├── mv@2.0.3 (rimraf@2.2.8, ncp@0.6.0)
├── mkdirp@0.5.1 (minimist@0.0.8)
├── asar@0.6.1 (chromium-pickle-js@0.1.0, commander@2.3.0, glob@5.0.10, cuint@0.1.5, minimatch@2.0.4)
├── rimraf@2.4.0 (glob@4.5.3)
├── extract-zip@1.0.3 (debug@0.7.4, minimist@0.1.0, async@0.9.0, mkdirp@0.5.0, yauzl@2.3.1, through2@0.6.3, concat-stream@1.4.8)
├── plist@1.1.0 (util-deprecate@1.0.0, base64-js@0.0.6, xmldom@0.1.19, xmlbuilder@2.2.1)
└── electron-download@1.0.5 (path-exists@1.0.0, home-path@0.1.2, nugget@1.5.2)


~~~

#### HelloElectron.app

- 作成

~~~
$ electron-packager ./ HelloElectron --platform=darwin --arch=x64 --version=0.25.1

Downloading electron-v0.25.1-darwin-x64.zip
[=================================================>] 100.0% of 36.84 MB (2.63 MB/s)
Packaging app for platform darwin x64 using electron v0.25.1
Wrote new app to /Users/hide/Documents/Projects/app/HelloElectron.app
~~~

~~~
$ ls -l
total 24
drwxr-xr-x  3 hide  staff  102  6  9 21:32 HelloElectron.app
-rw-r--r--+ 1 hide  staff  162  6  9 21:09 index.html
-rw-r--r--+ 1 hide  staff  470  6  9 21:06 index.js
-rw-r--r--+ 1 hide  staff  226  6  9 21:05 package.json
~~~



- 起動 (ダブクリ)

~~~
$ open HelloElectron.app
~~~
