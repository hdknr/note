# Git: [#48](https://github.com/hdknr/scriptogr.am/issues/48)

## コマンド

| Command                              | 内容, 用例                 |
| ------------------------------------ | ------------------------ |
| [branch](git.branch.md)              | ブランチ管理              |
| [checkout](git.checkout.md)          | ファイルを戻す /  ブランチ変更   |
| [cherry-pick](git.cherry-pick.md)    | 指定したコミットを取り込む   |
| [clone](git.clone.md)                | クローン                  |
| [commit](git.commit.md)              |   |
| [config](git.config.md)              |   |
| [diff](git.diff.md)                  | 差分 |
| [filter-branch](git.filter-branch.md)   |                       |
| [fsck](git.fsck.md)                   | DBのオブジェクトの妥当性の検証/接続の検証 |
| [log](git.log.md)                     |   |
| [ls-files](git.ls-files.md)           |   | 
| [merge](git.merge.md)                  | |
| [pull](git.pull.md)                   | |
| [push](git.push.md)                    | |
| [read-tree](git.read-tree.md)          | サブディレクトリの変更の取り込み |
| [remote](git.remote.md)                | |
| [reset](git.reset.md)                  | |
| [submodule](git.submodule.md)           | |
| [worktree](git.worktree.md)           | ローカルリポジトリで作業ツリーを複数同時に持つ|

## トピック

- [ssh](git.ssh.md)

## [インストール](git.install.md)

- ソースインストール

## リンク

- [サルでもわかるGit入門](http://www.backlog.jp/git-guide/)
- [github](git.github.md)

## tig

- [tigでgitをもっと便利に！ addやcommitも](http://qiita.com/suino/items/b0dae7e00bd7165f79ea)

~~~bash
$ sudo apt-get install tig
.
~~~~

~~~bash
$ brew install tig
.
~~~

## How To

- [特定のブランチからファイルの変更をマージする](git.checkout.md)
- [削除してしまったファイルを戻す](git.checkout.md)
- [他のブランチへ特定のコミットをマージする](git.cherry-pick.md)
- [コミット間で変更のあるファイル名を一覧する](git.diff.md)
- [error: remote unpack failed: eof before pack header was fully read](git.fsck.md)
- [特定のファイルの変更記録を見る](git.log.md)
- [削除したファイルを取り除く](git.ls-files.md)
- [リモートにある br-remote1 ブランチを ローカルの br-local2 にpull](git.pull.md)
- [ローカルを指定したコミットのところまで戻す](git.reset.md)
- [sshのキーを指定する](git.ssh.md)
- [ファイル名:大文字・小文字の変更を検知するようにする](git.config.md)


## トピック

- [git-crypt](git-crypt.md)
