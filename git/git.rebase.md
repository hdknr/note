- [3.6 Git のブランチ機能 - リベース](https://git-scm.com/book/ja/v1/Git-%E3%81%AE%E3%83%96%E3%83%A9%E3%83%B3%E3%83%81%E6%A9%9F%E8%83%BD-%E3%83%AA%E3%83%99%E3%83%BC%E3%82%B9)
- [サンプル](git.rebase.sample.md)


## リベース

分岐元のベースを変更する(より新しい更新から分岐したことにする)

~~~
git rebase [分岐元]
~~~

~~~
git rebase f4ba680921aa         # コミット番号
git rebase other-branch         # ブランチ
git rebase origin/other-branch  # オリジンのブランチ
~~~


## コンフリクト

コンフリクトを解消したら continue する

~~~
git rebase --continue
~~~

リベースを無かったものとする

~~~
git rebase --abort
~~~



## pull 時にリベース

~~~
[topic-branch] $ git pull --rebase [main branch]
~~~ 


## ブレンチ

統合ブランチ

- master(main, stable)ブランチ
- リリース版がいつでも作成可能なようにしておくためのブランチ
- なので、常に安定した状態を保っておくこと

トピックブランチ

- 機能追加やバグ修正といったある課題に関する作業を行うためのブランチ
- 統合ブランチから分岐する形で作成し、作業が完了したら統合ブランチに取り込む(merge)


## rebasing

- 公開リポジトリにプッシュしたコミットをリベースしてはいけない
- あくまでもプッシュする前のコミットをきれいにするための方法である


## 資料

- [git rebaseでのブランチ融合でコンフリクト解消](https://qiita.com/shizuma/items/82bb439e8899c1bd3114)
- [git pull --rebaseをpushする前にやろうという話。](https://qiita.com/makua/items/7aa1f4fa02ef9ab1f9d9)
- [Gitブランチについての基本まとめ](https://qiita.com/katsunory/items/252c5fd2f70480af9bbb)
