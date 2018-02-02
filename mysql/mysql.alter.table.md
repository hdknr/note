## カラム

### カラム削除

~~~mysql
alter table archives_bulletin drop column issued_year_month
~~~

### カラム追加

~~~mysql
alter table smtp_message add created_at datetime default NULL;
alter table smtp_message add updated_at datetime ;
~~~

### カラム長変更

~~~mysql
ALTER TABLE flier_address MODIFY address VARCHAR(100);
~~~


### NULL を許容

~~~mysql
ALTER TABLE archives_studentexchange  MODIFY major VARCHAR(50) null default null;
~~~


## インデックス

### 外部キー削除

~~~mysql
ALTER TABLE products_product drop FOREIGN KEY products_product_wholesale_id_8b1f92cc_fk_products_wholesale_id;
~~~

### インデックス削除

~~~mysql
ALTER TABLE partners_shippingfee DROP INDEX partners_shippingfee_company_id_e85a3531_uniq ;
~~~

## テーブル

### 削除

外部キー制約を無視する:

~~~mysql
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE users;
SET FOREIGN_KEY_CHECKS=1;
~~~
