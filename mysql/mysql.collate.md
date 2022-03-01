# 確認

## SHOW TABLE STATUS FROM

~~~
mysql> SHOW TABLE STATUS FROM apps_alpha where Name like 'auth%';
+----------------------------+--------+---------+------------+-------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
| Name                       | Engine | Version | Row_format | Rows  | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time | Check_time | Collation       | Checksum | Create_options | Comment |
+----------------------------+--------+---------+------------+-------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
| auth_group                 | InnoDB |      10 | Compact    |    21 |            780 |       16384 |               0 |        16384 |  11534336 |             33 | 2016-05-13 07:40:37 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
| auth_group_permissions     | InnoDB |      10 | Compact    |    28 |            585 |       16384 |               0 |        49152 |  11534336 |             97 | 2016-05-13 07:40:37 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
| auth_permission            | InnoDB |      10 | Compact    |   802 |            122 |       98304 |               0 |        81920 |  11534336 |            934 | 2016-05-13 07:40:37 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
| auth_user                  | InnoDB |      10 | Compact    | 37081 |            184 |     6832128 |               0 |      1589248 |  11534336 |          37056 | 2016-05-13 07:40:37 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
| auth_user_groups           | InnoDB |      10 | Compact    | 74353 |             35 |     2637824 |               0 |      6864896 |  11534336 |          73618 | 2016-05-13 07:40:37 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
| auth_user_user_permissions | InnoDB |      10 | Compact    |     3 |           5461 |       16384 |               0 |        49152 |  11534336 |             19 | 2016-05-13 07:40:37 | NULL        | NULL       | utf8_general_ci |     NULL |                |         |
+----------------------------+--------+---------+------------+-------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-----------------+----------+----------------+---------+
6 rows in set (0.02 sec)

~~~

## SHOW FULL COLUMNS FROM

~~~
mysql> SHOW FULL COLUMNS FROM auth_user where Field like 'username';                                                                                                             
+----------+-------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
| Field    | Type        | Collation       | Null | Key | Default | Extra | Privileges                      | Comment |
+----------+-------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
| username | varchar(30) | utf8_general_ci | NO   | UNI | NULL    |       | select,insert,update,references |         |
+----------+-------------+-----------------+------+-----+---------+-------+---------------------------------+---------+
1 row in set (0.00 sec)

~~~


## 変更

~~~sql
alter table <some_table> convert to character set utf8 collate utf8_unicode_ci;
~~~


## charset

~~~mysql
mysql> show variables like "chara%";

+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)
~~~

## SHOW TABLE STATUS where name like 'TABLE_NAME'



## utf8mb4_0900_ai_ci

- [MySQL 8.0の照合順序で標準になった「utf8mb4_0900_ai_ci」とは](https://qiita.com/seltzer/items/8b5d8a61591e72715d5b)
- [MySQL8.0: 日本語のutf8bm4のCollation(文字照合順)](https://dev.mysql.com/blog-archive/mysql-8-0-1-japanese-collation-for-utf8mb4-ja_jp/)


