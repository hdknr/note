# psql

- [PostgreSQLとMySQLで、僕がよく使うシステムコマンドのメモ](http://qiita.com/tamano/items/be43de7bb733ad38362c)

## インストール

```sh
brew update
brew install libpq
```

```txt
If you need to have libpq first in your PATH, run:
  echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.zshrc

For compilers to find libpq you may need to set:
  export LDFLAGS="-L/usr/local/opt/libpq/lib"
  export CPPFLAGS="-I/usr/local/opt/libpq/include"

For pkg-config to find libpq you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/libpq/lib/pkgconfig"
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
