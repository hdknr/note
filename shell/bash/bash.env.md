# env

## .env ファイルを使う


呼び出し:

~~~bash
$ env $(cat .env | xargs) ./main.sh
~~~

スクリプト内:

~~~bash
#!/bin/bash
set -a; source .env; set +a
echo $DB_HOST
~~~


## 記事

- [set - Set or unset values of shell options and positional parameters.](https://linuxcommand.org/lc3_man_pages/seth.html)
- [.envを扱いたいみなさん](https://qiita.com/ryo0301/items/3a6ccdd4e4cb55f82d4a)
- [mihow/load_dotenv.sh](https://gist.github.com/mihow/9c7f559807069a03e302605691f85572)


