# psql

- [PostgreSQLとMySQLで、僕がよく使うシステムコマンドのメモ](http://qiita.com/tamano/items/be43de7bb733ad38362c)

## インストール

```
brew update
brew install libpq
```

## テーブル一覧

~~~
\d
~~~

~~~bash
$ echo "\\d" | DJ dbshell | grep auth

public   | auth_group                           | table    | ecoroute
...
~~~

## テーブル定義

~~~
echo "\\d drivers_activity" | DJ dbshell
~~~

## 古いレコード

~~~
$ echo "select count(*) from drivers_activity" | DJ dbshell

count  
---------
4469774
(1 row)
~~~

~~~sql
select count(*) from drivers_activity where created_at <= cast(now() - interval '60 days' as timestamp);
~~~

~~~bash
echo "select count(*) from drivers_activity where created_at <= cast(now() - interval '300 days' as timestamp);" | DJ dbshell

count  
---------
4465542
(1 row)
~~~
