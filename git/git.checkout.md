# [git-checkout](https://git-scm.com/docs/git-checkout)

## checkout: 削除してしまったファイルを戻す

~~~bash
$ git checkout HEAD --  ../language/ja_jp.lang.py
~~~

~~~bash
$ git checkout -f
~~~
~~~bash
$ git checkout -f ../lib
~~~

## 特定のブランチからファイルを指定してマージします

`fulfillments` ブランチからインタラクティブにマージする:

~~~zsh
% git checkout --patch fulfillments sheets.py
~~~


`ここはStagingに乗せる？`(ワークツリーからコミットしたいファイル又はファイルの一部をIndexに登録すること):

~~~
Stage this hunk [y,n,q,a,d,/,j,J,g,s,e,?]?
~~~

~~~
y - はい: stage this hunk(変更した一範囲)
n - いいえ: do not stage this hunk
q - 中止します: quit; do not stage this hunk nor any of the remaining ones
a - これ以降は全てはい、です: stage this hunk and all later hunks in the file
d - これ以降は全ていいえ、です:: do not stage this hunk nor any of the later hunks in the file

g - 対象の変更を選択: select a hunk to go to
/ - 検索します(正規表現): search for a hunk matching the given regex

j - スキップして次の考慮中の変更に飛びます: leave this hunk undecided, see next undecided hunk
J - スキップして次の変更に飛びます: leave this hunk undecided, see next hunk
k - スキップして前の考慮中の変更に飛びます: leave this hunk undecided, see previous undecided hunk
K - スキップして前のの変更に飛びます: leave this hunk undecided, see previous hunk

s - 変更点をさらに分割します: split the current hunk into smaller hunks

e - 変更点を手動で訂正します: manually edit the current hunk

? - ヘルプ: print help
~~~