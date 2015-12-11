~~~
$ git filter-branch -f --index-filter 'git rm -rf --ignore-unmatch web/docs/source/terms/N09-01-20150324_B.pdf' HEAD        
     
Rewrite 459241c5db79ef30e3c7455a28d1ac7e31a58824 (25/26)rm 'web/docs/source/terms/N09-01-20150324_B.pdf'
Rewrite 31db00ee63e5465d632ab2e88eb6dfeed7435fa2 (26/26)
Ref 'refs/heads/concept' was rewritten
~~~

~~~
$ git status
On branch concept
Your branch and 'origin/concept' have diverged,
and have 2 and 2 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
nothing to commit, working directory clean
~~~

~~~
$ git pull
Merge made by the 'recursive' strategy.

$ git status
On branch concept
Your branch is ahead of 'origin/concept' by 3 commits.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean

$ git push
Counting objects: 3, done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 513 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: 
remote: Create pull request for concept:
remote:   https://bitbucket.org/harajukutech/pallet/pull-request/new?source=concept&t=1
remote: 
To git@bitbucket.org:harajukutech/pallet.git
   31db00e..5f427cb  concept -> concept
~~~

~~~
$ git filter-branch -f --index-filter 'git rm -rf --ignore-unmatch web/docs/source/terms/N09-01-20150324_B.pdf' -- --all
Rewrite 459241c5db79ef30e3c7455a28d1ac7e31a58824 (28/31)rm 'web/docs/source/terms/N09-01-20150324_B.pdf'
Rewrite 30ee9a8e93fece7b83a138acdd3faef135a467ca (31/31)
Ref 'refs/heads/concept' was rewritten
WARNING: Ref 'refs/heads/master' is unchanged
WARNING: Ref 'refs/remotes/origin/master' is unchanged
Ref 'refs/remotes/origin/concept' was rewritten
WARNING: Ref 'refs/remotes/origin/master' is unchanged
~~~

~~~
$ git pull
From bitbucket.org:harajukutech/pallet
 + edeffb3...30ee9a8 concept    -> origin/concept  (forced update)
Already up-to-date!
Merge made by the 'recursive' strategy.
(wordpress)vagrant@jessie:~/projects/pallet$ git status
On branch concept
Your branch is ahead of 'origin/concept' by 2 commits.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean
(wordpress)vagrant@jessie:~/projects/pallet$ git push
Counting objects: 2, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 321 bytes | 0 bytes/s, done.
Total 2 (delta 1), reused 0 (delta 0)
remote: 
remote: Create pull request for concept:
remote:   https://bitbucket.org/harajukutech/pallet/pull-request/new?source=concept&t=1
remote: 
To git@bitbucket.org:harajukutech/pallet.git
   30ee9a8..31f8ac9  concept -> concept
~~~