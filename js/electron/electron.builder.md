# electron-builder

~~~bash 
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (helloel) 
version: (1.0.0) 
description: hello electron
entry point: (index.js) 
test command: 
git repository: 
keywords: 
author: hdknr.com
license: (ISC) 
About to write to /Users/hide/Documents/Boxes/ubn1804/projects/helloel/package.json:

{
  "name": "helloel",
  "version": "1.0.0",
  "description": "hello electron",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "hdknr.com",
  "license": "ISC"
}

Is this OK? (yes) yes
~~~

~~~bash
$ npm install electron electron-builder

> electron@3.0.8 postinstall /Users/hide/Documents/Boxes/ubn1804/projects/helloel/node_modules/electron
> node install.js

Downloading tmp-24599-1-SHASUMS256.txt-3.0.8
[============================================>] 100.0% of 4.74 kB (4.74 kB/s)
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN helloel@1.0.0 No repository field.

+ electron@3.0.8
+ electron-builder@20.33.2
added 313 packages from 216 contributors in 72.314s
[+] no known vulnerabilities found [1135 packages audited]
~~~

~~~bash 
$ ./node_modules/.bin/build --help
build

Build

コマンド:
  build build                    Build                              [デフォルト]
  build install-app-deps         Install app deps
  build node-gyp-rebuild         Rebuild own native code
  build create-self-signed-cert  Create self-signed code signing cert for
                                 Windows apps
  build start                    Run application in a development mode using
                                 electron-webpack

Building:
  --mac, -m, -o, --macos   Build for macOS, accepts target list (see
                           https://goo.gl/5uHuzj).                        [配列]
  --linux, -l              Build for Linux, accepts target list (see
                           https://goo.gl/4vwQad)                         [配列]
  --win, -w, --windows     Build for Windows, accepts target list (see
                           https://goo.gl/jYsTEJ)                         [配列]
  --x64                    Build for x64                                  [真偽]
  --ia32                   Build for ia32                                 [真偽]
  --armv7l                 Build for armv7l                               [真偽]
  --arm64                  Build for arm64                                [真偽]
  --dir                    Build unpacked dir. Useful to test.            [真偽]
  --prepackaged, --pd      The path to prepackaged app (to pack in a
                           distributable format)
  --projectDir, --project  The path to project directory. Defaults to current
                           working directory.
  --config, -c             The path to an electron-builder config. Defaults to
                           `electron-builder.yml` (or `json`, or `json5`), see
                           https://goo.gl/YFRJOM

Publishing:
  --publish, -p  Publish artifacts, see https://goo.gl/tSFycD
       [選択してください: "onTag", "onTagOrDraft", "always", "never", undefined]

Deprecated:
  --draft       Please set releaseType in the GitHub publish options instead
                                                                          [真偽]
  --prerelease  Please set releaseType in the GitHub publish options instead
                                                                          [真偽]
  --platform    The target platform (preferred to use --mac, --win or --linux)
  [選択してください: "mac", "win", "linux", "darwin", "win32", "all", undefined]
  --arch        The target arch (preferred to use --x64 or --ia32)
          [選択してください: "ia32", "x64", "armv7l", "arm64", "all", undefined]

Other:
  --help     ヘルプを表示                                                 [真偽]
  --version  バージョンを表示                                             [真偽]

例:
  electron-builder -mwl                     build for macOS, Windows and Linux
  electron-builder --linux deb tar.xz       build deb and tar.xz for Linux
  electron-builder --win --ia32             build for Windows ia32
  electron-builder                          set package.json property `foo` to
  -c.extraMetadata.foo=bar                  `bar`
  electron-builder                          configure unicode options for NSIS
  --config.nsis.unicode=false

See https://electron.build for more documentation.
~~~

~~~bash 
$ ./node_modules/.bin/build 
  • electron-builder version=20.33.2

Package "electron" is only allowed in "devDependencies". Please remove it from the "dependencies" section in your package.json.
Package "electron-builder" is only allowed in "devDependencies". Please remove it from the "dependencies" section in your package.json.
~~~

~~~bash 
$ tree app/
app/
├── main.html
└── main.js
~~~

app/main.js:

~~~js
const {
  app,
  BrowserWindow
} = require('electron');

let win;

function createWindow() {
  win = new BrowserWindow({
    width: 800,
    height: 600
  })

  win.loadFile('app/main.html')

  win.webContents.openDevTools();   // Chrome Developer Tools

  win.on('closed', () => {
    win = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})
~~~

~~~html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <title>helloel</title>
</head>

<body>
  <h1>helloel</h1>
  <script>
    document.write(process.versions.node)
  </script>,
  <script>
    document.write(process.versions.chrome)
  </script>,
  <script>
    document.write(process.versions.electron)
  </script>.
</body>

</html>
~~~

package.json:

~~~js
{
  "name": "helloel",
  "version": "1.0.0",
  "description": "hello electron",
  "main": "app/main.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "hdknr.com",
  "license": "ISC",
  "dependencies": {},
  "devDependencies": {
    "electron": "^3.0.8",
    "electron-builder": "^20.33.2"
  }
}
~~~

~~~bash
$ npx electron .

/Library/Caches/com.apple.xbs/Sources/AppleGVA/AppleGVA-10.1.17/Sources/Slices/Driver/AVD_loader.cpp: failed to get a service for display 3 
2018-11-09 15:19:22.338 Electron Helper[25782:1421305] Couldn't set selectedTextBackgroundColor from default ()
~~~

~~~bash 
$ ./node_modules/.bin/build
  • electron-builder version=20.33.2
  • writing effective config file=dist/builder-effective-config.yaml
  • no native production dependencies
  • packaging       platform=darwin arch=x64 electron=3.0.8 appOutDir=dist/mac
  • default Electron icon is used reason=application icon is not set
  • signing         file=dist/mac/helloel.app identityName=Developer ID Application: Lafoglia.Co.,LTD. (5UZR37U96S) identityHash=B4FBD8F7D7EFA169F1042242A97127F7141257F0 provisioningProfile=none
  • building        target=macOS zip arch=x64 file=dist/helloel-1.0.0-mac.zip
  • building        target=DMG arch=x64 file=dist/helloel-1.0.0.dmg
  • building block map blockMapFile=dist/helloel-1.0.0.dmg.blockmap
  • building embedded block map file=dist/helloel-1.0.0-mac.zip
~~~