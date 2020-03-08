# Oracle

- [インストール](oracle.install)


## 起動

- [Oracleソフトウェアの停止と起動](https://docs.oracle.com/cd/E82638_01/unxar/stopping-and-starting-oracle-software.html#GUID-EFE15D61-4BDC-4A9B-B8E4-46A7325C2409)

~~~bash
$ which oraenv
/usr/local/bin/oraenv
~~~

`/etc/oratab`:

~~~bash
$ cat /etc/oratab 

orcl:/u01/app/oracle/product/11/db_1:N
~~~

~~~bash
$ source /usr/local/bin/oraenv 
ORACLE_SID = [orcl] ? 
The Oracle base for ORACLE_HOME=/u01/app/oracle/product/11/db_1 is /u01/app/oracle
~~~
