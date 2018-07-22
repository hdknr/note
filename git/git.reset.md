## reset

- srcディレクトリを add したけど取り消す

~~~bash
$ git reset HEAD src
~~~

- pull したけど、一つ前にもどす

~~~bash
$ git reset --hard HEAD^
~~~

## なかったことにして巻き戻す: git reset --hard コミットハッシュ

### ローカルを指定したコミットのところまで戻す

~~~~
$ git reset --hard e5e19a7
HEAD is now at e5e19a7 カラム指定
~~~~

オプション
- `--hard` : ローカルの内容も戻してしまう
- `--soft` : ローカルの内容はもどさない

ポジション
- `HEAD^` : 直前のコミット
- `HEAD^^` : ２つ前
- `HEAD~3`: ３つ前 (=`HEAD^^^`)
- `HEAD~`: 直前
- `ハッシュ値`
- `@^` : HEAD == @ :つまり直前

### そのあとで、リモート強制プッシュするとローカルの内容に合わせる

~~~
$ git push -f origin concept
Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create pull request for concept:
remote:   https://bitbucket.org/harajukutech/pallet/pull-request/new?source=concept&t=1
remote:
To git@bitbucket.org:harajukutech/pallet.git
 + 31f8ac9...e5e19a7 concept -> concept (forced update)
~~~

### 別のコンピュータ

~~~
 $ git pull
From bitbucket.org:harajukutech/pallet
 + 31f8ac9...e5e19a7 concept    -> origin/concept  (forced update)
Already up-to-date.

$ git status
On branch concept
Your branch is ahead of 'origin/concept' by 9 commits.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean

$ git reset --hard e5e19a7
HEAD is now at e5e19a7 カラム指定

~~~


## 削除したファイルの復活

~~~bash
$ git reset HEAD app.ico
$ git checkout  app.ico
~~~

## fatal: You have not concluded your merge (MERGE_HEAD exists).

## fatal: multiple stage entries for merged file '.gitignore'

- http://qiita.com/dt_pal/items/bb28084a63ad53a4039f


## 記事

- [git reset HEAD^を取り消す方法](https://qiita.com/ngron/items/7870fc8a803b882af9bd)
- [[git reset (--hard/--soft)]ワーキングツリー、インデックス、HEADを使いこなす方法](https://qiita.com/shuntaro_tamura/items/db1aef9cf9d78db50ffe)
- [gitで一度行った変更をなかったことにする方法4つ](http://labs.timedia.co.jp/2011/02/git-various-undo.html)
- [gitでのヤバイ！を取り消す方法](https://qiita.com/ritukiii/items/74ee3274c3f218511a0c)
- [3分でわかるGitで間違えてコミットや削除したときに使用するコマンド](https://iwb.jp/git-branch-restore-change-delete-command/)