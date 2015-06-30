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