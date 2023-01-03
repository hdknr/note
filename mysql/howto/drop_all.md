# 全テーブル削除


~~~bash
echo "SET FOREIGN_KEY_CHECKS = 0;" > /tmp/clear.sql
~~~

~~~bash
echo "show tables" | mysql ... dbname | grep -v "^Tables" | while read T ; do echo "DROP TABLE IF EXISTS $T;"; done >> /tmp/clear.sql
~~~


~~~bash
echo "SET FOREIGN_KEY_CHECKS = 1;" >> /tmp/clear.sql
~~~