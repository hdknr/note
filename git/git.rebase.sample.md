rebase サンプル

## 現在の状態

~~~
* 49ce6cc c4: master update from c2 (hdknr)  (HEAD, master)
| * 406a2d8 c3: feature branch first commit (hdknr)  (feature)
|/  
* de9d6f2 c2: 2nd update (hdknr)
* 3d8e658 c1: First Update (hdknr)
* b045031 c0: first commit (hdknr)
~~~

## A. masterで featureを merge

~~~bash
$ git branch master
$ git merge feature
$ vim README.md
$ git commit -a -m "c5: merged master"
~~~

~~~~
*   7f32a42 c5: merged master (hdknr)  (HEAD, master)
|\  
| * 406a2d8 c3: feature branch first commit (hdknr)  (feature)
* | 49ce6cc c4: master update from c2 (hdknr)
|/  
* de9d6f2 c2: 2nd update (hdknr)
* 3d8e658 c1: First Update (hdknr)
* b045031 c0: first commit (hdknr)
~~~

## B. feature で master を rebaseしてから masterで featureをmerge

~~~bash
$ git checkout feature
$ git rebase master

First, rewinding head to replay your work on top of it...
Applying: c3: feature branch first commit
Using index info to reconstruct a base tree...
M       README.md

Falling back to patching base and 3-way merge...
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Failed to merge in the changes.
Patch failed at 0001 c3: feature branch first commit
The copy of the patch that failed is found in:
   /tmp/t3/.git/rebase-apply/patch

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".
~~~

~~~bash
$ git rebase --continue
README.md: needs merge
You must edit all merge conflicts and then
mark them as resolved using git add

$ git add README.md
$ git rebase --continue
Applying: c3: feature branch first commit
~~~

~~~
* 47772bc c3: feature branch first commit (hdknr)  (feature)
* 49ce6cc c4: master update from c2 (hdknr)  (HEAD, master)
* de9d6f2 c2: 2nd update (hdknr)
* 3d8e658 c1: First Update (hdknr)
* b045031 c0: first commit (hdknr)
~~~

masterでfeatureをマージ

~~~
$ git checkout master
$ git merge feature
Updating 49ce6cc..47772bc
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

$ more README.md
c3': rebased master
~~~

~~~
* 47772bc c3: feature branch first commit (hdknr)  (HEAD, master, feature)
* 49ce6cc c4: master update from c2 (hdknr)
* de9d6f2 c2: 2nd update (hdknr)
* 3d8e658 c1: First Update (hdknr)
* b045031 c0: first commit (hdknr)
~~~
