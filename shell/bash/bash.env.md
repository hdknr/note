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

## 設定

| 設定              | 内容                                                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `set -e`          | 実行されたコマンドの 1 つ が 0 でないステータスで終了した場合にスクリプトを終了させ、エラーシェルスクリプト実行時に実行内容が表示される |
| `set -n`          | スクリプト自体は実行されず、文法チェックのみ                                                                                            |
| `set -u`          | 未定義変数が参照されたときに処理を終了                                                                                                  |
| `set -o pipefail` | パイプでつないだ各コマンドの中で終了ステータスが0以外(正常終了以外)だった場合に、最後に0以外だったコマンドの終了ステータスが返される    |
| `set -v`          | 実行されるコマンドを表示                                                                                                                |
| `set -x           | デバッグ情報                                                                                                                            |
## 記事

- [set - Set or unset values of shell options and positional parameters.](https://linuxcommand.org/lc3_man_pages/seth.html)
- [.envを扱いたいみなさん](https://qiita.com/ryo0301/items/3a6ccdd4e4cb55f82d4a)
- [mihow/load_dotenv.sh](https://gist.github.com/mihow/9c7f559807069a03e302605691f85572)
- [bashシェルスクリプトの記述の仕方に関するメモ書き](https://qiita.com/daisukeshimizu/items/c01f29f8398cc7f5c396)


