# electron-vue

~~~bash
C:\windows\system32>npm install -g vue-cli
npm WARN deprecated coffee-script@1.12.7: CoffeeScript on NPM has moved to "coffeescript" (no hyphen)
C:\Program Files\nodejs\vue -> C:\Program Files\nodejs\node_modules\vue-cli\bin\vue
C:\Program Files\nodejs\vue-list -> C:\Program Files\nodejs\node_modules\vue-cli\bin\vue-list
C:\Program Files\nodejs\vue-init -> C:\Program Files\nodejs\node_modules\vue-cli\bin\vue-init
+ vue-cli@2.9.6
added 237 packages from 206 contributors in 21.978s
~~~

~~~bash
C:\Users\spin\Documents\Projects>vue init simulatedgreg/electron-vue hellovue

? Target directory exists. Continue? Yes
? Application Name hellovue
? Application Id jp.lafoglia.hellovue
? Application Version 0.0.1
? Project description An electron-vue project
? Use Sass / Scss? Yes
? Select which Vue plugins to install axios, vue-electron, vue-router, vuex, vuex-electron
? Use linting with ESLint? Yes
? Which ESLint config would you like to use? Standard
? Set up unit testing with Karma + Mocha? Yes
? Set up end-to-end testing with Spectron + Mocha? Yes
? What build tool would you like to use? builder

   vue-cli · Generated "hellovue".
warning Failed to append commit SHA on README.md
~~~

~~~bash
C:\Users\spin\Documents\Projects\hellovue>npm install
npm WARN deprecated babel-preset-babili@0.1.4: babili has been renamed to babel-minify. Please update to babel-preset-minify
npm WARN deprecated circular-json@0.5.9: CircularJSON is in maintenance only, flatted is its successor.
npm WARN deprecated nodemailer@2.7.2: All versions below 4.0.1 of Nodemailer are deprecated. See https://nodemailer.com/status/
npm WARN deprecated browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
npm WARN deprecated circular-json@0.3.3: CircularJSON is in maintenance only, flatted is its successor.
npm WARN deprecated uws@9.14.0: stop using this version
npm WARN deprecated mailcomposer@4.0.1: This project is unmaintained
npm WARN deprecated socks@1.1.9: If using 2.x branch, please upgrade to at least 2.1.6 to avoid a serious bug with socket data flow and an import issue introduced in 2.1.0
npm WARN deprecated node-uuid@1.4.8: Use uuid module instead
npm WARN deprecated buildmail@4.0.1: This project is unmaintained
npm WARN deprecated boom@2.10.1: This version is no longer maintained. Please upgrade to the latest version.
npm WARN deprecated cryptiles@2.0.5: This version is no longer maintained. Please upgrade to the latest version.
npm WARN deprecated hoek@2.16.3: This version is no longer maintained. Please upgrade to the latest version.

> uws@9.14.0 install C:\Users\spin\Documents\Projects\hellovue\node_modules\uws
> node-gyp rebuild > build_log.txt 2>&1 || exit 0


> electron-chromedriver@1.8.0 install C:\Users\spin\Documents\Projects\hellovue\node_modules\electron-chromedriver
> node ./download-chromedriver.js

successfully dowloaded and extracted!
~~~

~~~bash
C:\Users\spin\Documents\Projects\hellovue>npm audit fix --force
npm WARN using --force I sure hope you know what you are doing.
npm WARN deprecated circular-json@0.5.9: CircularJSON is in maintenance only, flatted is its successor.

> fsevents@1.2.4 install C:\Users\spin\Documents\Projects\hellovue\node_modules\fsevents
> node install

npm WARN karma-webpack@3.0.5 requires a peer of webpack@^2.0.0 || ^3.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN hellovue@0.0.1 No repository field.
npm WARN hellovue@0.0.1 No license field.

+ karma@3.1.1
added 68 packages from 27 contributors, removed 103 packages and updated 7 packages in 11.473s
fixed 6 of 6 vulnerabilities in 18849 scanned packages
  1 package update for 6 vulns involved breaking changes
  (installed due to `--force` option)
~~~

~~~bash
C:\Users\spin\Documents\Projects\hellovue>npm audit

                       === npm audit security report ===

found 0 vulnerabilities
 in 18420 scanned packages
~~~

~~~bash
C:\Users\spin\Documents\Projects\hellovue>npm run dev

> hellovue@0.0.1 dev C:\Users\spin\Documents\Projects\hellovue
> node .electron-vue/dev-runner.js

         ___                      __
   __   /\_ \       __     ___   /\ \__    _ __    ___     ___              __  __  __  __     __
 / ,.`\ \//\ \    / ,.`\  /'___\ \ \ ,_\  /\` __\ / __`\ /' _ `\   _______ /\ \/\ \/\ \/\ \  / ,.`\
/\  __/   \_\ \_ /\  __/ /\ \__/  \ \ \/  \ \ \/ /\ \_\ \/\ \/\ \ /\______\\ \ \/ |\ \ \_\ \/\  __/
\ \____\  /\____\\ \____\\ \____\  \ \ \_  \ \_\ \ \____/\ \_\ \_\\/______/ \ \___/ \ \____/\ \____\
 \/____/  \/____/ \/____/ \/____/   \ \__\  \/_/  \/___/  \/_/\/_/           \/__/   \/___/  \/____/
                                     \/__/
  getting ready...

┏ Main Process ---------------

  compiling...

┗ ----------------------------

┏ Renderer Process -----------

  Hash: a569c69f8145c37dfbaa
  Version: webpack 4.25.1
  Time: 2014ms
  Built at: 2018-11-16 16:15:24
                  Asset       Size    Chunks             Chunk Names
  imgs/logo--assets.png   60.4 KiB            [emitted]
             index.html  428 bytes            [emitted]
            renderer.js   1.15 MiB  renderer  [emitted]  renderer
  Entrypoint renderer = renderer.js
  [0] multi ./.electron-vue/dev-client ./src/renderer/main.js 40 bytes {renderer} [built]
  [./.electron-vue/dev-client.js] 731 bytes {renderer} [built]
  [./node_modules/strip-ansi/index.js] 161 bytes {renderer} [built]
  [./node_modules/vue-hot-reload-api/dist/index.js] 6.13 KiB {renderer} [built]
  [./node_modules/vue-loader/lib/runtime/componentNormalizer.js] 2.63 KiB {renderer} [built]
  [./node_modules/vue/dist/vue.esm.js] 286 KiB {renderer} [built]
  [./node_modules/webpack-hot-middleware/client-overlay.js] (webpack)-hot-middleware/client-overlay.js 2.16 KiB {renderer} [built]
  [./node_modules/webpack-hot-middleware/client.js?noInfo=true&reload=true] (webpack)-hot-middleware/client.js?noInfo=true&reload=true 7.59 KiB {renderer} [built]
  [./node_modules/webpack-hot-middleware/process-update.js] (webpack)-hot-middleware/process-update.js 4.26 KiB {renderer} [built]
  [./src/renderer/App.vue] 1.12 KiB {renderer} [built]
  [./src/renderer/main.js] 382 bytes {renderer} [built]
  [./src/renderer/router/index.js] 264 bytes {renderer} [built]
  [./src/renderer/store/index.js] 342 bytes {renderer} [built]
  [axios] external "axios" 42 bytes {renderer} [built]
  [vue-electron] external "vue-electron" 42 bytes {renderer} [built]
      + 43 hidden modules
  Child html-webpack-plugin for "index.html":
           Asset      Size  Chunks  Chunk Names
      index.html  1.38 MiB       0
      Entrypoint undefined = index.html
      [./node_modules/html-webpack-plugin/lib/loader.js!./src/index.ejs] 1.15 KiB {0} [built]
      [./node_modules/lodash/lodash.js] 527 KiB {0} [built]
      [./node_modules/webpack/buildin/module.js] (webpack)/buildin/module.js 497 bytes {0} [built]

┗ ----------------------------

┏ Main Process ---------------

  Hash: 57cab86885e64a43d3aa
  Version: webpack 4.25.1
  Time: 2311ms
  Built at: 2018-11-16 16:15:24
    Asset     Size  Chunks             Chunk Names
  main.js  211 KiB    main  [emitted]  main
  Entrypoint main = main.js
  [0] multi ./src/main/index.dev.js ./src/main/index.js 40 bytes {main} [built]
  [./node_modules/cross-unzip/index.js] 1.49 KiB {main} [built]
  [./node_modules/electron-debug sync recursive] ./node_modules/electron-debug sync 160 bytes {main} [built]
  [./node_modules/electron-debug/index.js] 2.46 KiB {main} [built]
  [./node_modules/electron-devtools-installer/dist/downloadChromeExtension.js] 2.26 KiB {main} [built]
  [./node_modules/electron-devtools-installer/dist/index.js] 5.02 KiB {main} [built]
  [./node_modules/electron-devtools-installer/dist/utils.js] 1.88 KiB {main} [built]
  [./node_modules/electron-is-dev/index.js] 256 bytes {main} [built]
  [./node_modules/electron-localshortcut/index.js] 8.16 KiB {main} [built]
  [./node_modules/semver/semver.js] 37.1 KiB {main} [built]
  [./src/main/index.dev.js] 364 bytes {main} [built]
  [./src/main/index.js] 801 bytes {main} [built]
  [electron] external "electron" 42 bytes {main} [built]
  [fs] external "fs" 42 bytes {main} [built]
  [path] external "path" 42 bytes {main} [built]
      + 33 hidden modules

  WARNING in ./node_modules/electron-debug/index.js 81:45-58
  Critical dependency: the request of a dependency is an expression
   @ ./src/main/index.dev.js
   @ multi ./src/main/index.dev.js ./src/main/index.js

  WARNING in ./node_modules/electron-debug/index.js 84:85-106
  Critical dependency: the request of a dependency is an expression
   @ ./src/main/index.dev.js
   @ multi ./src/main/index.dev.js ./src/main/index.js

┗ ----------------------------

┏ Electron -------------------

  Debugger listening on ws://127.0.0.1:5858/ba2d6780-043a-4fe3-9
┗ ----------------------------

┏ Electron -------------------

  ab8-9cf7f6e41851
  For help see https://nodejs.org/en/docs/inspector

┗ ----------------------------

┏ Electron -------------------

  [2948:1116/161525.796:ERROR:CONSOLE(7574)] "Extension server error: Operation failed: : has no execution context", source: chrome-devtools://devtools/bundled/inspector.js (7574)

┗ ----------------------------
~~~

~~~bash

C:\Users\spin\Documents\Projects\hellovue>npm run build

> hellovue@0.0.1 build C:\Users\spin\Documents\Projects\hellovue
> node .electron-vue/build.js && electron-builder

 ___              __                        __                       ___       __
/\_ \       __   /\ \__     ____           /\ \       __  __   __   /\_ \     /\ \
\//\ \    / ,.`\ \ \ ,_\   / ,__\  _______ \ \ \____ /\ \/\ \ /\_\  \//\ \    \_\ \
  \_\ \_ /\  __/  \ \ \/  /\__, `\/\______\ \ \  ,. \\ \ \_\ \\/\ \   \_\ \_ /\ ,. \
  /\____\\ \____\  \ \ \_ \/\____/\/______/  \ \____/ \ \____/ \ \ \  /\____\\ \____\
  \/____/ \/____/   \ \__\ \/___/             \/___/   \/___/   \/_/  \/____/ \/___ /
                     \/__/

  - building main process
  √ building main process
  √ building renderer process


Hash: b6b40c085e80ef240e57
Version: webpack 4.25.1
Time: 1144ms
Built at: 2018-11-16 16:32:24
  Asset      Size  Chunks             Chunk Names
main.js  1.43 KiB       0  [emitted]  main
Entrypoint main = main.js
[0] external "electron" 42 bytes {0} [built]
[1] ./src/main/index.js 801 bytes {0} [built]
[2] external "path" 42 bytes {0} [built]

Hash: f7aee6437f29cb58670f
Version: webpack 4.25.1
Time: 9428ms
Built at: 2018-11-16 16:32:32
                Asset       Size  Chunks             Chunk Names
imgs/logo--assets.png   60.4 KiB          [emitted]
           index.html  313 bytes          [emitted]
          renderer.js    108 KiB       0  [emitted]  renderer
Entrypoint renderer = renderer.js
 [0] ./node_modules/vue-loader/lib/runtime/componentNormalizer.js 2.63 KiB {0} [built]
 [1] ./node_modules/vue-style-loader!./node_modules/css-loader!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/App.vue?vue&type=style&index=0&lang=css& 608 bytes {0} [built]
 [3] ./node_modules/vue-style-loader!./node_modules/css-loader!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/components/LandingPage.vue?vue&type=style&index=0&lang=css& 628 bytes {0} [built]
 [5] ./node_modules/vue-style-loader/lib/addStylesClient.js + 1 modules 6.71 KiB {0} [built]
     | ./node_modules/vue-style-loader/lib/addStylesClient.js 6.09 KiB [built]
     | ./node_modules/vue-style-loader/lib/listToStyles.js 637 bytes [built]
 [6] ./src/renderer/store/modules/index.js 238 bytes {0} [built]
 [7] external "vue-router" 42 bytes {0} [built]
 [8] external "vuex" 42 bytes {0} [built]
 [9] external "vuex-electron" 42 bytes {0} [built]
[10] external "axios" 42 bytes {0} [built]
[11] ./src/renderer/App.vue?vue&type=style&index=0&lang=css& 560 bytes {0} [built]
[18] ./src/renderer/components/LandingPage.vue?vue&type=style&index=0&lang=css& 600 bytes {0} [built]
[20] ./src/renderer/store/modules sync nonrecursive \.js$ 192 bytes {0} [built]
[22] external "vue-electron" 42 bytes {0} [built]
[23] ./src/renderer/components/LandingPage.vue + 9 modules 5.63 KiB {0} [built]
     | ./src/renderer/components/LandingPage.vue 590 bytes [built]
     | ./src/renderer/components/LandingPage.vue?vue&type=template&id=d52715ae& 215 bytes [built]
     | ./src/renderer/components/LandingPage.vue?vue&type=script&lang=js& 372 bytes [built]
     | ./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/components/LandingPage.vue?vue&type=template&id=d52715ae& 1.4 KiB [built]
     | ./node_modules/babel-loader/lib!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/components/LandingPage.vue?vue&type=script&lang=js& 269 bytes [built]
     | ./src/renderer/components/LandingPage/SystemInformation.vue 665 bytes [built]
     | ./src/renderer/components/LandingPage/SystemInformation.vue?vue&type=template&id=13129888&scoped=true& 239 bytes [built]
     | ./src/renderer/components/LandingPage/SystemInformation.vue?vue&type=script&lang=js& 396 bytes [built]
     | ./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/components/LandingPage/SystemInformation.vue?vue&type=template&id=13129888&scoped=true& 1.24 KiB [built]
     | ./node_modules/babel-loader/lib!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/components/LandingPage/SystemInformation.vue?vue&type=script&lang=js& 298 bytes [built]
[24] ./src/renderer/main.js + 8 modules 288 KiB {0} [built]
     | ./src/renderer/main.js 382 bytes [built]
     | ./node_modules/vue/dist/vue.esm.js 286 KiB [built]
     | ./src/renderer/App.vue 547 bytes [built]
     | ./src/renderer/router/index.js 264 bytes [built]
     | ./src/renderer/store/index.js 342 bytes [built]
     | ./src/renderer/App.vue?vue&type=template&id=223f658f& 201 bytes [built]
     | ./src/renderer/App.vue?vue&type=script&lang=js& 344 bytes [built]
     | ./node_modules/vue-loader/lib/loaders/templateLoader.js??vue-loader-options!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/App.vue?vue&type=template&id=223f658f& 210 bytes [built]
     | ./node_modules/babel-loader/lib!./node_modules/vue-loader/lib??vue-loader-options!./src/renderer/App.vue?vue&type=script&lang=js& 40 bytes [built]
    + 10 hidden modules
Child html-webpack-plugin for "index.html":
         Asset     Size  Chunks  Chunk Names
    index.html  556 KiB       0
    Entrypoint undefined = index.html
    [0] ./node_modules/html-webpack-plugin/lib/loader.js!./src/index.ejs 1.15 KiB {0} [built]
    [1] ./node_modules/lodash/lodash.js 527 KiB {0} [built]
    [2] (webpack)/buildin/module.js 497 bytes {0} [built]


 OKAY  take it away `electron-builder`

  • electron-builder version=20.34.0
  • loaded configuration file=package.json ("build" field)
  • writing effective config file=build\builder-effective-config.yaml
  • no native production dependencies
  • packaging       platform=win32 arch=x64 electron=2.0.13 appOutDir=build\win-unpacked
  • building        target=nsis file=build\hellovue Setup 0.0.1.exe archs=x64 oneClick=true
  • building block map blockMapFile=build\hellovue Setup 0.0.1.exe.blockmap
~~~ 

~~~bash 
C:\Users\spin\Documents\Projects\hellovue>dir build\win-unpacked\*.exe
 Volume in drive C is Windows
 Volume Serial Number is A644-721D

 Directory of C:\Users\spin\Documents\Projects\hellovue\build\win-unpacked

2018/11/16  16:32        67,813,888 hellovue.exe
               1 File(s)     67,813,888 bytes
               0 Dir(s)  453,989,588,992 bytes free
~~~