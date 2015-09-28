# MS SQL Server

## bcp


### CSV に落とす

~~~bash
C:¥> bcp "SELECT * FROM Database.dbo.Table" queryout C:\Test.csv -c -t, -T -S .\SQLEXPRESS
~~~

## Linux

- [django-pyodbc](https://github.com/lionheart/django-pyodbc/)
- [django-pyodbc-azure](https://github.com/michiya/django-pyodbc-azure)
- [FreeTDS](http://www.freetds.org/)
- [unixODBC](http://www.unixodbc.org/)
