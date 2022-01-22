# SPA対応

- 条件によってオリジンリクエストを修正する


## シンプルケース

条件:

- パスが拡張子でおわっていたら何もしない
- それ位以外は `/ビヘイビアプレフィクス/index.htm をリクエストする

~~~js

~~~js
const reAbsolute = /.+\.[^/]+$/;
const reBase = /(^\/[^\/]+)(.*)/;

exports.handler = function handler(event, context, callback) {
    const { request } = event.Records[0].cf
    const { uri } = request

    if (!uri.match(reAbsolute)) {
        request.uri = uri.replace(reBase, "$1") + '/index.html'
        callback(null, request)
        return
    }
    callback(null, request)
}
~~~
