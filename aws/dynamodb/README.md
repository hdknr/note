## Python

- [DynamoDBの高レベルクライアント「PynamoDB」が良かった](https://qiita.com/ykarakita/items/2bb4c951cbcb8771c3af)

## S3にエクスポート

`ポイントインタイムリカバリ (PITR)` を有効にしておくこと(`バックアップ` タブから設定)

```bash
aws --profile connect  \
    dynamodb export-table-to-point-in-time  \
    --table-arn arn:aws:dynamodb:ap-northeast-1:875050331796:table/ContactTable \
    --s3-bucket  helpdesk-admin-state \
    --s3-prefix temp/  \
    --export-format DYNAMODB_JSON
```
