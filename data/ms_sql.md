# MS SQL Server ([#101](https://github.com/hdknr/note/issues/101))

## bcp

### CSV に落とす

~~~bash
C:¥> bcp "SELECT * FROM Database.dbo.Table" queryout C:\Test.csv -c -t, -T -S .\SQLEXPRESS
.
~~~

## FreeTDS

- [Linux PHPからSQL Serverに接続 - Qiita](https://qiita.com/arachan@github/items/026091e69e1aba7b0918)
- [LinuxからSQL ServerにODBCで接続する - Qiita](https://qiita.com/arachan@github/items/5863c945dbe7507975d8)
- [sql server - How to install freetds in Linux? - Stack Overflow](https://stackoverflow.com/questions/33341510/how-to-install-freetds-in-linux)
- [ODBC, unixODBC, FreeTDS - Qiita](https://qiita.com/oyakata@github/items/2f8364553cbbef2ac4c2)

Site:

- [django-pyodbc](https://github.com/lionheart/django-pyodbc/)
- [django-pyodbc-azure](https://github.com/michiya/django-pyodbc-azure)
- [FreeTDS](http://www.freetds.org/)
- [unixODBC](http://www.unixodbc.org/)

### Ubuntu

- [sql server - How to install freetds in Linux? - Stack Overflow](https://stackoverflow.com/questions/33341510/how-to-install-freetds-in-linux)

~~~bash
$ sudo apt update && sudo apt install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc -y
.

$ dpkg -L freetds-common | grep etc
/etc
/etc/freetds
.

$ tree /etc/freetds/

/etc/freetds/
└── freetds.conf

~~~

~~~bash
$ dpkg -L tdsodbc | grep lib
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/odbc
/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
...

$ sudo tree /usr/lib/x86_64-linux-gnu/odbc
/usr/lib/x86_64-linux-gnu/odbc
├── libesoobS.so
├── libmimerS.so
├── libnn.so
├── libodbcdrvcfg1S.so
├── libodbcdrvcfg2S.so
├── libodbcminiS.so
├── libodbcmyS.so
├── libodbcnnS.so
├── libodbcpsqlS.so
├── libodbctxtS.so
├── liboplodbcS.so
├── liboraodbcS.so
├── libsapdbS.so
├── libtdsS.so
└── libtdsodbc.so

~~~

~~~bash
$ dpkg -L odbcinst | grep ini
/etc/odbc.ini
.
~~~

~~~bash
$ sudo vim /etc/odbcinst.ini
...
~~~

~~~ini
[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
Setup=/usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
~~~



### Mac

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

## tsql

~~~bash
$ echo "SELECT @@VERSION" |  tsql -S MYMSSQL -U superuser -P password -o qfh
Microsoft SQL Server 2017 (RTM-CU13-OD) (KB4483666) - 14.0.3049.1 (X64) 
	Dec 15 2018 11:16:42 
	Copyright (C) 2017 Microsoft Corporation
	Express Edition (64-bit) on Windows Server 2016 Datacenter 10.0 <X64> (Build 14393: ) (Hypervisor)
~~~

## T-SQL

- [Get list of databases from SQL Server - Stack Overflow](https://stackoverflow.com/questions/147659/get-list-of-databases-from-sql-server)
