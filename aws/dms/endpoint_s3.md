# S3 エンドポイント

## ポリシー

- [AWS Database Migration Service のターゲットに Amazon S3 を使用する](https://docs.aws.amazon.com/ja_jp/dms/latest/userguide/CHAP_Target.S3.html)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:DeleteObject", "s3:PutObjectTagging"],
      "Resource": ["arn:aws:s3:::buckettest2/*"]
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::buckettest2"]
    }
  ]
}
```

- [DMS を使って SQL Server のデータを S3 に出力する](https://dev.classmethod.jp/articles/dms-sql-server-s3/)
- [[AWS]AWS DMS で Aurora MySQL を S3 にデータ移行](https://zenn.dev/third_tech/articles/002ca4e4a9ac98)
- [AWS DMS の使用時に Amazon S3 エンドポイントの接続テスト障害をトラブルシューティングするにはどうすればよいですか。](https://repost.aws/ja/knowledge-center/dms-connection-test-fail-s3)

## Parquet 書式

- [Using Apache Parquet to store Amazon S3 objects](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Parquet)
- [AWS DMS を使用して Parquet 形式で Amazon S3 にデータを移行する方法を教えてください。](https://repost.aws/ja/knowledge-center/dms-s3-parquet-format)
- [Announcing the support of Parquet data format in AWS DMS 3.1.3](https://aws.amazon.com/jp/blogs/database/announcing-the-support-of-parquet-data-format-in-aws-dms-3-1-3/)

### Parquet S3 設定

[Endpoint settings when using Amazon S3 as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring)

```yaml
S3Settings:
  BucketName:
    Fn::ImportValue: !Sub ${S3Stack}-S3BucketName
  ServiceAccessRoleArn:
    Fn::ImportValue: !Sub ${S3Stack}-DmsS3EndpointAccessRoleArn
  EncryptionMode: SSE_S3
  DataFormat: parquet
  ParquetVersion: PARQUET_2_0
  CompressionType: GZIP
  EnableStatistics: true
  EncodingType: rle-dictionary
  CdcMaxBatchInterval: 60
  DataPageSize: 1024000
  RowGroupLength: 10024
  DictPageSizeLimit: 1024000
  AddColumnName: true
  TimestampColumnName: CdcTimestamp
  DatePartitionEnabled: true
  DatePartitionSequence: YYYYMMDD
  DatePartitionDelimiter: SLASH
```

## pyarrow で読み込み

```bash
pip install pyarrow
```

```py
import pyarrow.parquet as pq

df = pq.read_table("/Users/hdknr/Downloads/20240327-014303888.parquet").to_pandas()
```
