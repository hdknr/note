# to_entries/from_entries/with_entries

## `$変数` にあてて、後続にフィルターに処理

- `($変数["フィールド"])` で、 値を キーに変換

~~~bash
$ cat ~/Downloads/ami-prod.json | jq  '.[] | (.Tags | from_entries) as $tags | {($tags["deploy-server"]): .ImageId} | '
~~~