## Webpack

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
