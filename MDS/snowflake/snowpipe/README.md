# Snowpipe

[AWS DMS と Snowpipe を活用した Snowflake 用リアルタイムデータパイプラインの構築](https://zenn.dev/yohei/articles/2021-04-24-snowflake-dms-rds)


## Change Data Capture(CDC)

- RDB の変更をリアルタイムに取得して外部に転送するやり方
- Kafka
- [Debezium](https://debezium.io/)

### AWS DMS(Database Migration Service) によるCDC

![](cdc_dms.svg)