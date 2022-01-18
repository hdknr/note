# S3: リダイレクタ

やること:

- リダイレクトルールを設定した公開ホスティングS3を作る
- Route53でZAA(Zone Apex Alias)レコードでS3を向ける

### short.com S3バケット  

#### プロパティ

- 静的ウェブサイトホスティング: 有効にする
- ホスティングタイプ:  静的ウェブサイトをホストする
- インデックスドキュメント: index.html
- リダイレクトルール 

    ~~~json
    [
        {
            "Condition": {
                "KeyPrefixEquals": "*"
            },
            "Redirect": {
                "HostName": "wwww.yoursite.com",
                "HttpRedirectCode": "301",
                "Protocol": "https",
                "ReplaceKeyWith": "manual/"
            }
        }
    ]
    ~~~

#### アクセス許可

- ブロックパブリックアクセス (バケット設定): オフ
- バケットポリシー:

    ~~~json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Statement1",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::short.com/*"
            }
        ]
    }
    ~~~

### Route53: `short.com` ゾーン

DNS:

~~~
ns-1096.awsdns-09.org
ns-230.awsdns-28.com
ns-796.awsdns-35.net
ns-1567.awsdns-03.co.uk
~~~

`short.com` の Aレコード

- 上記の S3バケットに `ALIAS`  登録する
