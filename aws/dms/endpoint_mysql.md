# MySQL エンドポイント

## MySQL: CDC(Change Data Capture)

- [AWS Database Migration Service による Change Data Capture: 前編](https://ts223.hatenablog.com/entry/cdc-rds-bq/part1)
- [AWS Database Migration Service による Change Data Capture: 後編](https://ts223.hatenablog.com/entry/cdc-rds-bq/part2)
- https://github.com/tosh2230/cdc-rds-bq/tree/main/templates

- [AWS DatabaseMigrationService での DB 移行構築ハンズオン](https://qiita.com/i3no29/items/73363a7e1ca1c99000f8)

## RDS MySQL

- [AWS DMS のソースとして AWS が管理する MySQL 互換データベースの使用](https://docs.aws.amazon.com/ja_jp/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.AmazonManaged)

  - バイナリログ(`binlog_format` == `ROW`)
  - `binlog_row_image` == `Full`
  - `binlog_checksum` == `NONE`
