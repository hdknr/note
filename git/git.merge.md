## マージの前に

- コミットが済んでいないファイルが残っている状態で git checkout しない
- コミットが済んでいないファイルが残っている状態で git merge しない

## ブランチのマージ

fast-foward:

- デフォルトでは `fast-forward` マージ(mergeコミットを発生させる必要がない場合)
- mergeコミットを発生せずにmergeを行います

`--no-ff`:

- 意図的にfast-forwardを行わないコミットをすることが出来る


~~~bash 
$ git checkout master
$ git merge feature-111 --no-ff
~~~

## 問題が起きたら

- マージで衝突が発生した場合(ファイルを修正->コミット)
- マージを元に戻す ([reset](git.reset.md))


## mergeとrebase

mergeとrebaseは共に履歴を統合しますが、特徴が異なる。

merge:

- 変更内容の履歴はそのまま残るが、履歴が複雑になる。

rebase:

- 履歴は単純になるが、元のコミットから変更内容が変更される。
- そのため、元のコミットを動かない状態にしてしまうことがある。


## 記事

- [ブランチ切って更新してマージするまでの流れ](https://qiita.com/shuntaro_tamura/items/6c8bf792087fe5dc5103)
- [gitのmerge --no-ff のススメ](https://qiita.com/nog/items/c79469afbf3e632f10a1)
- [マージコミットとFast-forwardマージ](https://qiita.com/shyamahira/items/59ff8aa1cf7b893aab60)