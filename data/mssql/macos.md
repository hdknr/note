# Mac

## FreeTDS

- [Connecting to SQL Server from Mac OSX · mkleehammer/pyodbc Wiki](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX)
- [Install FreeTDS, unixODBC and pyodbc on OS X](https://gist.github.com/Bouke/10454272)

~~~bash
$ brew update
$ brew install unixodbc freetds
.
~~~

~~~bash
$ which tsql
/usr/local/bin/tsql

$ which isql
/usr/local/bin/isql
~~~


## 設定

### /usr/local/etc/odbcinst.ini

FreeTDSも登録する:

~~~bash
$ vi /usr/local/etc/odbcinst.ini
~~~

~~~ini
[ODBC Driver 17 for SQL Server]
Description=Microsoft ODBC Driver 17 for SQL Server
Driver=/usr/local/lib/libmsodbcsql.17.dylib
UsageCount=2

[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/local/lib/libtdsodbc.so
Setup=/usr/local/lib/libtdsodbc.so
FileUsage = 1
~~~


pyodbc: `Error: ('01000', "[01000] [unixODBC][Driver Manager]Can't open lib 'MDBTools' : file not found (0) (SQLDriverConnect)")`:

- isql はいけるのに
- isql は /etc をみているが、 pyodbc が /usr/local/etc をみている！ (`Homebrew` ?)


### `/etc/odbcinst.ini`

macOS(Homebrew)の場合、`/etc/odbcinst.ini` は ** 必須 **


~~~bash
$ sudo cp /usr/local/etc/odbcinst.ini /etc
Password:
~~~


