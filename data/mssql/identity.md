# IDENTITY

- [SQL ServerのIDENTITY　自動採番する](https://sql-oracle.com/sqlserver/?p=1087)

~~~
    IDENTITY(開始番号, 増加数)
~~~


~~~sql
ALTER TABLE dbo.T10_JUCYU add id int IDENTITY(1, 1) NOT NULL;
~~~