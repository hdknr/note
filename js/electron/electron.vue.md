# electron-vue

## Hello

初期化:

~~~bash
$ vue init simulatedgreg/electron-vue hellovue

? Application Name hellovue
? Application Id jp.lafoglia.hellovue
? Application Version 0.0.1
? Project description Hello Electron Vue
? Use Sass / Scss? Yes
? Select which Vue plugins to install axios, vue-electron, vue-router, vuex, vuex-electron
? Use linting with ESLint? Yes
? Which ESLint config would you like to use? Standard
? Set up unit testing with Karma + Mocha? Yes
? Set up end-to-end testing with Spectron + Mocha? Yes
? What build tool would you like to use? builder
? author hdknr <gmail@hdknr.com>

   vue-cli · Generated "hellovue".

---

All set. Welcome to your new electron-vue project!

Make sure to check out the documentation for this boilerplate at
https://simulatedgreg.gitbooks.io/electron-vue/content/.

Next Steps:

  $ cd hellovue
  $ yarn (or `npm install`)
  $ yarn run dev (or `npm run dev`)
~~~

インストール:

~~~bash
$ cd hellovue
$ npm update
$ npm audit
$ npm install karma@3.1.1
$ npm install
~~~

テスト実行:

~~~bash
$ npm run dev

> hellovue@0.0.1 dev /Users/hide/Documents/Boxes/ubn1804/projects/hellovue
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

  Hash: 18d8275702580a652b47
  Version: webpack 4.25.1
  Time: 2536ms
  Built at: 2018-11-11 21:02:40
                  Asset       Size    Chunks             Chunk Names
  imgs/logo--assets.png   60.4 KiB            [emitted]  
             index.html  434 bytes            [emitted]  
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

  Hash: 35fb50dadc66a19e6484
  Version: webpack 4.25.1
  Time: 2748ms
  Built at: 2018-11-11 21:02:40
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

  Debugger listening on ws://127.0.0.1:5858/0d8ef87e-a068-4bbf-8d19-df1fcc28a808
  For help see https://nodejs.org/en/docs/inspector
  
┗ ----------------------------

~~~

ビルド:

~~~bash
$ npm run build

> hellovue@0.0.1 build /Users/hide/Documents/Boxes/ubn1804/projects/hellovue
> node .electron-vue/build.js && electron-builder

 ___              __                        __                       ___       __    
/\_ \       __   /\ \__     ____           /\ \       __  __   __   /\_ \     /\ \   
\//\ \    / ,.`\ \ \ ,_\   / ,__\  _______ \ \ \____ /\ \/\ \ /\_\  \//\ \    \_\ \  
  \_\ \_ /\  __/  \ \ \/  /\__, `\/\______\ \ \  ,. \\ \ \_\ \\/\ \   \_\ \_ /\ ,. \ 
  /\____\\ \____\  \ \ \_ \/\____/\/______/  \ \____/ \ \____/ \ \ \  /\____\\ \____\
  \/____/ \/____/   \ \__\ \/___/             \/___/   \/___/   \/_/  \/____/ \/___ /
                     \/__/                                                           

  - building main process
  ✔ building main process
  ✔ building renderer process



Hash: b6b40c085e80ef240e57
Version: webpack 4.25.1
Time: 6923ms
Built at: 2018-11-11 21:05:43
  Asset      Size  Chunks             Chunk Names
main.js  1.43 KiB       0  [emitted]  main
Entrypoint main = main.js
[0] external "electron" 42 bytes {0} [built]
[1] ./src/main/index.js 801 bytes {0} [built]
[2] external "path" 42 bytes {0} [built]

Hash: 42a0e8f3f7ae1a4320c4
Version: webpack 4.25.1
Time: 8786ms
Built at: 2018-11-11 21:05:45
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
  • writing effective config file=build/builder-effective-config.yaml
  • no native production dependencies
  • packaging       platform=darwin arch=x64 electron=2.0.13 appOutDir=build/mac
  • downloading               parts=8 size=49 MB url=https://github.com/electron/electron/releases/download/v2.0.13/electron-v2.0.13-darwin-x64.zip
  • downloaded                duration=18.987s url=https://github.com/electron/electron/releases/download/v2.0.13/electron-v2.0.13-darwin-x64.zip
  • signing         file=build/mac/hellovue.app identityName=Developer ID Application: LaFoglia Co.,LTD. (4UZR37U96S) identityHash=B4FBD8F7D7EFA169F1042242A97127F7141257F0 provisioningProfile=none
  • building        target=macOS zip arch=x64 file=build/hellovue-0.0.1-mac.zip
  • building        target=DMG arch=x64 file=build/hellovue-0.0.1.dmg
  • building block map blockMapFile=build/hellovue-0.0.1.dmg.blockmap
  • building embedded block map file=build/hellovue-0.0.1-mac.zip
~~~

## Topic

- https://github.com/SimulatedGREG/electron-vue

## 記事

- https://qiita.com/search?q=electron-vue
- [フロントエンド開発初心者がelectron-vueでアプリをつくってみた　その１～概念編～ - Qiita](https://qiita.com/kurimeg/items/63a28981e619dfed9708)
- [フロントエンド開発初心者がelectron-vueでアプリをつくってみた　その２～実装編～ - Qiita](https://qiita.com/kurimeg/items/1736ab05dde5d8f8973c)
- [electron-vueで自動アップデートを実装する - Qiita](https://qiita.com/hatahata/items/0036294967e0e69c4a3d)
