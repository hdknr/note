# Route53


## Zone Apex Alias

- [【小ネタ】Route 53 のホストゾーンに CNAME レコードと重複するドメイン名で MX レコードを登録しようとしたらきちんと怒られた](https://dev.classmethod.jp/articles/cname-resouce-record-conflict/)
- [Amazon Route 53のALIASレコード利用のススメ](https://dev.classmethod.jp/articles/amazon-route-53-alias-records/)
- [Route 53でZone ApexドメインをS3を使ってリダイレクトする](https://dev.classmethod.jp/articles/route-53-zone-apex-s3-redirect/)
 

Step:

S3:

- 1. S3 バケットを Zone Apex の名前で作成する (`lafoglia.jp` とか)
- 2. 作成したバケットのプロパティで、`静的ウェブホスティング` を有効にする (`http://lafoglia.jp.s3-website-ap-northeast-1.amazonaws.com`)
- 3. `ホスティングタイプ` を `オブジェクトのリクエストをリダイレクトする` で作成し、リダイレクト先を設定する (`www.lafoglia.jp` とか。 '/' を最後につけないこと)

Route 53:

- 1. レコード作成し、`S3ウェブエンドポイントへのエイリアス` で、 リージョンを選択する。
- 2. 作成した S3 を選ぶ
- 3. `A` レコードで作成する 