# ArangoDB

- [インストール](arangodb.install.md)
- [arangosh](tools/arangosh.md)
- [チュートリアル](https://www.tutorialspoint.com/arangodb/index.htm)

## 概念

|  RDB     |  ArangoDB   |
| -------- | ----------- |
| テーブル  | コレクション  |
| レコード  | ドキュメント  |
| カラム    | フィールド   | 


| RDB  | RethinkDB | MongoDB | ArangoDB |
|:--------|:---------|:---------|:---------|
| database  | database  |  database  | database  |
| table  | table  | collection  |  collection  |
| row (tuple, record)  |  document  |  document  |  document  |
| column (field, attribute)  | field |  field |  attribute  |
| primary key  |  ```id``` field |  ```_id``` field  | &bull; ```_key``` attribute<br/> &bull; ```_id = collectionName + "/" + _key``` |
