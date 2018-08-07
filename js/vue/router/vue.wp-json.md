# wp-json の記事を固定ページにレンダリング

`$route` をウォッチして、 `this.$route.params.your_router_variable` を処理する

~~~js
 watch: {
    '$route': 'onRoute'
  },
~~~

## wordpress.js ミックスイン

~~~js
const routes = [
 {path: '/posts/:id', name: 'post'},        // 記事番号
 {path: '/page/:page', name: 'page'},       // 改ページ
];

// ルーターの追加
var router = new VueRouter({
  routes
});

var wordpress = {
  data: function () {
    return {
      categories: {},                   // Wordpressカテゴリ
      categories_ids: {},               // カテゴリ
      nextPost: null,                   // 次の記事
      prevPost: null,                   // 前の記事
      current_page: 1,                  // 現在のページ
      total_pages: 1,                   // 全体のページ数
      post_counts:0,                    // ページ無いの記事数
      posts: [],                        // ページのPosts
      post: {}                          // 個別のPost
    };
  },
  filters: {
    local_datetime: function (date, format) {
      // ISO時間をローカルに変換する
      format = format || 'YYYY.MM.DD';
      return moment(date).format(format);
    }
  },
  methods: {
    firstCategory: function(post){
      // ある記事の最初のカテゴリのスラグを返す
      if (post.categories && post.categories.length > 0) {
        const id = post.categories[0];
        const cats = this.categories.filter(function(cat){ return id == cat.id; });
        if(cats.length > 0){
           return cats[0].slug;
        }
      }
      return 'post';
    },

    isCategory: function (slug, post) {
      // 記事が指定したカテゴリかを判定
      if (post.categories && post.categories.length > 0) {
        const id = post.categories[0];
        return _.some(this.categories,
          function (cat) {
            return (cat.id == id) && (slug == cat.slug);
          }
        );
      }
      return false;
    },

    reloadPosts: function (slugs, id) {
      // Wordpressから指定したスラグのカテゴリ番号の記事を取ってくる
      // IDは記事番号で、onCategoriesLoadedに渡す
      let params = {
        'slug': slugs.join(',')
      };
      var url = '/wordpress/wp-json/wp/v2/categories';
      axios.get(url, {
        params: params
      }).then((res) => {
        Vue.set(this, 'categories', res.data);
        Vue.set(this, 'categories_ids',
          res.data.map(function (cat) {
            return cat.id;
          }));
        // カテゴリがロードされたら
        this.onCategoriesLoaded(slugs, id);
      });
    },

    onCategoriesLoaded: function(slug, id){
        // カテゴリが読み込まれた後の処理
        if (id) {
          // IDがあったら記事を読み込む(詳細ページ)
          this.getPost(id);
        } else {
          // カテゴリに対応するPostを読み込む(一覧ページ) 
          this.loadPosts(this.categories_ids);
        }
    },

    getPost: function (id) {
      // 個別記事の取得
      let params = {'_embed': '' };
      var url = '/wordpress/wp-json/wp/v2/posts/' + id;
      axios.get(url, {
        params: params
      }).then((res) => {
        Vue.set(this, 'post', res.data);
        this.onPostLoaded();                    // 読み込まれたあとの処理
        this.getNextPost(this.post);            // 次の記事
        this.getPrevPost(this.post);            // 前の記事
      });
    },

    onPostLoaded: function() {
        // 個別記事が読み込まれたら
    },

    loadPosts: function (categories_ids, name) {
      // 一覧記事を読み込む
      name = name || 'posts';
      let params = {
        '_embed': '',
        'page': this.current_page,
        'per_page': 100,
      };
      params.categories = categories_ids.join(',');
      var url = '/wordpress/wp-json/wp/v2/posts';
      axios.get(url, {
        params: params
      }).then((res) => {
        Vue.set(this, name, res.data);
        // メタ情報が応答ヘッダーに帰ってくる
        Vue.set(this, 'total_pages', res.headers['x-wp-totalpages']);       // ページ数
        Vue.set(this, 'post_counts', res.headers['x-wp-total']);            // 記事数
      });
    },

    postDetailUrl: function (post) {
      // 詳細記事JSONをレンダリングする固定ページリンクを作る
      const category = this.firstCategory(post);
      const path = "/post/" + catgory ".html#/posts/" + post.id;
    },

    toLocalHtml(post, field){
      // Wordpressの exerpt, content のアンカーを変換(Wordpressに飛ばないで、固定ページに飛ばす)
      if (post && post[field]) {
        const src = post[field].rendered;
        let el = document.createElement('div');
        el.innerHTML = src;
        const anchors = el.getElementsByTagName("a");
        for (let i = 0; i < anchors.length; i++) {
          anchors[i].href = this.postDetailUrl(post);
        }
        return el.innerHTML;
      }
      return '';
    },

    getNextPost: function(post) {
      // 指定した記事の次の記事
      let params = {
        '_embed': '',
        'after': post.date,
        'order': 'asc',
      };
      params.categories = this.categories_ids.join(',');
      var url = '/wordpress/wp-json/wp/v2/posts';
      axios.get(url, {
        params: params
      }).then((res) => {
        Vue.set(this, 'nextPost', (res.data.length > 0) ? res.data[0] : null);
      });
    },

    getPrevPost: function(post) {
      // 指定した記事の前の記事
      let params = {
        '_embed': '',
        'before': post.date,
        'order': 'desc',
      };
      params.categories = this.categories_ids.join(',');
      var url = '/wordpress/wp-json/wp/v2/posts';
      axios.get(url, {
        params: params
      }).then((res) => {
        Vue.set(this, 'prevPost', (res.data.length > 0) ? res.data[0] : null);
      });
    },

    catchImage: function(post){
      // 記事に設定されているキャッチ画像
      try{
      	const media = post['_embedded']['wp:featuredmedia'];
      	const res = media[0]['media_details']['sizes']['medium']['source_url'];
        return res;
      }catch(e){
        return '';
      }
    }
  }
}
~~~


## index.html

- `slugs` で指定したカテゴリの記事を Wordpressから取ってきて一覧する
- 要約(excerpt)の中のアンカーは Wordpressへのリンクなので、 固定ページのリンクに変更する
- `index.html#/page/3` のようにページ番号が指定されているので、それを読み取る

~~~html
<div v-for="post in posts">
    <a :href="postDetailUrl(post)">
		<div>
	        <img :src="catchImage(post)">
		</div>

        <p class="day">{{ post.date|local_datetime }}<p>

        <h3>{{ post.title.rendered }}</h3>
        <div v-html="toLocalHtml(post, 'excerpt')"></div>
    </a>
</div>

<ul><!-- 改ページ-->
    <li>{{current_page }} / {{ total_pages }}</li>
    <template v-if="total_pages > 1">
    <li v-for="i in (1, total_pages)">
        <a href="#" @click="onPageChanged(i)" :class="{on: i == current_page }">
            <span v-if="i < total_pages">{{ i }}</span>
            <span v-else>最終</span>
        </a>
    </li>
    </template>
</ul>
~~~

~~~html
<!--vue, vu-router, axios, moment, underscore -->
<script src="//cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="//unpkg.com/vue-router@3.0.1/dist/vue-router.js"></script>
<script src="//unpkg.com/axios/dist/axios.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/locale/ja.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore-min.js"></script>
<script src="/script/vuw/wordpress.js"></script>
<script>
var app = new Vue({
  el: '#app',
  mixins: [wordpress],
  data: {
    slugs: ['post','news','blog'],          // カテゴリスラグ
  },
  methods:{
    fetchData: function() {
       // ページ読み込み
       this.reloadPosts(this.slugs);
    },
    onPageChanged(page){
      // ページが変わったら
      if(page){
         Vue.set(this, 'current_page', page);
         this.fetchData();
      } 
    },
    onRoute: function(){
      // ルーティングのパラメータが変わったら(実際はURLでページ指定があったら)
      const page = this.$route.params.page;
      this.onPageChanged(page);
    }
  },
   watch: {
    '$route': 'onRoute'
  },
  mounted() {
    // 最初にページをロードする
    this.fetchData();
  }
});
</script>
~~~

## news.html(post.html, blog.html) (詳細ページ)

- `news.html#/post/3` のように記事番号が指定されているので、それを読み取る

~~~html
<section><!-- 記事詳細 -->
    <img :src="catchImage(post)">
    <h3 v-if="post.title">{{ post.title.rendered }}</h3>

    <div class="warp">
        <p class="date">{{ post.date|local_datetime }}</p>
        <div v-if="post.content" v-html="toLocalHtml(post, 'content')">
            <!-- ブログ内容 -->
        </div>
        <a href="index.html"> 戻る</a>
    </div>

	<ul class="pager"> <!-- 前後の記事 -->
        <li>
            <a :href="postDetailUrl(prevPost)" v-if="prevPost">&#x3C; PREV</a>
        </li>
        <li>
            <a href="index.html">TOP</a>
        </li>
        <li>
            <a :href="postDetailUrl(nextPost)" v-if="nextPost">NEXT &#x3E;</a>
        </li>
    </ul>
</section>
~~~

~~~html
<!--vue, vu-router, axios, moment, underscore -->
<script src="//cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="//unpkg.com/vue-router@3.0.1/dist/vue-router.js"></script>
<script src="//unpkg.com/axios/dist/axios.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/moment.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.22.2/locale/ja.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore-min.js"></script>
<!-- vue-head でHTMLの head を変更 -->
<script src="//cdn.rawgit.com/ktquez/vue-head/master/vue-head.js"></script>
<script src="/script/vuw/wordpress.js"></script>
<script>
var app = new Vue({
  router,
  el: 'app',
  mixins: [wordpress],
  watch: {
    '$route': 'onRoute',                        // ルートが変更されたら
    'post': function () {                       
      // postの内容が変わったらページのタイトル変更
      document.title = this.post.title.rendered;
    }
  },
  methods: {
    onRoute: function () {
      this.reloadPosts(["news"], this.$route.params.id);
    },
    onPostLoaded: function () {
      // ページがよみこまれたら head を変更
      this.$emit('updateHead');
    }
  },
  mounted() {
    this.onRoute();         // 最初にURLのフラグメントのidの記事を読み込む
  },
  head: {
    title: function () {
      return {
        inner: (this.post && this.post.title) ? this.post.title.rendered : '',
        separator: ' ',
        complement: ' '
      }
    },
    meta: function () {
      // $emit('updateHead') のコールバック
      return [{
          name: 'description',
          content: (this.post && this.post.title) ? this.post.title.rendered : ''
        },
        {
          name: 'twitter:title',
          content: (this.post && this.post.title) ? this.post.title.rendered : ''
        },
        {
          n: 'twitter:description',
          c: (this.post && this.post.title) ? this.post.title.rendered : ''
        },
      ]
    }
  }
});
</script>
~~~