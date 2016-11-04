## 削除したファイルを取り除く

- [参考](http://www.commandlinefu.com/commands/view/1246/git-remove-files-which-have-been-deleted)

~~~bash
$ git rm $(git ls-files --deleted)
~~~
