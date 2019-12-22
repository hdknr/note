# CORS ヘッダーの確認

`Origin` ヘッダーを入れること:

~~~bash
$ curl  -u admin:pass -i -s -H "Origin: http://localhost:9000"  -F "hostname=client1" https://api1.com/accounts/api/client/

HTTP/1.1 200 OK
Date: Fri, 26 Apr 2019 08:55:13 GMT
Content-Type: application/json
Content-Length: 279
Vary: Accept, Cookie, Origin
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://localhost:9000
~~~
