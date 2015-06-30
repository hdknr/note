## 指定したパターンのファイルを除外

- [複数のディレクトリ除外](https://gist.github.com/kiyotune/3825822)

```
$ sudo find . -type f -name "*~" -prune -o -name "*" -exec grep -H jquery.js {} \;
```

```
$ sudo find . -type f \( -name "*~" -o -name "*bk" \) -prune -o -name "*" -exec grep -H jquery.js {} \;
```

- .svn を除外

```
find ../ -name .svn -prune -o -type f -name "*" -exec grep -H error404 {} \;
```

## ファイルの拡張子一覧
- bash の置換, `${FILE##*.}` を使う。

```
$ find . -type f -print | while read FILE; do  echo "${FILE##*.}"; done | sort |uniq

conf
html
js
php
sh
sql
txt
```

