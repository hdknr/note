# ndjsonの書き込み

- https://github.com/ndjson/ndjson-spec

## 設定

`epm_server` ユーザーに書き込み件を設定:

~~~sql
GRANT FILE ON *.* TO 'epm_server'@'%';
~~~

my.cnfで書き込み可能にする:

~~~ini
[mysqld]
secure-file-priv = ""
~~~

ブランクを指定すると任意のパスが可能 (mysqld の権限による)

## 実行

SQL:

~~~sql
SELECT 
    JSON_OBJECT(
        "id", id, 
        "outstanding_invoice_amount", outstanding_invoice_amount
    ) as unload
INTO OUTFILE '/tmp/dump.json'
FROM    
    sales_clearing;
~~~


~~~bash
% cat /tmp/dump.sql| mysql --defaults-file=../.secrets/local.ini epm_server 
% cat /tmp/dump.json 
~~~

~~~json
{"id": 448, "outstanding_invoice_amount": -550000}
{"id": 449, "outstanding_invoice_amount": 0}
{"id": 450, "outstanding_invoice_amount": -1100000}
~~~


