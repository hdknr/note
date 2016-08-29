## 行の削除

### 行番号

- 5 行目を表示

~~~bash
$ sed -n 5P source.txt
$ awk 'NR==5' source.txt
~~~

- 1-5行目を削除

```
$ sed -e "5,10d" source.txt
```

- 最終行を削除

~~~bash
$ sed '$d'
~~~

[how to use sed to remove last n lines of a file](http://stackoverflow.com/questions/13380607/how-to-use-sed-to-remove-last-n-lines-of-a-file)

###  パターンまで

- "DROP PROCEDURE" で始まる行まで削除

```
$ sed -e "1,/^DROP PROCEDURE/d" sql/schema.sql
```



## その他

- [BSD sed のメモ](http://qiita.com/mattintosh4/items/4e4d44016be15333af11)
