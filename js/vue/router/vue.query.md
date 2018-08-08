# クエリ

`http://foo.com/path/to/page#?key1=val1&key2=val2` でフラグメント以降にクエリをわたすと `$route.query` でオブジェクトで参照可能

`category=カテゴリ名` を渡す例：

~~~js
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
  ]
})

new Vue({
  router,
  el: '#app',
  data:{},
  created(){
    if(this.$route.query.category) {
      const category = this.$_.find(this.env.categories, (c)=>{return c.name == this.$route.query.category; });
      Vue.set(this, 'category', category);
    }
  },
}
~~~

## DOM + underscore.js を使う

~~~js
function getFragmentQuery(){
    var parser = document.createElement('a');
    parser.href = location.href;
    parser.href = parser.hash.replace('#', '');
    var query = _.map(parser.search.replace('?', '').split('&'), function(pair){
      return decodeURI(pair).split('='); 
    });
    return _.object(query);
}

function getCategory(categories){
    var query = getFragmentQuery();
    var category = _.find(categories, function(cat){return cat.name == query.category;});
    return category;
}
~~~
