## moment.js

### moment.js を使いましょう

- ブラウザのJavascriptによってDateの挙動が異なるのでmement.js を使いましょう
- [http://momentjs.com/](http://momentjs.com/)

~~~bash
$ npm install moment --save
moment@2.13.0 node_modules/moment
~~~

~~~js
> var moment = require('moment')

> var dt = moment();
undefined
> dt
{ [Number: 1465183469148]
  _isAMomentObject: true,
  _isUTC: false,
  _pf:
   { empty: false,
     unusedTokens: [],
     unusedInput: [],
     overflow: -2,
     charsLeftOver: 0,
     nullInput: false,
     invalidMonth: null,
     invalidFormat: false,
     userInvalidated: false,
     iso: false,
     parsedDateParts: [],
     meridiem: null },
  _locale:
   { _ordinalParse: /\d{1,2}(th|st|nd|rd)/,
     ordinal: [Function],
     _abbr: 'en',
     _config:
      { ordinalParse: /\d{1,2}(th|st|nd|rd)/,
        ordinal: [Function],
        abbr: 'en' },
     _ordinalParseLenient: /\d{1,2}(th|st|nd|rd)|\d{1,2}/ },
  _d: Mon Jun 06 2016 12:24:29 GMT+0900 (JST) }
>
> moment('2016-06-01 10:00:00').toString();
'Wed Jun 01 2016 10:00:00 GMT+0900'
> moment('2016-06-01 10:00:00').toISOString();
'2016-06-01T01:00:00.000Z'
~~~

- パース

~~~js
> dt = moment('2016-11-02T02:07:38.396Z')
> dt.isValid()
true
> dt.toDate().getFullYear()
2016
~~~

### moment 問題とか

Safariの場合、 YYYY-MM-DD を守らないと日付をデシリアライズできない:

~~~js
moment('2018-01');        // OK
moment('2018-1');         // NG
moment(['2018', '1']);    // OK (こちら推奨)
~~~

`add`などは破壊的:

~~~js
while(dt <= last ){
    ...
    dt.add(1, 'month')
}
~~~

オブジェクトなので、代入するときはインスタンスを作ること:

~~~js
all_dt = []
while(dt <= last){
    all_dt.push(moment(dt));            // 新しく作ったインスタンスを保存する
    dt.add(1, 'month')
}
~~~

## Date

### Date.parse

-  返すのは Date でなく整数

~~~js
> var a = "2016-01-01T03:00:00Z";
undefined
> Date.parse(a)
1451617200000
> new Date(a)
Fri Jan 01 2016 03:00:00 GMT+0000 (UTC)
~~~

### 演算

- 比較は `getTime()` メソッドで行う
- `YYYY-MM-DD` と　現在時刻を比較するときは時刻を `00:00:00` (とか) にあわせること

~~~js
const value = moment('2018-04-21', 'YYYY-MM-DD').toDate();                  // 00:00:00
// startOf('day') をすることで、時刻を 00:00:00 にそろえる
const min_date = moment().subtract(13, 'months').startOf('day').toDate();
const max_date = moment().subtract(1, 'days').startOf('day').toDate();
~~~

### 書式

- toString()        `'Wed Jun 01 2016 10:00:00 GMT+0900 (JST)'`
- toDateString()    `'Wed Jun 01 2016'`
- toTimeString()    `'10:00:00 GMT+0900 (JST)'`
- toISOString()     `'2016-06-01T01:00:00.000Z'`
- toGMTString()     `'Wed, 01 Jun 2016 01:00:00 GMT'`
- toJSON()          `'2016-06-01T01:00:00.000Z'`
- toLocaleDateString()  `'2016-06-01'`
- toLocaleTimeString()  `'10:00:00'`

## 時間追加

- setFullYear(), setMonth(), setDate()
- setHours(), setMinutes(), setSeconds(), setMilliseconds()
- setUTC*()

### deep copy

~~~js
var date = new Date();
var copiedDate = new Date(date);
~~~

### 分ブロック単位化

~~~js
// 次の block 単位日時
function blocktime(dt, block){
    h = dt.getHours();
    m = block * Math.ceil(dt.getMinutes() / block );
    return new Date(dt.getFullYear(), dt.getMonth(), dt.getDay(), h, m, 0, 0);    
}

// 指定された時刻間のブロックリスト
function blocktimelist(d0, d1, block){
    var s = new Date(d0);
    var rs = [];
    while(s <= d1) {
        rs.push(new Date(s));
        s.setMinutes(s.getMinutes() + block);
    }   
    return rs;
}
~~~    

## Picker

- [Datepicker for Bootstrap](http://www.eyecon.ro/bootstrap-datepicker/)
- [Bootstrap Timepicker](http://jdewit.github.io/bootstrap-timepicker/)
- [jQuery UI Timepicker](https://fgelinas.com/code/timepicker/)
- [HTML + CSS + JavaScript で簡単に導入できるdatetimepicker の比較](http://techracho.bpsinc.jp/shibuya/2014_10_15/19114)

## 記事

- [Generate array of times for every X minutes in Javascript](http://stackoverflow.com/questions/36125038/generate-array-of-times-for-every-x-minutes-in-javascript)
- [意外と知られていないJavaScriptのnew Date()の使用方法](http://iwb.jp/javascript-new-date-gettime/)
- [JavaScript の Date は罠が多すぎる](http://qiita.com/labocho/items/5fbaa0491b67221419b4)
- [Dateオブジェクトの挙動の違い](http://d.hatena.ne.jp/naoyes/20101107/1289105967)
