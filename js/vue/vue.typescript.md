~~~bash 

$ ndenv version
v9.4.0 (set by /Users/hide/.anyenv/envs/ndenv/version)


$ npm install -g @vue/cli
/Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/bin/vue -> /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/@vue/cli/bin/vue.js

> fsevents@1.2.4 install /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/@vue/cli/node_modules/fsevents
> node install

[fsevents] Success: "/Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/@vue/cli/node_modules/fsevents/lib/binding/Release/node-v59-darwin-x64/fse.node" is installed via remote

> protobufjs@6.8.8 postinstall /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/@vue/cli/node_modules/protobufjs
> node scripts/postinstall


> nodemon@1.18.3 postinstall /Users/hide/.anyenv/envs/ndenv/versions/v9.4.0/lib/node_modules/@vue/cli/node_modules/nodemon
> node bin/postinstall || exit 0

Love nodemon? You can now support the project via the open collective:
 > https://opencollective.com/nodemon/donate

+ @vue/cli@3.0.1
added 693 packages in 39.278s

$ vue --version
3.0.1


4 vue create vue-ts-hello

Vue CLI v3.0.1
? Please pick a preset:
  default (babel, eslint)
❯ Manually select features

Vue CLI v3.0.1
? Please pick a preset: Manually select features
? Check the features needed for your project:
 ◯ Babel
 ◉ TypeScript
 ◉ Progressive Web App (PWA) Support
 ◉ Router
 ◉ Vuex
 ◉ CSS Pre-processors
 ◉ Linter / Formatter
 ◉ Unit Testing
❯◉ E2E Testing

Vue CLI v3.0.1
? Please pick a preset: Manually select features
? Check the features needed for your project: TS, PWA, Router, Vuex, CSS Pre-processors, Linter, Unit, E2E
? Use class-style component syntax? Yes
? Use Babel alongside TypeScript for auto-detected polyfills? Yes
? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): SCSS/SASS
? Pick a linter / formatter config: TSLint
? Pick additional lint features: Lint on save
? Pick a unit testing solution: Jest
? Pick a E2E testing solution: Cypress
? Where do you prefer placing config for Babel, PostCSS, ESLint, etc.? In dedicated config files
? Save this as a preset for future projects? (y/N) N

 $ cd vue-ts-hello
 $ npm run serve

> vue-ts-hello@0.1.0 serve /Users/hide/Documents/Tech/annotated-django/samples/vue-ts-hello
> vue-cli-service serve

 INFO  Starting development server...
Starting type checking and linting service...
Using 1 worker with 2048MB memory limit
 98% after emitting CopyPlugin

 DONE  Compiled successfully in 5548ms                                                                                                                                         10:02:02

No type errors found
No lint errors found
Version: typescript 3.0.1, tslint 5.11.0
Time: 5279ms

  App running at:
  - Local:   http://localhost:8080/
  - Network: http://192.168.1.15:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.


~~~

~~~
$ tree -I node_modules
.
├── README.md
├── babel.config.js
├── cypress.json
├── jest.config.js
├── package-lock.json
├── package.json
├── postcss.config.js
├── public
│   ├── favicon.ico
│   ├── img
│   │   └── icons
│   │       ├── android-chrome-192x192.png
│   │       ├── android-chrome-512x512.png
│   │       ├── apple-touch-icon-120x120.png
│   │       ├── apple-touch-icon-152x152.png
│   │       ├── apple-touch-icon-180x180.png
│   │       ├── apple-touch-icon-60x60.png
│   │       ├── apple-touch-icon-76x76.png
│   │       ├── apple-touch-icon.png
│   │       ├── favicon-16x16.png
│   │       ├── favicon-32x32.png
│   │       ├── msapplication-icon-144x144.png
│   │       ├── mstile-150x150.png
│   │       └── safari-pinned-tab.svg
│   ├── index.html
│   ├── manifest.json
│   └── robots.txt
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   └── HelloWorld.vue
│   ├── main.ts
│   ├── registerServiceWorker.ts
│   ├── router.ts
│   ├── shims-tsx.d.ts
│   ├── shims-vue.d.ts
│   ├── store.ts
│   └── views
│       ├── About.vue
│       └── Home.vue
├── tests
│   ├── e2e
│   │   ├── plugins
│   │   │   └── index.js
│   │   ├── specs
│   │   │   └── test.js
│   │   └── support
│   │       ├── commands.js
│   │       └── index.js
│   └── unit
│       └── HelloWorld.spec.ts
├── tsconfig.json
└── tslint.json

13 directories, 42 files
~~~

## 記事

- [TypeScriptでVue.jsを書く – Vue CLIを使った開発のポイントを紹介 | maesblog](https://mae.chab.in/archives/60167)
