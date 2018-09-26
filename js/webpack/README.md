## Webpack

- [#65](https://github.com/hdknr/scriptogr.am/issues/65)

### 例

~~~bash
$ yarn add webpack
~~~

packages.json:

~~~js
{
  "scripts": {
    "build": "`yarn bin`/webpack"
  },
  "dependencies": {
    "axios": "^0.16.2",
    "vue": "^2.4.4",
    ....
  },
  "devDependencies": {
    "webpack": "^3.8.1"
  }
}
~~~

webpack.config.js:

~~~js
var webpack = require('webpack');

module.exports = {
  entry: __dirname + "/index.js",
  output: {
    path: __dirname + '/static/lib',
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery"
    })
  ]
}
~~~

index.js:

~~~js
import {$,jQuery} from 'jquery';
.....
~~~

ビルド:

~~~bash
$ yarn run build

yarn run v1.2.1
$ `yarn bin`/webpack
Hash: a7ed2486d39d4b24fed6
Version: webpack 3.8.1
Time: 730ms
   Asset    Size  Chunks                    Chunk Names
bundle.js  676 kB       0  [emitted]  [big]  main
  [9] (webpack)/buildin/global.js 488 bytes {0} [built]
 [10] ./index.js 249 bytes {0} [built]
   + 47 hidden modules
Done in 2.44s.
~~~

## 関連

- [webpack-contrib/webpack-bundle-analyzer: Webpack plugin and CLI utility that represents bundle content as convenient interactive zoomable treemap](https://github.com/webpack-contrib/webpack-bundle-analyzer)


## 記事

[最新版で学ぶwebpack 3入門(図解付き) – JS開発で必須のモジュールバンドラー ](https://ics.media/entry/12140)

- 「CSSや画像を含むあらゆるアセットファイルをJavaScriptとして出力する」ことが基本的な使い方
- ECMAScript Modules(ES Modules/ESM)をサポート
- [Tree Shaking](https://qiita.com/pirosikick/items/863830856891d40308cb)（未使用のモジュールを省いてバンドルする機能）が使える
