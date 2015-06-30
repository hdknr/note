## 絶対パス

- readline を使ってスクリプトの絶対パスを出す

~~~
BASEDIR=$(readlink -f $0 | xargs dirname)
~~~


## 置換

- [参考](http://d.hatena.ne.jp/ozuma/20130928/1380380390)

```
${VAR#パターン} → 前方一致でのマッチ部分削除(最短マッチ)
${VAR##パターン} → 前方一致でのマッチ部分削除(最長マッチ)
${VAR%パターン} → 後方一致でのマッチ部分削除(最短マッチ)
${VAR%%パターン} → 後方一致でのマッチ部分削除(最長マッチ)
${VAR/置換前文字列/置換後文字列} → 文字列置換(最初にマッチしたもののみ)
${VAR//置換前文字列/置換後文字列} → 文字列置換(マッチしたものすべて)
```

- basname 

~~~
basename=${path##*/}
~~~

- 拡張子

~~~
extension=${basename##*.}
~~~

- 拡張子なし

~~~
filename=${basename%.*}
~~~

## プロンプト
- [PS1](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html)


## 配列の要素を削除

- unset
- 要素インデックスを詰めてくれない

## let で計算

```
   X=1;
   let "X=X+1";
   echo $X; 
   let "X=X*37";
   echo $X;
```
```
2
74
```


## 関数

- [関数の使用方法](http://shellscript.sunone.me/function.html)

## 複数行に渡る文字列

[c++,bash,python,perl : 複数行にわたる文字列](http://www.hci.iis.u-tokyo.ac.jp/~ogaki/blog/blog/2012/02/14/cbashpython-%E8%A4%87%E6%95%B0%E8%A1%8C%E3%81%AB%E3%82%8F%E3%81%9F%E3%82%8B%E6%96%87%E5%AD%97%E5%88%97/)


~~~bash
DOC='
hoge.bash
    arg1:
'
~~~

## ケースのトグル

[Switching case of characters](http://vim.wikia.com/wiki/Switching_case_of_characters)

## 文字列を分割して配列に入れる

[How do I split a string on a delimiter in bash?](https://stackoverflow.com/questions/918886/how-do-i-split-a-string-on-a-delimiter-in-bash)


```bash
Q="mysql -N -u root --password=password apps"
SCRIPT=$HOME/update_employee_info.sh 
FF="name dep sec"
TT="employee"
TOTAL=46
D=ほげ
#
for T in $TT ;do
  for F in $FF; do
    #echo "update $T set $F='$D'" |  $QT
    bash $SCRIPT
    R=$(echo "select $F, count(*) from $T group by $F" | $Q)
    A=(${R})        # スペースでsplitする
    if [ "${A[1]}" == "$TOTAL" ] ; then
        echo "$T.$F OK" 
    fi
  done;
done
```

## global replace

- {$変数{//変換対象文字/変換文字}

```bash

x=1.2.3.4
echo  ${x//./-}
```

```
1-2-3-4
```

