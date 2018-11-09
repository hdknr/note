
- [HelloElectron.app for OSX](http://qiita.com/hidelafoglia/items/5279f4f60a2f6d762f99)

## nodejs インストール

- 管理者としてコンソールを開く

~~~
C:\WINDOWS\system32>choco install nodejs
Chocolatey v0.9.9.2
Installing the following packages:
nodejs
By installing you accept licenses for the packages.

nodejs v0.12.4
 Found 'chocolateyInstall.ps1':

#Install-VirtualPackage 'nodejs.commandline' 'nodejs.install'



Do you want to run the script?
 NOTE: If you choose not to run the script, the installation will
 fail.
 Skip is an advanced option and most likely will never be wanted.

 1) yes
 2) no [Default - Press Enter]
 3) skip
3
 nodejs has been installed successfully.

Chocolatey installed 1/1 package(s). 0 package(s) failed.
 See the log for details.
 ~~~

### node のパス

 ~~~

C:\Users\hdknr\Documents>SET PATH=%PATH%;%PROGRAMFILES%\nodejs
~~~

## electron インストール

~~~
C:\Users\hdknr\Documents>npm -g install electron-prebuilt
~~~

~~~

C:\Users\hdknr\AppData\Roaming\npm\electron -> C:\Users\hdknr\AppData\Roaming\npm\node_modules\electron-prebuilt\cli.js

> electron-prebuilt@0.27.3 postinstall C:\Users\hdknr\AppData\Roaming\npm\node_modules\electron-prebuilt
> node install.js

Downloading electron-v0.27.3-win32-x64.zip

[=================================================>] 100.0% of 47.41 MB (1.98 MB/s)
electron-prebuilt@0.27.3 C:\Users\hdknr\AppData\Roaming\npm\node_modules\electron-prebuilt
├── extract-zip@1.0.3 (debug@0.7.4, async@0.9.0, minimist@0.1.0, mkdirp@0.5.0, through2@0.6.3, yauzl@2.3.1, concat-stream@1.4.8)
└── electron-download@1.0.5 (path-exists@1.0.0, home-path@0.1.2, mkdirp@0.5.1, mv@2.0.3, nugget@1.5.2)
~~~

### npmのパス

~~~

C:\Users\hdknr\Documents>set PATH=%PATH%;%APPDATA%\npm
~~~

~~~
C:\Users\hdknr\Documents>electron --version
C:\Users\hdknr\Documents>[9704:0611/074638:INFO:CONSOLE(0)] v0.27.3
~~~

## hello

~~~
C:\Users\hdknr\Documents>mkdir proj\app

C:\Users\hdknr\Documents>cd proj\app
~~~

### init

~~~
C:\Users\hdknr\Documents\proj\app>npm init -y
Wrote to C:\Users\hdknr\Documents\proj\app\package.json:
~~~

~~~js
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
~~~

~~~
C:\Users\hdknr\Documents\proj\app>tree /F
フォルダー パスの一覧:  ボリューム Acer
ボリューム シリアル番号は 000000E6 9AAA:8637 です
C:.
    package.json

サブフォルダーは存在しません
~~~

### index.js & index.html

- [こぴぺ](http://qiita.com/hidelafoglia/items/5279f4f60a2f6d762f99)

### 起動

~~~
C:\Users\hdknr\Documents\proj\app>electron .

C:\Users\hdknr\Documents\proj\app>[8288:0611/075204:ERROR:crash_reporter_win.cc(75)] Cannot initialize out-of-process crash handler
[9312:0611/075204:INFO:renderer_main.cc(200)] Renderer process started
~~~

## 配布

### asar インストール

~~~
C:\Users\hdknr\Documents\proj\app>npm install -g asar
~~~

~~~
C:\Users\hdknr\AppData\Roaming\npm\asar -> C:\Users\hdknr\AppData\Roaming\npm\node_modules\asar\bin\asar

asar@0.7.1 C:\Users\hdknr\AppData\Roaming\npm\node_modules\asar
├── chromium-pickle-js@0.1.0
├── commander@2.3.0
├── mkdirp@0.5.1 (minimist@0.0.8)
├── cuint@0.1.5
├── minimatch@2.0.4 (brace-expansion@1.1.0)
├── glob@5.0.10 (inherits@2.0.1, path-is-absolute@1.0.0, inflight@1.0.4, once@1.3.2)
└── mksnapshot@0.1.0 (fs-extra@0.18.2, decompress-zip@0.1.0, request@2.55.0)
~~~

### アーカイブ化

- アーカイブ

~~~
C:\Users\hdknr\Documents\proj\app>asar pack . %USERPROFILE%\app.asar
~~~

- 起動

~~~
C:\Users\hdknr\Documents\proj\app>electron %USERPROFILE%\app.asar

C:\Users\hdknr\Documents\proj\app>[8096:0611/080544:INFO:renderer_main.cc(200)]　Renderer process started
~~~

## electron-packager

~~~
C:\Users\hdknr\Documents\proj\app>npm install electron-packager -g
npm WARN engine xmlbuilder@2.2.1: wanted: {"node":"0.8.x || 0.10.x"} (current: {"node":"0.12.4","npm":"2.10.1"})
C:\Users\hdknr\AppData\Roaming\npm\electron-packager -> C:\Users\hdknr\AppData\R
oaming\npm\node_modules\electron-packager\cli.js
electron-packager@4.1.2 C:\Users\hdknr\AppData\Roaming\npm\node_modules\electron-packager
├── minimist@1.1.1
├── ncp@2.0.0
├── mv@2.0.3 (ncp@0.6.0, rimraf@2.2.8)
├── mkdirp@0.5.1 (minimist@0.0.8)
├── rimraf@2.4.0 (glob@4.5.3)
├── asar@0.6.1 (commander@2.3.0, chromium-pickle-js@0.1.0, glob@5.0.10, minimatch@2.0.4, cuint@0.1.5)
├── rcedit@0.3.0
├── extract-zip@1.0.3 (debug@0.7.4, minimist@0.1.0, async@0.9.0, mkdirp@0.5.0, concat-stream@1.4.10, yauzl@2.3.1, through2@0.6.3)
├── electron-download@1.0.5 (path-exists@1.0.0, home-path@0.1.2, nugget@1.5.2)
└── plist@1.1.0 (util-deprecate@1.0.0, base64-js@0.0.6, xmldom@0.1.19, xmlbuilder@2.2.1)
~~~

### HelloElectron.exe

- 作製

~~~

C:\Users\hdknr\Documents\proj\app>electron-packager ./ HelloElectron --platform=win32 --arch=x64 --version=0.25.1

Downloading electron-v0.25.1-win32-x64.zip
[=================================================>] 100.0% of 41.79 MB (245.12kB/s)
Packaging app for platform win32 x64 using electron v0.25.1
Wrote new app to C:\Users\hdknr\Documents\proj\app\HelloElectron-win32
~~~

~~~
C:\Users\hdknr\Documents\proj\app>dir .
 ドライブ C のボリューム ラベルは Acer です
 ボリューム シリアル番号は 9AAA-8637 です

 C:\Users\hdknr\Documents\proj\app のディレクトリ

2015/06/11  08:13    <DIR>          .
2015/06/11  08:13    <DIR>          ..
2015/06/11  08:13    <DIR>          HelloElectron-win32
2015/06/11  07:51               170 index.html
2015/06/11  07:51               489 index.js
2015/06/11  07:48               217 package.json
~~~

- 起動（エクスプローラでダブクリ)

~~~
C:\Users\hdknr\Documents\proj\app>HelloElectron-win32\HelloElectron.exe

C:\Users\hdknr\Documents\proj\app>[9820:0611/081626:ERROR:crash_reporter_win.cc(70)] Cannot initialize out-of-process crash handler
[5048:0611/081626:INFO:renderer_main.cc(200)] Renderer process started
~~~
