# ng-repeat


## limitTo

- [limitTo](https://docs.angularjs.org/api/ng/filter/limitTo)
- [Angular.js入門 (3)フィルタ](http://qiita.com/_rdtr/items/5bf69a29e33f668168cc)
- [angularjs show last 5 items in ng-repeat list](http://stackoverflow.com/questions/26812833/angularjs-show-last-5-items-in-ng-repeat-list)


~~~html
<li ng-repeat="name in nameLog | limitTo:-5 | orderBy:'time':true">...</li>
~~~
