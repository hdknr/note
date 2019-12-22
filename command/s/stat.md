# stat コマンド

## ファイルの最終更新日

~~~bash
LASTDT=$(date -d @$( stat -c %Y access.log ) +%Y-%m-%d)
~~~
