
[git-read-tree - Reads tree information into the index

](https://git-scm.com/docs/git-read-tree)

## サブディレクトリのマージ

sampleレポジトリの作成:

~~~bash
$ mkdir sample;cd sample
$ git init
Initialized empty Git repository in /Users/hide/Downloads/sample/.git/
$ echo "Master" > README.md
$ mkdir feature1
$ mkdir feature2
$ echo "Feature1" > feature1/README.md
$ echo "Feature2" > feature2/README.md
$ git add .
$ git commit -a -m "start"
[master (root-commit) c0688b1] start
 3 files changed, 3 insertions(+)
 create mode 100644 README.md
 create mode 100644 feature1/README.md
 create mode 100644 feature2/README.md
$ tree .
.
├── README.md
├── feature1
│   └── README.md
└── feature2
    └── README.md

2 directories, 3 files
~~~

feature1, feature2ブランチの作成：

~~~bash
$ git branch feature1
$ git branch feature2
$ git branch
  feature1
  feature2
* master
~~~

feature1の実装:

~~~bash
$ git checkout feature1
Switched to branch 'feature1'
$ echo "hello()" >> feature1/README.md 
$ echo "print('hello')" > feature1/hello.py
$ git add .
$ git commit -a -m "feature1: hello() was implemented"
[master 51c1de4] feature1: hello() was implemented
 2 files changed, 2 insertions(+)
 create mode 100644 feature1/hello.py
$ tree .
.
├── README.md
├── feature1
│   ├── README.md
│   └── hello.py
└── feature2
    └── README.md

2 directories, 4 files
~~~

feature2の実装:

~~~bash
$ git checkout feature2
Switched to branch 'feature2'
$ echo "goodbye()" >> feature2/README.md  
$ echo "print('good bye')" > feature2/goodbye.py
$ git add .
$ git commit -a -m "feature2: goodbye() was implemented"
[master 2452ef1] feature2: goodbye() was implemented
 2 files changed, 2 insertions(+)
 create mode 100644 feature2/goodbye.py

$ tree .
.
├── README.md
├── feature1
│   └── README.md
└── feature2
    ├── README.md
    └── goodbye.py

2 directories, 4 files
~~~

masterからtempをブランチ:

~~~bash
$ git checkout master
Switched to branch 'master'
$ git checkout -b temp
Switched to a new branch 'temp'
~~~

feature1を更新したいので、tempで一旦削除:

~~~bash
$ git rm -r --cached feature1
rm 'feature1/README.md'
~~~

feature1のfeature1ディレクトリの差分だけをtempに持ってくる:

~~~bash
$ git read-tree --prefix=feature1/ feature1:feature1
$ git status
On branch temp
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   feature1/README.md
        new file:   feature1/hello.py

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   feature1/README.md
        deleted:    feature1/hello.py
~~~

tempでチェックアウト:

~~~bash
$ git checkout .
$ git status
On branch temp
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   feature1/README.md
        new file:   feature1/hello.py
~~~

tempをコミット:

~~~bash
$ git commit -a -m "feature1 -> temp"
[temp 2193b37] feature1 -> temp
 2 files changed, 2 insertions(+)
 create mode 100644 feature1/hello.py
~~~

masterに移って、tempを取り込む:

~~~bash
$ git checkout master
Switched to branch 'master'

$ git merge --squash temp
Updating 1203d78..2193b37
Fast-forward
Squash commit -- not updating HEAD
 feature1/README.md | 1 +
 feature1/hello.py  | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 feature1/hello.py
~~~


masterで取り込み分をコミット:

~~~bash
$ git commit -a -m "feature1 -> temp -> master"
[master b2b97b4] feature1 -> temp -> master
 2 files changed, 2 insertions(+)
 create mode 100644 feature1/hello.py

$ tree .
.
├── README.md
├── feature1
│   ├── README.md
│   └── hello.py
└── feature2
    └── README.md

2 directories, 4 files
~~~

tempを削除:

~~~bash
$ git branch -D temp
Deleted branch temp (was 2193b37).
~~~

feature2も同様に。。。

まだ temp を削除していない状態:

~~~bash 
$ git log --graph --all --format="%x09%an%x09%h %d %s"

*       hdknr   2bfe83b  (HEAD -> master) feature2->temp->master
| *     hdknr   605851d  (temp) feature2 -> temp
|/  
*       hdknr   b2b97b4  feature1 -> temp -> master
| *     hdknr   422d76d  (feature2) readme
| *     hdknr   fe08b2d  feature2: goodbye() was implemented
|/  
| *     hdknr   486bc32  (feature1) feature1: hello() was implemented
|/  
*       hdknr   1203d78  start
~~~