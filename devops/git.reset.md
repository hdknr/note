## なかったことにする: git reset --hard コミットハッシュ

- ローカルを戻す

~~~~
$ git reset --hard e5e19a7
HEAD is now at e5e19a7 カラム指定
~~~~

- リモート強制プッシュ

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

- 別のコンピュータ

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