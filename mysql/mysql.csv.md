## 標準出力

~~~bash
$ echo "select * from users" | mysql -u user -p dbname | sed 's/\t/,/g'
~~~

## SQL 文

以下を実行:

~~~py
SELECT * FROM users
  INTO OUTFILE '/tmp/users.csv'
  FIELDS TERMINATED BY ','
  OPTIONALLY ENCLOSED BY '"';
~~~

だだし、セキュリティ的に問題あり:

~~~
ERROR 1290 (HY000) at line 1:
The MySQL server is running with the --secure-file-priv option
so it cannot execute this statement
~~~

secure_file_privの確認:

~~~bash
echo "SELECT @@global.secure_file_priv;" | mysql -u root -p -t
Enter password:

+---------------------------+
| @@global.secure_file_priv |
+---------------------------+
| /var/lib/mysql-files/     |
+---------------------------+
~~~

修正し、`root` (もしくは `grant file on *.* to you@localhost`) で実行すればよい：

~~~sql
SELECT * FROM users
  INTO OUTFILE '/var/lib/mysql-files/users.csv'
  FIELDS TERMINATED BY ','
  OPTIONALLY ENCLOSED BY '"';
~~~
