# AWS: ACM(Amazon Web Services Certificate Manager) での証明書

## CloudFront

- `us-east-1` の ACM に設定する必要があります

## 外部取得証明書のインポート

- `PEM` 形式の証明書をインポート可能
- [AWS Certificate Manager への証明書のインポート - AWS Certificate Manager](https://docs.aws.amazon.com/ja_jp/acm/latest/userguide/import-certificate.html)
- [証明書のインポート - AWS Certificate Manager](https://docs.aws.amazon.com/ja_jp/acm/latest/userguide/import-certificate-api-cli.html)

## [FAQ](https://aws.amazon.com/jp/certificate-manager/faqs/)

- 証明書に最大10個のドメイン名を設定できる


## [コマンド](https://docs.aws.amazon.com/cli/latest/reference/acm/index.html#cli-aws-acm)(`acm`)

[証明書一覧](https://docs.aws.amazon.com/cli/latest/reference/acm/list-certificates.html)(`list-certificate`):

~~~bash
aws acm list-certificates --profile cloud --region us-east-1 | jq ".CertificateSummaryList[].CertificateArn" 
"arn:aws:acm:us-east-1:726544500144:certificate/d6a49ff5-d8af-490b-82a9-1c9260a7099b"
"arn:aws:acm:us-east-1:726544500144:certificate/b40a6989-bd5d-47b2-9fd4-ba94429afb65"
"arn:aws:acm:us-east-1:726544500144:certificate/118845ca-78dc-4b66-bb92-b4489ac91c52"
~~~

ドメイン指定で、jqフィルタリングする:

~~~bash
... | jq '.CertificateSummaryList[] | select(.DomainName == "www.cloud.com") | .CertificateArn'
~~~



[内容](https://docs.aws.amazon.com/cli/latest/reference/acm/describe-certificate.html)(`describe-certificate`):

~~~bash
% aws acm describe-certificate --certificate-arn $CERT --profile cloud --region us-east-1
~~~

jqでドメイン名の一覧を取得:

~~~bash
... | jq ".Certificate.DomainValidationOptions[].DomainName"
~~~
