## 5.7 にあげるとエラー

/var/log/mysql/error.log:

~~~
2018-08-02T15:22:12.506477Z 0 [Warning] InnoDB: Table mysql/innodb_index_stats has length mismatch in the column name table_name.  Please run mysql_upgrade
~~~

### アップグレード

~~~bash 
$ mysql_upgrade  -u root -p
~~~

~~~
...
bashUpgrade process completed successfully.
Could not create the upgrade info file '/data/mysql/mysql_upgrade_info' in the MySQL Servers datadir, errno: 13
~~~

~~~bash
$ sudo mysql_upgrade  -u root -p
~~~
 

### 記事

- [MySQL5.1→5.7へアップグレード](https://qiita.com/riritea/items/31644f023ad0ab0dd0bb)