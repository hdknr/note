# hostname

~~~sql
SELECT @@hostname;
~~~~

~~~sql
SHOW VARIABLES LIKE 'hostname';
~~~

## RDS: プロンプトを変える

[PROMPT \u@\h >\_`](mysql.prompt.md)

~~~sql
MySQL [db_server]> PROMPT \u@\h >\_

PROMPT set to '\u@\h >\_'
db_server@mycloud-prod-ffs-db-instance.caxxpg8dbdd0.ap-northeast-1.rds > 
~~~~