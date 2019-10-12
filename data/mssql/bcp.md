# bcp

## CSV に落とす

~~~bash
C:¥> bcp "SELECT * FROM Database.dbo.Table" queryout C:\Test.csv -c -t, -T -S .\SQLEXPRESS
.
~~~
