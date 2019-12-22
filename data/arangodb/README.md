# ArangoDB

- [インストール](arangodb.install.md)
- [arangosh](tools/arangosh.md)
- [チュートリアル](https://www.tutorialspoint.com/arangodb/index.htm)
- [AQL](aql.md)

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

## 記事

- [Say Hi To ArangoDB Oasis: A Fully-Managed Multi-Model Database Service](https://www.arangodb.com/2019/11/arangodb-oasis-a-fully-managed-multi-model-database-service/)
