CORS (Cross-Origin Resource Sharing)

##  Origin `呼び出し元URL` is therefore not allowed access (Chrome)

Safari:
~~~
[Error] Origin http://localhost.lafoglia.jp:3000 is not allowed by Access-Control-Allow-Origin.
[Error] Failed to load resource: Origin http://localhost.lafoglia.jp:3000 is not allowed by Access-Control-Allow-Origin. (ssodata, line 0)
[Error] XMLHttpRequest cannot load https://lafoglia.auth0.com/user/ssodata/ due to access control checks.
~~~

- Ajax 呼び出し先URLで、呼び出し元を許可する必要がある


## 記事

- [CORSまとめ](https://qiita.com/tomoyukilabs/items/81698edd5812ff6acb34)


trustedsite.comが呼び出し元:

~~~
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://trustedsite.com
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET,POST,HEAD,OPTIONS
Access-Control-Allow-Headers: X-MyRequest,X-MyOption
~~~