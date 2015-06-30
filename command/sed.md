## 行の削除

### 行番号

- 1-5行目を削除

```
$ sed -e "5,10d" source.txt
```

###  パターンまで

- "DROP PROCEDURE" で始まる行まで削除

```
$ sed -e "1,/^DROP PROCEDURE/d" sql/schema.sql
```