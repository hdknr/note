# [Amazon CloudFront](https://aws.amazon.com/jp/cloudfront/)

- [ドキュメント](https://docs.aws.amazon.com/ja_jp/cloudfront/?id=docs_gateway)
- [Qiita](https://qiita.com/tags/cloudfront)

## 概念

Origin(オリジン):

- コンテンツの配信元となるサーバ

Edge(エッジ):

- CloudFrontのサーバーのこと(負荷分散されています)

デフォルトルートオブジェクト:

- デフォルトページ (`index.html` など)

## トピック

- [Wordpress](wordpress.md)
- [SSL/証明書](ssl.md)
- [ヘッダー送信](Cache_Based_on_Selected_Request_Headers)

## [ガイド](https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

トピック:

- コンテンツを配信するように CloudFront を設定する方法
- CloudFront ユースケース
- CloudFront がコンテンツを配信する方法
- CloudFront エッジサーバーの場所と IP アドレス範囲
- CloudFront へのアクセス
- Amazon CloudFront の使用を開始する方法
- AWS Identity and Access Management
- CloudFront 料金表

## API

- [Amazon CloudFront API Reference](https://docs.aws.amazon.com/ja_jp/cloudfront/latest/APIReference/Welcome.html)
- [awscli > cloudfront](awscli.cloudfront.md)

## 記事

- [Lambda@Edge Design Best Practices - Networking & Content Delivery](https://aws.amazon.com/jp/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/)
- [Resizing Images with Amazon CloudFront & Lambda@Edge - AWS CDN Blog - Networking & Content Delivery](https://aws.amazon.com/jp/blogs/networking-and-content-delivery/resizing-images-with-amazon-cloudfront-lambdaedge-aws-cdn-blog/)
