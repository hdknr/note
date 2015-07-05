~~~
$ ls ../../qiita/*swift*.md | while read s;do  echo $s | ln -s $s $(sed -E  "s/(.+swift)-(.+)/\2/"); done
~~~
