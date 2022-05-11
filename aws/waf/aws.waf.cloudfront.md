# クラウドフロント

- aws_wafv2_web_acl を aws.virgina で作ること
- つくったリソースの `arn` を CloudFrontに設定する

~~~tf
resource {
    web_acl_id = var.web_acl.arn
}
~~~



## 資料

- [terraformで Cloudfront に WAF2 を使って特定のパスやAPIにIP制限をする](https://qiita.com/eretica/items/6e9516ea8dd8ba073347)
- [AWS WAF + CloudFront + S3 でIP制限をかけたホスティングサイトをサーバレスで組み立てる](https://techblog.timers-inc.com/entry/waf-cloudfront-s3)
- [AWS WAFにてデフォルトAllowで「特定のIPリスト以外をBlock」する [Terraform]](https://dev.classmethod.jp/articles/allow-by-default-and-block-ips-except-whitelist/)
- [AWS WAFを利用してCloudFrontのELBオリジンへ直接アクセスを制限してみた](https://dev.classmethod.jp/articles/restrict-elb-origin-awswaf/)
- [Terraformで AWS WAF を作成したが、リソースがAWSコンソールに表示されない問題](https://www.ikkitang1211.site/entry/2020/05/19/222910)
- [AWSのWAFとCloudFrontをTerraformで導入してみました ](https://zenn.dev/bun913/articles/waf-cloudfront-by-terraform)
- [TerraformでAWS WAFを基礎から学ぶ(ロギング編)](https://qiita.com/neruneruo/items/ad886c2b47ff6af37c91)
