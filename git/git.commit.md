# [git-commit](https://git-scm.com/docs/git-commit)

    git commit [-a | --interactive | --patch] [-s] [-v] [-u<mode>] [--amend]
    	   [--dry-run] [(-c | -C | --fixup | --squash) <commit>]
    	   [-F <file> | -m <msg>] [--reset-author] [--allow-empty]
    	   [--allow-empty-message] [--no-verify] [-e] [--author=<author>]
    	   [--date=<date>] [--cleanup=<mode>] [--[no-]status]
    	   [-i | -o] [-S[<keyid>]] [--] [<file>…​]

## コメントの修正(--amend)

~~~bash
$ git commit --amend -m "コメント修正"
~~~

## fatal: cannot do a partial commit during a merge.

~~~bash
$ git commit -a my_filename
.
~~~

### `-i`, `--include`

![4 Status](https://git-scm.com/figures/18333fig0201-tn.png)

ステージ:

- 「stageする」＝「特定の変更内容をindexに登録する」＝「次回コミットに含めるようgitに指示する」

    Before making a commit out of staged contents so far,
    stage the contents of paths given on the command line as well.

    This is usually not what you want unless you are concluding a conflicted merge.

~~~bash
$ git commit -i file.txt -m "Merging file.txt"
.
~~~

### [3つの場所](https://qiita.com/hshimo/items/ab91b99cd61724127aa7)

1. 作業ディレクトリ
2. ステージング・エリア
3. Gitディレクトリ (レポジトリ)

### ファイルの状態

- `untraced` (追跡されてない)
- `trakced` (追跡されている)

    1. `unmodified` (未修正)
    2. `modified`   (変更済み)
    3. `staged`     (ステージに入った)
