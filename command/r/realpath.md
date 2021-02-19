# realpath

スクリプトの絶対パス:

~~~zsh
#!/bin/zsh
BASEDIR=$(dirname $(realpath "$0"))
echo $BASEDIR
~~~


## 記事

- [bash で ファイルの絶対パスを得る](https://qiita.com/katoy/items/c0d9ff8aff59efa8fcbb)
