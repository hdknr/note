# Lambda@Edge

## サンプル

[一般的](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-general-examples):

- [A/Bテスト](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-a-b-testing)
- [応答ヘッダの書き換え](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-overriding-response-header) 

[応答生成](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-generated-response-examples):

- [静的コンテンツ](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-static-web-server)
- [Gzip圧縮した静的コンテンツ](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-body-encoding-base64)
- [HTTPリダイレクト](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#w713aac27c55c25c17b9b3)


[クエリ](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-query-string-examples):

- [クエリによってヘッダーを追加](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-header-based-on-query-string)
- [クエリを正規化してキャッシュヒットをあげる](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-normalize-query-string-parameters)
- [匿名ユーザーをログインページに飛ばす](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirect-to-signin-page)

[パーソナライズ(国/デバイス)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirecting-examples):
- [Viewer Requestを国別URLにリダイレクト](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirect-based-on-country)
- [デバイスとごとに別のバージョンのオブジェクトを返す](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-vary-on-device-type)

[動的オリジン変更(Origin-Requestトリガ)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-content-based-routing-examples):
- [でカスタムオリジンからS3オリジンへ変更](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-content-based-S3-origin-based-on-query)
- [S3オリジンを切り替える](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-content-based-S3-origin-request-trigger)
- [S3からカスタムオリジンへ変更](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-content-based-custom-origin-request-trigger)
- [徐々にS3バケットへのトラフィックを別のバケットへ転送](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-content-based-gradual-traffic-transfer)
- [Countryヘッダーでオリジンのドメイン名を変更する](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-content-based-geo-header)

[エラーステータス更新(Origin-Requetsトリガ)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-update-error-status-examples):
- [エラーを200に変更](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-custom-error-static-body)
- [エラーを302 Not Foundに変更](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-custom-error-new-site)

[リクエストボディ変更(Requestトリガ)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-access-request-body-examples):
- [HTMLフォームを読む](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-access-request-body-examples-read) 
- [HTMLフォームを変更](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-access-request-body-examples-replace)

## lambda

### リクエスト, レスポンス, ヘッダー

~~~py
def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']          # Request トリガ
    response = event['Records'][0]['cf']['response']        # Response トリガ
    headers = request['headers']
    ...
    return request

~~~

### `uri` の変更

- `uri` には クエリを付けないこと
- `querystring` に設定する

~~~py
def lambda_handler(event, context):
    ...
    request['uri'] = modified_uri
    ...
    return request
~~~

### クエリ

~~~py
from urllib.parse import parse_qs, urlencode

def lambda_handler(event, context):
    ...
    params = {k : v[0] for k, v in parse_qs(request['querystring']).items()}
    ...
    request['querystring'] = urlencode(params)
    ...
    return request
~~~

### ヘッダー追加

~~~py
def lambda_handler(event, context):
    ...
    headers['x-original-ua'] = [{'value': ua}]
    ...
    return request
~~~

### コンテンツ返答

~~~py
def lambda_handler(event, context):
    ...
    html = '<html>....'
    response = {
        'status': '200', 'statusDescription': 'OK',
         'headers': {
            'cache-control': [
                {'key': 'Cache-Control', 'value': 'max-age=100'}
            ],
            "content-type": [
                {'key': 'Content-Type', 'value': 'text/html'}
            ],
            'content-encoding': [
                {'key': 'Content-Encoding', 'value': 'UTF-8'}
            ]
        },
        'body': html
    }
    ...
    return response
~~~

### リダイレクト

~~~py
def lambda_handler(event, context):
    ...
    response = {
        'status': '302',
        'statusDescription': 'Found',
        'headers': {
            'location': [{
                'key': 'Location',
                'value': 'http://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html'
            }]
        }
    }
    ...
    return response # リクエストトリガでも応答を返して良い
~~~



### クッキー

~~~py
def parseCookies(headers):
    parsedCookie = {}
    if headers.get('cookie'):
        for cookie in headers['cookie'][0]['value'].split(';'):
            if cookie:
                parts = cookie.split('=')
                parsedCookie[parts[0].strip()] = parts[1].strip()
    return parsedCookie

def lambda_handler(event, context):
    ...
    parsedCookies = parseCookies(headers)
    ...
    return request
~~~

### カスタムオリジンホスト変更

~~~py
def lambda_handler(event, context):
    ...
    doaminName = 'test.mysite.com'
    ...
    request['origin'] = {
        'custom': {
            'domainName': domainName,
            'port': 443,
            'protocol': 'https',
            'path': '',
            'sslProtocols': ['TLSv1', 'TLSv1.1'],
            'readTimeout': 5,
            'keepaliveTimeout': 5,
            'customHeaders': {}
            }
        }
    ...
    request['headers']['host'] = [{'key': 'host', 'value': doaminName}]
    ...
    return request
~~~

もしくは:

~~~py
def lambda_handler(event, context):
    ...
    doaminName = 'test.mysite.com'
    ...
    request['origin']['custom']['domainName'] = domainName
    request['headers']['host'] = [{'key': 'host', 'value': domainName}]
    ...
    return request
~~~

### S3オリジンホスト変更

~~~py
def lambda_handler(event, context):
    ...
    s3DomainName = 'my-bucket.s3.amazonaws.com'
    ...
    request['origin'] = {
        's3': {
            'domainName': s3DomainName,
            'region': '',
            'authMethod': 'none',
            'path': '',
            'customHeaders': {}
        }
    }
    ...
    request['headers']['host'] = [{'key': 'host', 'value': s3DomainName}]
    ...
    return request
~~~

### 応答ステータス

~~~py
def lambda_handler(event, context):
    ...
    response['status'] = 200
    response['statusDescription'] = 'OK'
    response['body'] = 'Body generation example'
    ...
    return response
~~~
