## time_zone

- [サーバーがUTCなのでMySQLのタイムゾーンが気になって調べた](http://bit.ly/2bkl0vs)

~~~sql
mysql> SELECT @@global.system_time_zone, @@global.time_zone, @@session.time_zone;
+---------------------------+--------------------+---------------------+
| @@global.system_time_zone | @@global.time_zone | @@session.time_zone |
+---------------------------+--------------------+---------------------+
| UTC                       | SYSTEM             | SYSTEM              |
+---------------------------+--------------------+---------------------+
1 row in set (0.00 sec)
~~~

## now()

~~~sql
mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2016-08-26 07:26:32 |
+---------------------+
~~~


## RFC 5322 compliant Message-ID


~~~py
msgid = '<%s.%s.%s%s@%s>' % (utcdate, pid, randint, idstring, domain)
~~~

utcdate:

~~~sql
mysql> select UNIX_TIMESTAMP(now());
+-----------------------+
| UNIX_TIMESTAMP(now()) |
+-----------------------+
|            1472197567 |
+-----------------------+
~~~

randint:

~~~sql
mysql> select id, ROUND( RAND() * 50000 + 100000 ) from auth_user limit 10;
+-------+----------------------------------+
| id    | ROUND( RAND() * 50000 + 100000 ) |
+-------+----------------------------------+
| 37054 |                           134782 |
|     8 |                           132310 |
|     9 |                           107205 |
|    10 |                           139094 |
|    11 |                           123857 |
|    12 |                           102001 |
|    13 |                           138435 |
|    14 |                           136173 |
| 11149 |                           115561 |
|    15 |                           119285 |
+-------+----------------------------------+
~~~

連結:

~~~sql
mysql> select concat(CONVERT(id, CHAR), '.', CONVERT(ROUND( RAND() * 50000 + 100000 ), CHAR)) as V from auth_user limit 10;
+--------------+
| V            |
+--------------+
| 37054.123192 |
| 8.118800     |
| 9.124425     |
| 10.115727    |
| 11.105359    |
| 12.129613    |
| 13.131989    |
| 14.121104    |
| 11149.109553 |
| 15.134454    |
+--------------+
~~~
