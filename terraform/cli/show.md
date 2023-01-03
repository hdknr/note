# `show`

~~~bash
% terraform show --help
~~~

~~~
Usage: terraform [global options] show [options] [path]

  Teraffrom `state` / `plan` ファイルを読める形式で出力する。

  `path` が指定されないと現在の `state` が表示される。

Options:

  -no-color           カラー情報を含まない
  -json               JSONで出力
~~~


## 例

~~~json
$ terraform % terraform -chdir=prod show -json all.plan  | jq "." > ~/Downloads/plan.json
~~~


AMIを確認:

~~~bash
terraform -chdir=prod show -json all.plan |  jq -r '.resource_changes[] | select(.type == "aws_instance")|[.address,.change.before.ami,.change.after.ami]|@tsv'
~~~
