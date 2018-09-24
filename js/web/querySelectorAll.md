# querySelectorAll

- [Document.querySelectorAll() - Web API インターフェイス | MDN](https://developer.mozilla.org/ja/docs/Web/API/Document/querySelectorAll)
- [document.getElementById()...の代わり. querySelectorのメモ - Qiita](https://qiita.com/s-yoshiki/items/9650da37bd7c842a7036)


## ページのクエリを引き継ぐ

~~~js
 var parser = document.createElement('a');
  parser.href = window.location.href;
  if(parser.search){
    [].map.call(document.querySelectorAll('.rel-landing'), function(a){
      var href = a.getAttribute('href');
      a.setAttribute('href', href + parser.search);
    });
  }
~~~