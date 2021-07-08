# HTTP ステータスコード


- [HTTP レスポンスステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Status)
- [Module ngx_http_stub_status_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html)
- [Module ngx_http_api_module](https://nginx.org/en/docs/http/ngx_http_api_module.html)




[http/ngx_http_request](https://github.com/nginx/nginx/blob/master/src/http/ngx_http_request.h):

~~~c
#define NGX_HTTP_CONTINUE                  100
#define NGX_HTTP_SWITCHING_PROTOCOLS       101
#define NGX_HTTP_PROCESSING                102
#define NGX_HTTP_OK                        200
#define NGX_HTTP_CREATED                   201
#define NGX_HTTP_ACCEPTED                  202
#define NGX_HTTP_NO_CONTENT                204
#define NGX_HTTP_PARTIAL_CONTENT           206
#define NGX_HTTP_SPECIAL_RESPONSE          300
#define NGX_HTTP_MOVED_PERMANENTLY         301
#define NGX_HTTP_MOVED_TEMPORARILY         302
#define NGX_HTTP_SEE_OTHER                 303
#define NGX_HTTP_NOT_MODIFIED              304
#define NGX_HTTP_TEMPORARY_REDIRECT        307
#define NGX_HTTP_PERMANENT_REDIRECT        308
#define NGX_HTTP_BAD_REQUEST               400
#define NGX_HTTP_UNAUTHORIZED              401
#define NGX_HTTP_FORBIDDEN                 403
#define NGX_HTTP_NOT_FOUND                 404
#define NGX_HTTP_NOT_ALLOWED               405
#define NGX_HTTP_REQUEST_TIME_OUT          408
#define NGX_HTTP_CONFLICT                  409
#define NGX_HTTP_LENGTH_REQUIRED           411
#define NGX_HTTP_PRECONDITION_FAILED       412
#define NGX_HTTP_REQUEST_ENTITY_TOO_LARGE  413
#define NGX_HTTP_REQUEST_URI_TOO_LARGE     414
#define NGX_HTTP_UNSUPPORTED_MEDIA_TYPE    415
#define NGX_HTTP_RANGE_NOT_SATISFIABLE     416
#define NGX_HTTP_MISDIRECTED_REQUEST       421
#define NGX_HTTP_TOO_MANY_REQUESTS         429
#define NGX_HTTP_CLOSE                     444
#define NGX_HTTP_NGINX_CODES               494
#define NGX_HTTP_REQUEST_HEADER_TOO_LARGE  494
#define NGX_HTTP_TO_HTTPS                  497
#define NGX_HTTP_CLIENT_CLOSED_REQUEST     499
#define NGX_HTTP_INTERNAL_SERVER_ERROR     500
#define NGX_HTTP_NOT_IMPLEMENTED           501
#define NGX_HTTP_BAD_GATEWAY               502
#define NGX_HTTP_SERVICE_UNAVAILABLE       503
#define NGX_HTTP_GATEWAY_TIME_OUT          504
#define NGX_HTTP_VERSION_NOT_SUPPORTED     505
#define NGX_HTTP_INSUFFICIENT_STORAGE      507
~~~

## 記事

- [nginx で接続状態を確認する(stub_status を使ってみる)](https://server-setting.info/centos/nginx-stub_status-setting.html)
