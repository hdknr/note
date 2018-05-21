underscore.js

- [http://underscorejs.org/](http://underscorejs.org/)
- [enja-oss/Underscore](https://github.com/enja-oss/Underscore)

## nullフィールドをオブジェクト(辞書)から抜く

[omit](http://underscorejs.org/#omit) + [isNull](http://underscorejs.org/#isNull): 

~~~js
> const _ = require('underscore')
undefined
> _.omit([1, 2, null, 3, 4, null, 5], _.isNull)
{ '0': 1, '1': 2, '3': 3, '4': 4, '6': 5 }
> _.omit({a: 3, b: null, c: 5}, _.isNull)
{ a: 3, c: 5 }

~~~~

## 記事

- [JavaScriptで関数型プログラミングを強力に後押しするUnderscore.jsのおすすめメソッド12選（lodashもあるよ）](http://qiita.com/takeharu/items/7d4ead780710c627172e)
- [遅すぎたUnderscore.js入門 - 全体像](http://qiita.com/hp0me/items/72d80dc166aace2759dc)
