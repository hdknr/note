# SSLと証明書

- [CloudFront で SSL/TLS の証明書を使用するための要件 - Amazon CloudFront](https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html)

## ACMリージョン

- バージニア北部リージョン(`us-east-1`)

## キーサイズは 1024 / 2048 bit の２択

- [パブリックキーのサイズ](https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html#https-requirements-size-of-public-key)
- ACMは 4096bit まで行くのに....

## 証明書タイプ

- ドメイン認証証明書
- 拡張認証 (EV) 証明書
- 高保証証明書
- ワイルドカード証明書 (*.example.com)
- 主体者別名 (SAN) 証明書 (example.com および example.net)
