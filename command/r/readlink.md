## 現在のディレクトリの絶対パス

~~~
#!/bin/bash
BASEDIR=$(readlink -f $0 | xargs dirname)
echo $BASEDIR
~~~

~~~
$ ../../../run.bash 
/home/vagrant/projects/pia/web
~~~