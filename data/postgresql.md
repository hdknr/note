- OSX/Homebrew

~~~bash
$ brew install postgresql
~~~

- Python

~~~bash
$ pip install psycopg2
~~~

## パスワード

### ~/.pgpass

- パスワードファイル

~~~
$ cat ~/.pgpass

localhost:5432:postgres:psqluser:psqluser
~~~

- w (パスワード指定しない) でログイン。
- ユーザー名とホストは必須。

~~~
$ psql -U psqluser -w postgres -h localhost
psql (9.3.10)
SSL connection (cipher: DHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

postgres=> \q
~~~

### 変更

- [Postgresでパスワードを忘れた場合の対策](http://qiita.com/satomin/items/0e481af2490603a271fe)
- [Amazon RDSのマスターパスワードを忘れた場合の対処法](http://qiita.com/biatunky/items/c9bc8a283fb1ceb94258)

## データベース作成権限

- [PostgreSQL8でpostgresユーザ以外のユーザにcreatedbを実行させる方法](http://nobuneko.com/blog/archives/2011/07/postgresql8postgrescreatedb.html)

- `postgres` ユーザーに sudo したほうがいい


## Ansible

- [ansibleでpostgresqlインストール](http://qiita.com/kitaro_tn/items/04aa7279c17be8b9b0ed)
