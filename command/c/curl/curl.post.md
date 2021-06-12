# POST

## フォーム送信: `-F` オプション

- [curlコマンドから HTTP POST する方法
](https://qiita.com/letsspeak/items/8c7266742371699ab45e)

FORM:

~~~bash
$ curl -F "name1=value1" -F "name2=value2" http://yourdomain/execute.script
.
~~~

## データ送信: `-d`

~~~bash
$ curl http://dev.mysite.com/articles/wp-json/wp/v2/posts -X POST -d 'title=title' -d 'content=sample content' -d 'slug=api-sample'
.
~~~

~~~bash
$ curl -X POST -H "Content-Type: application/json"  -d @TC-00001.json  http://localhost:8182/order
~~~

## JSON 送信

JSON:

~~~bash
$ curl -X POST -H "Content-Type: application/json" -d '
{
    "name": "Manager",
    "description": "someone who manages"
}'
~~~

## 応答ヘッダーを表示 (`--dump-header -`)

~~~bash
$ curl --dump-header - --user 'articles:@articles!1998@' http://dev.mysite.com/articles/wp-json/wp/v2/posts -X POST -d 'title=title' -d 'content=sample content' -d 'slug=api-sample'

HTTP/1.1 403 Forbidden
Server: nginx/1.14.0 (Ubuntu)
Date: Mon, 26 Aug 2019 23:10:19 GMT
Content-Type: text/html
Content-Length: 178
Connection: keep-alive

<html>
<head><title>403 Forbidden</title></head>
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.14.0 (Ubuntu)</center>
</body>
</html>
~~~
