
## ファイルの拡張子一覧

~~~bash 
$ find html/ -type f | while read f; do echo ${f##*.}; done  | sort | uniq
~~~


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

## printf

- [find lacks the option -printf, now what?](http://stackoverflow.com/questions/752818/find-lacks-the-option-printf-now-what)

## 大きいファイルを探す

~~~bash
$find / -type f -size +10000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'
~~~

## ディレクトリのみ表示

~~~bash
$ find . -maxdepth 1 -type d
~~~

## find -exec rm in Windows

~~~bash
C:\>for /F "usebackq" %i in  (`dir /s /b *.config`) do del %i
~~~
