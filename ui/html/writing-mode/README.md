# 文字の向き

- [CSSで文字を縦書きにする方法 | TechMemo](https://techmemo.biz/css/writing-mode/)
- [HTML5 & CSS3 リファレンス - writing-mode プロパティ（文字表記の方向）](https://www.osaka-kyoiku.ac.jp/~joho/html5_ref/css/writing-mode_css.php)
- [日本らしさを表現！CSSで文字の縦書きに挑戦！ | Webクリエイターボックス](https://www.webcreatorbox.com/tech/writing-mode)
- [CSS3 Writing Modesの仕様解説](http://tategaki.github.io/commentaries/2015/11/09/commentary-writing-modes.html)


## 縦書き(`Vertical` + `Right to Left`)

- `writing-mode: vertical-rl;`
- IE: `-ms-writing-mode: tb-rl;`   (`Vertical` -> `Top to Bottom`)

## 文字の表示方向(`text-orientation`)

~~~css
.mixed {       /* デフォルト: 和文は縦、英語は横 */
  -webkit-text-orientation: mixed;
  text-orientation: mixed;
}
.upright {      /* すべて 縦 */
  -webkit-text-orientation: upright;
  text-orientation: upright;
}

.sideways {     /* 全て横 */
  -webkit-text-orientation: sideways;
  text-orientation: sideways;
}
~~~

## 英数字の向き（縦中横) (`text-combine-upright`)

英数字や記号などを1文字分の幅として表示:

~~~css
.text-combine {
  -webkit-text-combine: horizontal;
  -ms-text-combine-horizontal: all;
  text-combine-upright: all;
}
~~~

「たてちゅうよこ」であり、「たてなかよこ」ではない（JIS X 4051)

## リンク線を右側に(縦書き時)

~~~css
a {
  text-decoration: overline;
}
~~~

あるいは:

~~~css
a {
  text-decoration: none;
  border-right: 1px dashed;
  padding-right: 3px;
}
~~~

## 振り仮名（ルビ） (`ruby` + `rt`(ruby text))

~~~html
<p><ruby>真奈<rt>マナ</rt></ruby></p>
<p><ruby>三次<rt>みよし</rt>ワイナリー</ruby></p>
<p><ruby>伸縮自在の愛<rt>バンジーガム</rt></ruby></p>
~~~

## １文字字下げ

~~~css
p {
  text-indent: 1em;
}
~~~