
- [13.5 String Functions](http://dev.mysql.com/doc/refman/5.7/en/string-functions.html)

# REPLACE

## 空白を無視してSELECT

~~~sql
select * from table
where replace(replace(key,' ',''),'　','') like '%検索文字列%'
~~~
