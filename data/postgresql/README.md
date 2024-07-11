- [#77](https://github.com/hdknr/scriptogr.am/issues/77)
- [psql](postgresql.psql.md)

## パフォーマンス

- [pg_stat_statements](postgresql.pg_stat_statements.md)

現在の設定値の値:

```sql
SELECT name,setting,unit FROM pg_settings;
```

記事:

- [Postgres の RDS チューニング ](http://qiita.com/awakia/items/9981f37d5cbcbcd155eb)

## メモ

- http://dalibo.github.io/powa/
- https://blog.dbi-services.com/monitoring-tools-for-postgresql-powa/
- [AWS: Amazon RDS のベストプラクティス](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)

## [パスワードファイル](https://www.postgresql.jp/docs/9.2/libpq-pgpass.html)(`~/.pgpass`)

```
hostname:port:database:username:password
```

- `:` はバックスラッシュでクオートする。
- 600 に `chmod` する

以下のコマンドでパスワードの入力なしで利用可能:

```
psql -h hostname -p port -d database -U username
```
