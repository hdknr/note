- [Javascriptによる正規表現まとめ](http://yut.hatenablog.com/entry/20110305/1299318337)
- [JavaScriptで正規表現（文字列制限編）](http://qiita.com/hrdaya/items/2cd5cc19cae35061225c)


## Unicode

- Unicodeスペースを置き換え

~~~javascript
> "　    ".replace(/[\u3000]/, 'x')
'x    '
~~~
