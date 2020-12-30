# realpath

スクリプトの絶対パス:

~~~zsh
#!/bin/zsh
BASEDIR=$(dirname $(realpath "$0"))
echo $BASEDIR
~~~
