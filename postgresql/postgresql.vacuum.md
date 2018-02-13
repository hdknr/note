
## 最近のVACUUM

~~~sql
SELECT relname, n_live_tup, n_dead_tup, last_vacuum, last_autovacuum, last_analyze, last_autoanalyze
FROM pg_stat_all_tables
WHERE schemaname = 'public'
ORDER BY relname
~~~

自動vacuum:

~~~sql
SELECT n_live_tup,n_dead_tup,schemaname, relname,last_vacuum,last_autovacuum
FROM pg_stat_all_tables
WHERE n_dead_tup != 0 AND schemaname = 'public'
~~~


## 記事

- [Postgresql サーバを移行したらAUTO VACUUM が実行されず、データベースが肥大化した時の話](https://qiita.com/seikoudoku2000/items/e49a321182b5f91b86fe)
