## ndenv

~~~bash
$ ndenv install v9.4.0
Downloading node-v9.4.0-darwin-x64.tar.gz...
-> https://nodejs.org/dist/v9.4.0/node-v9.4.0-darwin-x64.tar.gz
Installing node-v9.4.0-darwin-x64...
Installed node-v9.4.0-darwin-x64 to /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0
~~~

~~~bash
$ ndenv global v9.4.0
~~~

## vue-cli

~~~bash
$ npm install --global vue-cli
npm WARN deprecated coffee-script@1.12.7: CoffeeScript on NPM has moved to "coffeescript" (no hyphen)
/Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/bin/vue -> /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/vue-cli/bin/vue
/Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/bin/vue-init -> /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/vue-cli/bin/vue-init
/Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/bin/vue-list -> /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/vue-cli/bin/vue-list
+ vue-cli@2.9.2
added 264 packages in 9.963s
~~~

## nuxt　プロジェクト

~~~bash
$ vue init nuxt-community/starter-template sample

? Project name sample
? Project description Nuxt.js project
? Author hdknr <gmail@hdknr.com>

   vue-cli · Generated "sample".

   To get started:

     cd sample
     npm install # Or yarn
     npm run dev
~~~

~~~bash
$ cd sample

$ tree .
.
├── README.md
├── assets
│   └── README.md
├── components
│   ├── Logo.vue
│   └── README.md
├── layouts
│   ├── README.md
│   └── default.vue
├── middleware
│   └── README.md
├── nuxt.config.js
├── package.json
├── pages
│   ├── README.md
│   └── index.vue
├── plugins
│   └── README.md
├── static
│   ├── README.md
│   └── favicon.ico
└── store
    └── README.md

8 directories, 15 files
~~~

## 依存パッケージインストール

~~~bash
$ cat package.json
~~~

~~~js
{
  "name": "sample",
  "version": "1.0.0",
  "description": "Nuxt.js project",
  "author": "hdknr <gmail@gmail.com>",
  "private": true,
  "scripts": {
    "dev": "nuxt",
    "build": "nuxt build",
    "start": "nuxt start",
    "generate": "nuxt generate",
    "lint": "eslint --ext .js,.vue --ignore-path .gitignore .",
    "precommit": "npm run lint"
  },
  "dependencies": {
    "nuxt": "^1.0.0"
  },
  "devDependencies": {
    "babel-eslint": "^7.2.3",
    "eslint": "^4.3.0",
    "eslint-config-standard": "^10.2.1",
    "eslint-loader": "^1.9.0",
    "eslint-plugin-html": "^3.1.1",
    "eslint-plugin-import": "^2.7.0",
    "eslint-plugin-node": "^5.1.1",
    "eslint-plugin-promise": "^3.5.0",
    "eslint-plugin-standard": "^3.0.1"
  }
}
~~~


~~~bash
$ npm install

> fsevents@1.1.3 install /Users/hide/Documents/Boxes/ubn/projects/nuxts/sample/node_modules/fsevents
> node install

[fsevents] Success: "/Users/hide/Documents/Boxes/ubn/projects/nuxts/sample/node_modules/fsevents/lib/binding/Release/node-v59-darwin-x64/fse.node" is installed via remote

> uglifyjs-webpack-plugin@0.4.6 postinstall /Users/hide/Documents/Boxes/ubn/projects/nuxts/sample/node_modules/webpack/node_modules/uglifyjs-webpack-plugin
> node lib/post_install.js


> nuxt@1.0.0 postinstall /Users/hide/Documents/Boxes/ubn/projects/nuxts/sample/node_modules/nuxt
> opencollective postinstall || exit 0

[server error] Cannot load the stats for nuxtjs – please try again later

                                     :=.
                                    -=+=:   :-
                                  .-=+++=: :++=.
                                 .-+++++++=++++=.
                                .=+++++++****++++.
                               :=+++++++******++*+:
                              :=+++++++********++*+:
                             :=+++++++**********++*+-
                            -=+++++++*************+*+-.
                          .-=======+**************++++=.
                          .........::::::::::::::::::::.


                          Thanks for installing nuxt 🙏
                 Please consider donating to our open collective
                        to help us maintain this package.


           👉  Donate: https://opencollective.com/nuxtjs/donate

npm notice created a lockfile as package-lock.json. You should commit this file.
added 1315 packages in 27.102s
~~~

## 実行

~~~bash
$ npm run dev
> sample@1.0.0 dev /Users/hide/Documents/Boxes/ubn/projects/nuxts/sample
> nuxt

  nuxt:build App root: /Users/hide/Documents/Boxes/ubn/projects/nuxts/sample +0ms
  nuxt:build Generating /Users/hide/Documents/Boxes/ubn/projects/nuxts/sample/.nuxt files... +1ms
  nuxt:build Generating files... +23ms
  nuxt:build Generating routes... +5ms
  nuxt:build Building files... +19ms
  nuxt:build Adding webpack middleware... +507ms
  ████████████████████ 100%

Build completed in 3.203s



 DONE  Compiled successfully in 3205ms                                                                                                                                10:09:43


 OPEN  http://localhost:3000
~~~


~~~bash
$ curl http://localhost:3000 | pup
~~~

~~~html
<html data-n-head-ssr="" data-n-head="">
 <head>
  <meta data-n-head="true" charset="utf-8">
  <meta data-n-head="true" name="viewport" content="width=device-width, initial-scale=1">
  <meta data-n-head="true" data-hid="description" name="description" content="Nuxt.js project">
  <title data-n-head="true">
   sample
  </title>
  <link data-n-head="true" rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="preload" href="/_nuxt/manifest.js" as="script">
  <link rel="preload" href="/_nuxt/vendor.js" as="script">
  <link rel="preload" href="/_nuxt/app.js" as="script">
  <link rel="prefetch" href="/_nuxt/pages/index.js">
  <link rel="prefetch" href="/_nuxt/layouts/default.js">
  <style data-vue-ssr-id="7bfb1fe6:0">
   .nuxt-progress {
  position: fixed;
  top: 0px;
  left: 0px;
  right: 0px;
  height: 2px;
  width: 0%;
  -webkit-transition: width 0.2s, opacity 0.4s;
  transition: width 0.2s, opacity 0.4s;
  opacity: 1;
  background-color: #efc14e;
  z-index: 999999;
}
  </style>
  <style data-vue-ssr-id="057cd565:0">
   html {
  font-family: &#34;Source Sans Pro&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, &#34;Helvetica Neue&#34;, Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}
*, *:before, *:after {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  margin: 0;
}
.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}
.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}
.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}
.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}
  </style>
  <style data-vue-ssr-id="066f8cc9:0">
   .container {
  min-height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  text-align: center;
}
.title {
  font-family: &#34;Quicksand&#34;, &#34;Source Sans Pro&#34;, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, &#34;Helvetica Neue&#34;, Arial, sans-serif; /* 1 */
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}
.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}
.links {
  padding-top: 15px;
}
  </style>
  <style data-vue-ssr-id="52e05c84:0">
   .VueToNuxtLogo {
  display: inline-block;
  -webkit-animation: turn 2s linear forwards 1s;
          animation: turn 2s linear forwards 1s;
  -webkit-transform: rotateX(180deg);
          transform: rotateX(180deg);
  position: relative;
  overflow: hidden;
  height: 180px;
  width: 245px;
}
.Triangle {
  position: absolute;
  top: 0;
  left: 0;
  width: 0;
  height: 0;
}
.Triangle--one {
  border-left: 105px solid transparent;
  border-right: 105px solid transparent;
  border-bottom: 180px solid #41B883;
}
.Triangle--two {
  top: 30px;
  left: 35px;
  -webkit-animation: goright 0.5s linear forwards 3.5s;
          animation: goright 0.5s linear forwards 3.5s;
  border-left: 87.5px solid transparent;
  border-right: 87.5px solid transparent;
  border-bottom: 150px solid #3B8070;
}
.Triangle--three {
  top: 60px;
  left: 35px;
  -webkit-animation: goright 0.5s linear forwards 3.5s;
          animation: goright 0.5s linear forwards 3.5s;
  border-left: 70px solid transparent;
  border-right: 70px solid transparent;
  border-bottom: 120px solid #35495E;
}
.Triangle--four {
  top: 120px;
  left: 70px;
  -webkit-animation: godown 0.5s linear forwards 3s;
          animation: godown 0.5s linear forwards 3s;
  border-left: 35px solid transparent;
  border-right: 35px solid transparent;
  border-bottom: 60px solid #fff;
}
@-webkit-keyframes turn {
100% {
    -webkit-transform: rotateX(0deg);
            transform: rotateX(0deg);
}
}
@keyframes turn {
100% {
    -webkit-transform: rotateX(0deg);
            transform: rotateX(0deg);
}
}
@-webkit-keyframes godown {
100% {
    top: 180px;
}
}
@keyframes godown {
100% {
    top: 180px;
}
}
@-webkit-keyframes goright {
100% {
    left: 70px;
}
}
@keyframes goright {
100% {
    left: 70px;
}
}
  </style>
 </head>
 <body data-n-head="">
  <div data-server-rendered="true" id="__nuxt">
   <div class="nuxt-progress" style="width:0%;height:2px;background-color:#3B8070;opacity:0;">
   </div>
   <div id="__layout">
    <div>
     <section class="container">
      <div>
       <div class="VueToNuxtLogo">
        <div class="Triangle Triangle--two">
        </div>
        <div class="Triangle Triangle--one">
        </div>
        <div class="Triangle Triangle--three">
        </div>
        <div class="Triangle Triangle--four">
        </div>
       </div>
       <h1 class="title">
        sample
       </h1>
       <h2 class="subtitle">
        Nuxt.js project
       </h2>
       <div class="links">
        <a href="https://nuxtjs.org/" target="_blank" class="button--green">
         Documentation
        </a>
        <a href="https://github.com/nuxt/nuxt.js" target="_blank" class="button--grey">
         GitHub
        </a>
       </div>
      </div>
     </section>
    </div>
   </div>
  </div>
  <script type="text/javascript">
   window.__NUXT__={"layout":"default","data":[{}],"error":null,"state":{},"serverRendered":true};
  </script>
  <script src="/_nuxt/manifest.js" defer="">
  </script>
  <script src="/_nuxt/vendor.js" defer="">
  </script>
  <script src="/_nuxt/app.js" defer="">
  </script>
 </body>
</html>
~~~

## スタティックサイトジェネレータ

~~~bash
$ vue init nuxt-community/starter-template shaper
$ cd shaper
$ npm install
~~~

~~~bash 
$ npm run generate --ssr

> shaper@1.0.0 generate /Users/hide/Documents/Tech/tmp/shaper
> nuxt generate

  nuxt:generate Generating... +0ms
  nuxt:build App root: /Users/hide/Documents/Tech/tmp/shaper +0ms
  nuxt:build Generating /Users/hide/Documents/Tech/tmp/shaper/.nuxt files... +0ms
  nuxt:build Generating files... +50ms
  nuxt:build Generating routes... +6ms
  nuxt:build Building files... +17ms
  ████████████████████ 100% 

Build completed in 9.029s

 DONE  Compiled successfully in 9032ms                                                                                                               13:22:27

Hash: 826418b29c15fabd8828
Version: webpack 3.12.0
Time: 9032ms
                                  Asset       Size  Chunks             Chunk Names
    pages/index.bad21caf5aec6e92e66a.js    4.05 kB       0  [emitted]  pages/index
layouts/default.43b36a86c35a6950d916.js    1.42 kB       1  [emitted]  layouts/default
         vendor.13ef70b463ce71c01a92.js     145 kB       2  [emitted]  vendor
            app.9024e623c2ef58df1c1b.js      28 kB       3  [emitted]  app
       manifest.826418b29c15fabd8828.js    1.47 kB       4  [emitted]  manifest
                               LICENSES  604 bytes          [emitted]  
 + 3 hidden assets
Hash: 906707197973097cd37b
Version: webpack 3.12.0
Time: 750ms
             Asset    Size  Chunks             Chunk Names
server-bundle.json  125 kB          [emitted]  
  nuxt: Call generate:distRemoved hooks (1) +0ms
  nuxt:generate Destination folder cleaned +11s
  nuxt: Call generate:distCopied hooks (1) +21ms
  nuxt:generate Static & build files copied +21ms
  nuxt:render Rendering url / +0ms
  nuxt: Call generate:page hooks (1) +135ms
  nuxt:generate Generate file: /index.html +134ms
  nuxt:render Rendering url / +131ms
  nuxt: Call generate:done hooks (1) +3ms
  nuxt:generate HTML Files generated in 11.1s +3ms
  nuxt:generate Generate done +0ms
~~~

~~~bash 
$ tree dist/
dist/
├── 200.html
├── README.md
├── _nuxt
│   ├── LICENSES
│   ├── app.9024e623c2ef58df1c1b.js
│   ├── layouts
│   │   └── default.43b36a86c35a6950d916.js
│   ├── manifest.826418b29c15fabd8828.js
│   ├── pages
│   │   └── index.bad21caf5aec6e92e66a.js
│   └── vendor.13ef70b463ce71c01a92.js
├── favicon.ico
└── index.html

3 directories, 10 files
~~~

~~~bash
$ python -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
~~~

~~~bash 
$ curl -s http://localhost:8000/dist/ | pup "h1"
<h1 class="title">
 shaper
</h1>
~~~