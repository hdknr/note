- [Enabling pg_stat_statements](https://pganalyze.com/docs/install/amazon_rds/01_configure_rds_instance)
- [F.32. pg_stat_statements
](https://www.postgresql.jp/document/9.1/html/pgstatstatements.html)

## pg_stat_statementsについて

- SQLのプロファイリングを行うビュー
- SQLごとに以下の情報を取得できます。
- total_time は複数回実行した累積値ですので、calls で割ると「1回あたりの平均時間」が計算できます。

Name   | Description
-------|--------------------------
userid | SQLを実行したユーザのID
dbid   | データベースのID
query  | SQLのクエリテキスト
calls  | 実行回数
total_time | 実行時間 (単位=秒 / 精度=マイクロ秒)
rows | 処理行数 (返却行数 or 影響行数)


## モジュールのインストール

- ”パラメータグループ"を作成
- 設定変更


Name	                   |Value             |
-------------------------|-----------------|----------
pg_stat_statements.track |ALL               |
shared_preload_libraries |pg_stat_statements|
track_activity_query_size|2048	            |

- 有効化

~~~sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
~~~


## 確認


- `\x` オプションで列を展開する

~~~sql
=# \x
=# SELECT query, calls, total_time, rows
     FROM pg_stat_statements ORDER BY total_time DESC LIMIT 3;
-[ RECORD 1 ]------------------------------------------------------------
query      | UPDATE branches SET bbalance = bbalance + $1 WHERE bid = $2;
calls      | 3000
total_time | 35.9654100
rows       | 3000
-[ RECORD 2 ]------------------------------------------------------------
query      | UPDATE tellers SET tbalance = tbalance + $1 WHERE tid = $2;
calls      | 3000
total_time | 34.7969816
rows       | 3000
-[ RECORD 3 ]------------------------------------------------------------
query      | UPDATE accounts SET abalance = abalance + $1 WHERE aid = $2;
calls      | 3000
total_time | 0.6603847
rows       | 3000
~~~
