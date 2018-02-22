var path = require('path')
var webpack = require('webpack')
var modules = require('./modules.json')   // *.js のサーチパス
/* modules.json:
[
  "/vagrant/projects/mycompany/myservice/web/theme/templates/vue",
  "/vagrant/projects/mycompany/myservice/web/djvue/vue"
]
*/
var sources = require('./sources.json')   // モジュールのソース
/* sources.json:
[
    "app/entry/index.js",
    "app/entry/edit.js"
]
*/

// マルチエントリ
var entry = {};
sources.map((i) => {entry[i.replace('.js', '')] = i})

module.exports = {
  entry: entry,         // マルチエントリ https://webpack.js.org/configuration/entry-context/#entry
  output: {             // https://webpack.js.org/configuration/output/
    path: path.resolve(__dirname, './static/bundles/'),   // 出力先ディレクトリ
    publicPath: '/static/bundles',
    filename: '[name].bundle.js'                          // バンドルファイル名
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      },
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader'
        ],
      },
      {
        test: /\.sass$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader?indentedSyntax'
        ],
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
            // Since sass-loader (weirdly) has SCSS as its default parse mode, we map
            // the "scss" and "sass" values for the lang attribute to the right configs here.
            // other preprocessors should work out of the box, no loader config like this necessary.
            'scss': [
              'vue-style-loader',
              'css-loader',
              'sass-loader'
            ],
            'sass': [
              'vue-style-loader',
              'css-loader',
              'sass-loader?indentedSyntax'
            ]
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  resolve: {  // https://webpack.js.org/configuration/resolve/
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    modules: [path.resolve(__dirname, 'node_modules'), path.resolve(__dirname, 'src')].concat(modules), // モジュール検索パス
    extensions: ['*', '.js', '.vue', '.json']
  },
  resolveLoader: {  // https://webpack.js.org/configuration/resolve/#resolveloader
    modules: [path.resolve(__dirname, 'node_modules')],   // ローダーの検索パス
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
