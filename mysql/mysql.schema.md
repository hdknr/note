# スキーマ情報を調べる

~~~sql
mysql> desc information_schema.COLUMNS ;
+--------------------------+---------------------+------+-----+---------+-------+
| Field                    | Type                | Null | Key | Default | Extra |
+--------------------------+---------------------+------+-----+---------+-------+
| TABLE_CATALOG            | varchar(512)        | NO   |     |         |       |
| TABLE_SCHEMA             | varchar(64)         | NO   |     |         |       |
| TABLE_NAME               | varchar(64)         | NO   |     |         |       |
| COLUMN_NAME              | varchar(64)         | NO   |     |         |       |
| ORDINAL_POSITION         | bigint(21) unsigned | NO   |     | 0       |       |
| COLUMN_DEFAULT           | longtext            | YES  |     | NULL    |       |
| IS_NULLABLE              | varchar(3)          | NO   |     |         |       |
| DATA_TYPE                | varchar(64)         | NO   |     |         |       |
| CHARACTER_MAXIMUM_LENGTH | bigint(21) unsigned | YES  |     | NULL    |       |
| CHARACTER_OCTET_LENGTH   | bigint(21) unsigned | YES  |     | NULL    |       |
| NUMERIC_PRECISION        | bigint(21) unsigned | YES  |     | NULL    |       |
| NUMERIC_SCALE            | bigint(21) unsigned | YES  |     | NULL    |       |
| CHARACTER_SET_NAME       | varchar(32)         | YES  |     | NULL    |       |
| COLLATION_NAME           | varchar(32)         | YES  |     | NULL    |       |
| COLUMN_TYPE              | longtext            | NO   |     | NULL    |       |
| COLUMN_KEY               | varchar(3)          | NO   |     |         |       |
| EXTRA                    | varchar(27)         | NO   |     |         |       |
| PRIVILEGES               | varchar(80)         | NO   |     |         |       |
| COLUMN_COMMENT           | varchar(1024)       | NO   |     |         |       |
+--------------------------+---------------------+------+-----+---------+-------+
19 rows in set (0.00 sec)
~~~

~~~sql
SELECT * 
	FROM information_schema.COLUMNS 
WHERE
 	TABLE_NAME = 'summaries' AND
 	TABLE_SCHEMA = database();
~~~

- データタイプ

~~~sql
SELECT 
	DATA_TYPE  
FROM 
	information_schema.COLUMNS 
WHERE
   TABLE_NAME = 'summaries' AND
   TABLE_SCHEMA = database() AND
   COLUMN_NAME = 'id';

+-----------+
| DATA_TYPE |
+-----------+
| int       |
+-----------+
1 row in set (0.00 sec)

~~~

