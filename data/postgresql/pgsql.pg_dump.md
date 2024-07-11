# pg_dump コマンド

## DDL 出力 (`-s`)

```bash
pg_dump -h test-trsm9lbtx88f.cluster-ro-c3imw8wgwmji.us-west-2.rds.amazonaws.com  -U postgresql -d rag -p 3306 -s >  /tmp/rag-ddl.sql
```
