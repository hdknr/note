# 数字を金額表示

- 文字列化 -> 文字配列化 -> 逆順に並べ替え -> 文字に戻す -> 3桁ごとに区切った配列 -> 間にカンマをいれて文字列化 -> １文字づつの配列 -> 逆順に並べ替え -> 文字列化

~~~javascript
function toCurrency(n){
  return String(n).split("").reverse().join("").match(/\d{1,3}/g).join(",").split("").reverse().join("");
}
~~~

- [JavaScriptは肯定先読みはできるが肯定後読みはできない](http://stabucky.com/wp/archives/5805)

## python

- [数値に3桁ごとのコンマを入れる](http://d.hatena.ne.jp/cheeseshop/20121209/1355018129)

~~~py
import re
re.sub(r'(\d)(?=(\d{3})+(?!\d))', '\\1,', str(3214332))
'3,214,332'
~~~
