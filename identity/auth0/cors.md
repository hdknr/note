## 同一オリジン(Same Origin Policy)

2つのページにおいて,

- プロトコルとポート番号（もしあれば）とホストが等しい場合、両者のページは同一のオリジンを持っていると見なされます。
- ここでは「スキーム/ホスト/ポート」の組み合わせで参照されます。


ドメインとオリジンの違い:

- ドメインは yoursite.com みたいな部分だけ
- オリジンは http や https などプロトコルと ポート番号が含まれる 

## [Originリクエストヘッダー](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)


- フェッチの起点を示します
- パス情報は含まれず、サーバー名のみ
- Referer ヘッダーと似ています


## peflight リクエスト



- HTTPメソッドが `OPTIONS`
- リクエストヘッダにAccess-Control-Request-Methodフィールドが付加


応答例:

~~~
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://trustedsite.com
Access-Control-Allow-Methods: GET,POST,HEAD,OPTIONS
~~~

## オリジンをまたいだデータストレージアクセス

- localStorage や IndexedDB など、ブラウザー内部に保存されるデータへのアクセスは、オリジンによって権限が分かれています。
- それぞれのオリジンが個別にストレージを持ち、あるオリジンの JavaScript から別のオリジンに属するストレージを読み書きすることはできません。

## Cookie

- クロスドメインアクセスを行う際、デフォルトではCookieのやりとりができない


[withCredentials](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials)はデフォルトで`false`だが有効にできる:

~~~js 
axios.get('/some/url', { 
  xsrfHeaderName: 'X-CSRF-Token',
  withCredentials: true
})
~~~

ただし `/some/url` が 以下のCORSヘッダーを返さないとブラウザが受け取らない: 

~~~
Access-Control-Allow-Credentials: true
~~~



## 記事


- [オリジン間リソース共有 (CORS) ](https://developer.mozilla.org/ja/docs/Web/HTTP/HTTP_access_control)
- [同一オリジンポリシー](https://developer.mozilla.org/ja/docs/Web/Security/Same-origin_policy)
- [HTML5 Security Cheatsheet](https://html5sec.org/)
- [Research Papers on HTML5 Security](http://html5security.org/)
- [CORSまとめ](https://qiita.com/tomoyukilabs/items/81698edd5812ff6acb34)
- [CORS(Cross-Origin Resource Sharing)によるクロスドメイン通信の傾向と対策](https://dev.classmethod.jp/cloud/cors-cross-origin-resource-sharing-cross-domain/)
- [CORS(Cross-Origin Resource Sharing)について整理してみた](https://dev.classmethod.jp/etc/about-cors/)
- [Learning from XAuth: Cross-domain localStorage](https://www.nczonline.net/blog/2010/09/07/learning-from-xauth-cross-domain-localstorage/)
- [[JavaScript]サーバーを使わずにクロスドメインなスタンプラリーシステム。](http://d.hatena.ne.jp/shunsuk/20111012/1318420264)

## Django 

- [ottoyiu/django-cors-headers](https://github.com/ottoyiu/django-cors-headers)


## 3rd パーティークッキー

- yoursite.com(1stパーティ)からブラウザ(2nd パーティ)が取得した応答からスクリプトでXMLHttpRequest で google.com (3rdパーティ) にアクセスする際に送信するクッキー

- [Firefox:サードパーティ Cookie を禁止する](https://support.mozilla.org/ja/kb/disable-third-party-cookies)