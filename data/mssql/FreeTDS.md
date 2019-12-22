# FreeTDS

- [Linux PHPからSQL Serverに接続 - Qiita](https://qiita.com/arachan@github/items/026091e69e1aba7b0918)
- [LinuxからSQL ServerにODBCで接続する - Qiita](https://qiita.com/arachan@github/items/5863c945dbe7507975d8)
- [sql server - How to install freetds in Linux? - Stack Overflow](https://stackoverflow.com/questions/33341510/how-to-install-freetds-in-linux)
- [ODBC, unixODBC, FreeTDS - Qiita](https://qiita.com/oyakata@github/items/2f8364553cbbef2ac4c2)

Site:

- [django-pyodbc](https://github.com/lionheart/django-pyodbc/)
- [django-pyodbc-azure](https://github.com/michiya/django-pyodbc-azure)
- [FreeTDS](http://www.freetds.org/)
- [unixODBC](http://www.unixodbc.org/)

Install

- [Ubuntu](ubuntu.md)
- [macOS](ubuntu.md)

## tsql コマンド

~~~bash
$ echo "SELECT @@VERSION" |  tsql -S MYMSSQL -U superuser -P password -o qfh
Microsoft SQL Server 2017 (RTM-CU13-OD) (KB4483666) - 14.0.3049.1 (X64) 
	Dec 15 2018 11:16:42 
	Copyright (C) 2017 Microsoft Corporation
	Express Edition (64-bit) on Windows Server 2016 Datacenter 10.0 <X64> (Build 14393: ) (Hypervisor)
~~~