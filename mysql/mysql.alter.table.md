## カラム削除

~~~mysql
alter table archives_bulletin drop column issued_year_month
~~~

## カラム追加

~~~mysql
alter table smtp_message add created_at datetime default NULL;
alter table smtp_message add updated_at datetime ;
~~~

## カラム長変更

~~~mysql
ALTER TABLE flier_address MODIFY address VARCHAR(100);
~~~


## NULL を許容

~~~mysql
ALTER TABLE archives_studentexchange  MODIFY major VARCHAR(50) null default null;
~~~
