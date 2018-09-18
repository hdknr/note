# IE11対応

## Promiseが見つかりません

pollyfill を読み込む:

~~~html
<script src="//www.promisejs.org/polyfills/promise-6.1.0.min.js"></script>
~~~


## アローではなく `function()` で書き直す

~~~js
created(){
    this.initialize();
}
~~~

~~~js
created: function(){
    this.initialize();
}
~~~

## 省略形が使えない

~~~js
var app = new Vue({
    router,
});
~~~

~~~js
var app = new Vue({
    router: router,
});
~~~

## アローがつかえないのでローカルで `this` を定義し直す

~~~js
reloadPosts: function (slugs, id) {
    var vm = this;
    ...
    axios.get(url, {
        params: params
    }).then(function(res){
        Vue.set(vm, 'categories', res.data);
        vm.onCategoriesLoaded(slugs, id);
    });
},
~~~

## vue-routerのイベントが無視される

- [Manual change of hash into the URL doesn't trigger the route in IE11 · Issue #1849 · vuejs/vue-router](https://github.com/vuejs/vue-router/issues/1849)
- [window.onhashchange - Web API インターフェイス | MDN](https://developer.mozilla.org/ja/docs/Web/API/WindowEventHandlers/onhashchange)
- [プログラムによるナビゲーション | Vue Router](https://router.vuejs.org/ja/guide/essentials/navigation.html)

IE判定:

~~~js
methods:{
    isIE: function(){
       return '-ms-scroll-limit' in document.documentElement.style && '-ms-ime-align' in document.documentElement.style;
    },
},
~~~

URLフラグメントが変更されたら vue-router をナビゲートさせるようにイベントハンドラを定義:

~~~js 
mounted: function() {
    if(this.isIE()){
      var vm = this;
      // https://developer.mozilla.org/ja/docs/Web/API/WindowEventHandlers/onhashchange
      window.addEventListener('hashchange', function() {
        var currentPath = window.location.hash.slice(1);    // '#' を覗く
        if (vm.$route.path !== currentPath) {
          // https://router.vuejs.org/ja/guide/essentials/navigation.html
          vm.$router.push(currentPath)
        }
      }, false);
    }
    //.....
},
~~~

## 記事

- [【Vue.js】IE11でひっかかるエラー - Qiita](https://qiita.com/kaoriSG/items/09158675f83183dd43da)
- [【IE11】IE11で動かした時に、vue-routerの定義で「':'がありません」と怒られる【Vue】 - The sky is the limit](http://www.sky-limit-future.com/entry/ie-err-vue-router)
