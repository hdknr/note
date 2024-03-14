# snowflake


- https://www.snowflake.com/?lang=ja

- [RedshiftとSnowflakeの比較：6つの主な相違点](https://www.integrate.io/jp/blog/redshift-vs-snowflake-difference-ja/)


## 構成

| レイヤ               | name     | 内容                                              |
| -------------------- | -------- | ------------------------------------------------- |
| ストレージ層         | Storage  | Snowflakeが保持しているデータが置かれているレイヤ |
| コンピューティング層 | Compute  | データ処理(クエリ)を実行                          |
| サービス層           | Services | システム管理                                      |

システム管理:

1. セキュリティ
2. ユーザセッション
3. メタデータ
4.  SQL最適化
5. トランザクション管理


## キャッシュ

1. クエリリザルトキャッシュ (再利用できるクエリ結果)
2. メタデータキャッシュ (メタデータ(行数, Max/Min etc))
3. ウェアハウスキャッシュ (データのキャッシュ)



## 資料

- [【Snowflake】Snowflake ～ 基礎知識編 ～](https://dk521123.hatenablog.com/entry/2021/11/02/130111)
- [【Snowflake】Snowflake ～ 入門編 / Hello world ～](https://dk521123.hatenablog.com/entry/2021/11/22/212520)