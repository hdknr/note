# if


## `[` と `[[`

`[`:

- `/usr/bin` 配下に存在する通常のコマンド
- `[` がコマンド本体, `]` はパラメータ( `[` の直後にスペースがないとエラーになるのはそのため )
- エラーステータス は `2`
- 変数は展開されるので、　`if` で処理する場合は `"` で囲う

~~~bash
$ which "["
/usr/bin/[
~~~


`[[`:

- `bash` の組み込みコマンド
- エラーステータス は `1`


注意:

- `zsh` では、 `[` は組み込みコマンド