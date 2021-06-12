## 印刷時にURLが表示されてしまう

- bootstrap で `content` が埋められている

~~~css
@media print {
  a[href]:after { content: " (" attr(href) ")"; }
  abbr[title]:after { content: " (" attr(title) ")"; }
~~~  

- ブランクを設定するようにページに記載する

~~~css
@media print {
    a[href]:after { content: ""; }
    abbr[title]:after { content: ""; }
}
~~~
