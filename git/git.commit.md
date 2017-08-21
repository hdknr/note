## コメントの修正(--amend)

~~~bash
$ git commit --amend -m "コメント修正"
~~~


## fatal: cannot do a partial commit during a merge.

~~~bash
$ git commit -a my_filename
~~~


### `-i`, `--include`

~~~
Before making a commit out of staged contents so far,
stage the contents of paths given on the command line as well.

This is usually not what you want unless you are concluding a conflicted merge.
~~~

~~~bash
$ git commit -i file.txt -m "Merging file.txt"
~~~
