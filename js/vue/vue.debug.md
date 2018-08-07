# デバッグ


## vue-debtools

https://github.com/vuejs/vue-devtools

- Chrome Extension, Firefox Addon をインストールする

- npm で development ビルドする

package.json:

`devbuildを追加

~~~json
  "scripts": {
    "dev": "cross-env NODE_ENV=development webpack-dev-server --open --hot",
    "devbuild": "cross-env NODE_ENV=development webpack --progress --hide-modules",
    "build": "cross-env NODE_ENV=production webpack --progress --hide-modules"
  },
~~~

ビルド:

~~~sh
$ npm run devbuild
~~~
