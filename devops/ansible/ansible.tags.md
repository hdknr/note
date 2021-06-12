- [Ansibleでタグを使ってみる](http://qiita.com/kiarina/items/affa0b68a710eeeda75b)


# タスクの分岐/切り替え

[ansibleで実行対象を切り替える方法](http://tdoc.info/blog/2014/05/30/ansible_target_switching.html):

1. サーバーが異なるだけで、設定が同じ場合 : ホストグループ
2. 最後のtaskを一つだけ切り替えたい: `when`
3. タグで切り替えたい
4. includeでまとめて切り替える
5. roleで切り替える
6. varsを切り替える: `include_vars`
