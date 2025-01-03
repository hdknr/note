## トピック

- [#66](https://github.com/hdknr/scriptogr.am/issues/66)
- [連想配列](bash.dict.md)
- [配列](bash.arrays.md)
- [補完](bash.completion.md)

## 変数

- [IFS](bash.IFS.md)(Internal Filed Separator: 区切り文字)

## OS

- [OSX](bash.osx.md)

## 記事

## 履歴(!)

- `!` を無効にする

~~~bash
set +H
~~~

- 有効にする

~~~bash
set +H
~~~

## `$$` : PID

~~~bash
$ ps -F --pid $$  
UID        PID  PPID  C    SZ   RSS PSR STIME TTY          TIME CMD
vagrant  24267 29628  0  6361  6328   0 22:57 pts/12   00:00:00 -bash
~~~

- 一時ファイル名

~~~bash
$ date +'%m%d%H%M%S'.$$
1030233536.24267
~~~

## 絶対パス

- [realpath](https://linuxjm.osdn.jp/html/GNU_coreutils/man1/realpath.1.html) を使う

~~~
THIS=$(realpath $0)
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

## name.jpgのファイル名の間に文字を挿入

- [$IFS](https://bash.cyberciti.biz/guide/$IFS)

~~~bash
IFS=.
for i in *.jpg; do
    A=($i)
    echo "${A[0]}.small.${A[1]}"
done
~~~

## global replace

- {$変数{//変換対象文字/変換文字}

```bash

x=1.2.3.4
echo  ${x//./-}
```

```
1-2-3-4
```

## OS判定

~~~
$ echo $OSTYPE
linux-gnu
~~~

~~~
$ echo $OSTYPE
darwin14
~~~

## ヒアドキュメント

- [bashのヒアドキュメントを活用する - Qiita](https://qiita.com/take4s5i/items/e207cee4fb04385a9952)

## その他

- [たった一行で bash の代入式がスマートに書けるようになる関数](http://qiita.com/mattintosh4/items/959517399d5993e34ef7)

## stdout, stderr

- [bash: 標準出力、標準エラー出力をファイル、画面それぞれに出力する方法](https://qiita.com/laikuaut/items/e1cc312ffc7ec2c872fc)

## while

- [シェルスクリプト「whileの中の変数が見えない」解決方法5選 〜 パイプ・サブシェル問題](https://qiita.com/ko1nksm/items/e23d43a7194a388fd850)s
