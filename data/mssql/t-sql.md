# T-SQL

- [Get list of databases from SQL Server - Stack Overflow](https://stackoverflow.com/questions/147659/get-list-of-databases-from-sql-server)

## データベース

### データベース一覧

~~~sql
USE AdventureWorks2012;  
GO  
SELECT name, database_id, create_date  FROM sys.databases ;  
GO  
~~~

### 現在のデータベース

~~~sql
SELECT db_name()
~~~

## テーブル

### テーブル一覧

- [SQL Server テーブル一覧取得いろいろ - Qiita](https://qiita.com/qsuke92/items/51a85a58ac91782ee528)
