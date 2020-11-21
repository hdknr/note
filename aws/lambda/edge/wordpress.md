# Wordpressユーザー認証

## シナリオ

- `/media` のオリジンを S3バケットとする
- `/media` に認証をかける
- `/` のオリジンが Wordpressなので、 Wordpressのユーザー管理でパスワード認証をかける

## 1. S3 のオリジン

- S3バケットを作成
- オリジンに登録
- `Public Access` はさせない
- `Restrict Bucket Access` を `Create a New Identity`にして、 S3のURLの直リンを禁止
- `Origin Access Identity` を適切に設定し、 `Grant Read Permissions on Bucket` も `Yes, Update Bucket Polic`

S3バケット`my-media` の `バケットポリシー`:

~~~json
{
    "Version": "2008-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E3VC81AJ9JZ4HH"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-media/*"
        }
    ]
}
~~~

#### 2. `/media*` ビヘイビア

- `Path Pattern`: `/media*`
- `Origin or Origin Group`: 作成したS3オリジン

Lambda Edgeを作成したら:

- `Lambda Function Associations` に　`CloudFront Event` として `Viewer Request`の　Lambda@Edge をアサインする 
- `Include Body`  にチェックをいれる


## 3. 認証の Lambda@Edgeを作成

- PHPの認証プログラム(`/auht.php`) で作成したHMAC(SHA256)を検証して一致したら認証しているものとみなす。

`lambda_function.py`:

~~~py
import json
import hmac
import hashlib
import os
import re
from urllib import parse
import conf
import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def redirect(path):
    url = conf.AUTH_URL  + '?' + parse.urlencode({conf.NEXT_KEY: path})
    res = {
            "key": "Location",
            "value": url,
        }
        
    return {
        'status': '301',
        'statusDescription': 'Redirect',
        'body': 'Auth Required',
        'headers': {
            'location': [res],
        },
    }
    
    
def isValidAuthHamc(key, source, value):
    v = hmac.new(key.encode(), source.encode(), hashlib.sha256).hexdigest()
    logger.info(f'("{key}", "{source}") {v} == {value}')
    return value == v
    
        
def isValidAuthHamcCookies(cookies):

    authmac = cookies.pop('AuthHmac', None)
    authdata = cookies.pop('AuthData', None)
    if authmac and authdata:
        return isValidAuthHamc(conf.KEY, parse.unquote(authdata), authmac)
        
    logger.info('no authdata or authhmac')
    return False
    
    
def parse_cookie(cookies):
    src = ';'.join(
        map(lambda i: i['value'], 
            filter(lambda i: i.get('key', '') == 'cookie' and 'value' in i, cookies)))
    return src and dict([i.split('=') for i in re.split(r'\s*;\s*', src) if i.find('=') > 0]) or {}
   
   
def main(request, cookies):
    try:
        values = parse_cookie(cookies)
        logger.info(str(values))
        if isValidAuthHamcCookies(values):
            return request
    except:
        logger.error(traceback.format_exc())
    
    return redirect(request.get('uri', '/'))
    
    
def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    headers = request['headers']
    cookies = headers.get('cookie', [])
        
    return main(request, cookies)
~~~

`conf.py` に設定情報をいれる(Lambda@Edgeは環境変数使えません):

~~~py
AUTH_URL = '/auth.php'
KEY = '......'
NEXT_KEY = 'redirect_to'
~~~

## 4. '/auth.php` ビヘイビアの作成

- オリジンは `/` の Wordpressとする
- `Path Pattern`: `/auth.php`
- `Allowed HTTP Methods`:   `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
- キャッシュさせない: `Minimum TTL`, `Maximum TTL` : 0

### 5. `/auth.php` の実装

- Wordpressのユーザーで認証する

~~~php
<?php
require_once(__DIR__ . '/wp-config.php');

function getAuthHmac($data){
   $key = AUTH_KEY;             # wp-config.php で設定
   $hmac = hash_hmac('sha256', $data, $key);
   return $hmac;
}

$auth_required = ( 'POST' === $_SERVER['REQUEST_METHOD'] ) && isset($_POST['log']) && isset($_POST['pwd']);
$secure_cookie = false;

if ( $auth_required ) { 
    # Wordpressの標準ログイン( log + pwd)
    $user = wp_signon( array(), $secure_cookie );

    if ( $user ){

        # SHA256のデータを WPの認証クッキーとする
        $data = wp_generate_auth_cookie($user->ID, time());     

        # ２つのクッキーでHMACのデータを渡す
	    setcookie('AuthHmac', getAuthHmac($data));
        setcookie('AuthData', $data); 

        # redirect_toに指定されたURLにリダイレクトさせる
        $requested_redirect_to = isset( $_REQUEST['redirect_to'] ) ? $_REQUEST['redirect_to'] : '';
	    wp_safe_redirect($requested_redirect_to);
   }
}
?>

<!DOCTYPE html>
<!-- 以下, Wordpressの認証ページを参考にログインページを作成  -->
~~~