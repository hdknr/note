# ルータ

## 基礎

### pages/*.vue で router.jsにエントリが追加されます

~~~bash
$ tree pages/
pages/
├── README.md
└── index.vue

$ npm run build
$ more .nuxt/router.js
~~~

~~~js
export function createRouter () {
  return new Router({
    mode: 'history',
    base: '/',
    linkActiveClass: 'nuxt-link-active',
    linkExactActiveClass: 'nuxt-link-exact-active',
    scrollBehavior,
    routes: [
		{
			path: "/",
			component: _08d0bc34,
			name: "index"
		}
    ],
    fallback: false
  })
}
~~~

pages/about.vue を追加

~~~bash
$ tree pages/
pages/
├── README.md
├── about.vue
└── index.vue

$ npm run build
$ more .nuxt/router.js
~~~

~~~js
export function createRouter () {
  return new Router({
    mode: 'history',
    base: '/',
    linkActiveClass: 'nuxt-link-active',
    linkExactActiveClass: 'nuxt-link-exact-active',
    scrollBehavior,
    routes: [
		{
			path: "/about",
			component: _2dce3d22,
			name: "about"
		},
		{
			path: "/",
			component: _08d0bc34,
			name: "index"
		}
    ],
    fallback: false
  })
}
~~~



## 動的ルーティング

- `アンダースコアプレフィックス` で動的ルーティングを生成

~~~bash
$ tree pages/
pages/
├── README.md
├── about.vue
├── index.vue
└── posts
    ├── _slug.vue
    └── index.vue
$ npm run build
$ cat .nuxt/router.js
~~~

~~~js
export function createRouter () {
  return new Router({
    mode: 'history',
    base: '/',
    linkActiveClass: 'nuxt-link-active',
    linkExactActiveClass: 'nuxt-link-exact-active',
    scrollBehavior,
    routes: [
		{
			path: "/posts",
			component: _233edd10,
			name: "posts"
		},
		{
			path: "/about",
			component: _2dce3d22,
			name: "about"
		},
		{
			path: "/posts/:slug",
			component: _26ac1fa0,
			name: "posts-slug"
		},
		{
			path: "/",
			component: _08d0bc34,
			name: "index"
		}
    ],
    fallback: false
  })
}
~~~

~~~bash 
$ npm run dev
~~~

~~~bash
$ curl  -s http://localhost:3000/ | pup h1 text{}
      shaperweb

$ curl  -s http://localhost:3000/about | pup h1 text{}
      About Shaper
    
$ curl  -s http://localhost:3000/posts | pup h1 text{}
      Posts Index
    
$ curl  -s http://localhost:3000/posts/a | pup h1 text{}
      Posts Detail
    
$ curl  -s http://localhost:3000/posts/b | pup h1 text{}
      Posts Detail
~~~

## スタティック生成(`generate`) では動的ルーティングは無視されます

- [generate プロパティ: routes](https://ja.nuxtjs.org/api/configuration-generate#routes)

nuxt.config.jsに `generate` プロパティを追加:

~~~js
module.exports = {
  .......
  generate: {
    routes: [
        '/about',
        '/posts',
        '/posts/1',
        '/posts/2'
    ]
  }
}
~~~

~~~bash 
$ npm run generate
~~~~

~~~bash
$ tree -P *.html dist/
dist/
├── about
│   └── index.html
├── index.html
└── posts
    ├── 1
    │   └── index.html
    ├── 2
    │   └── index.html
    └── index.html
~~~

### 動的なパラーメータ

- `Promise` を返す 関数 を使う
- `コールバック` と一緒に 関数 を使う

Wordpressから記事を取得してみる

~~~bash
$ npm instal axios
~~~~

nuxt.config.js:

~~~js
const axios = require('axios')

module.exports = {
    ...
    generate: {
    routes: function () {
      const url = "http://192.168.56.54:8080/wp-json/wp/v2/posts";
      return axios.get(url)
      .then((res) => {
        return res.data.map((post) => {
          return '/posts/' + post.slug;
        });
      });     
    }
  }
}
~~~

~~~bash
$ npm run generate
.....
nuxt:generate Generate file: /posts/index.html +2s
  nuxt:generate Generate file: /about/index.html +0ms
  nuxt:generate Generate file: /index.html +0ms
  nuxt:generate Generate file: /posts/hello-world/index.html +0ms
  nuxt:generate Generate file: /posts/ratione-distinctio-repellendus-ut-id-ut/index.html +0ms
  nuxt:generate Generate file: /posts/enim-neque-voluptas-qui-qui/index.html +0ms
  nuxt:generate Generate file: /posts/non-ipsum-illo-voluptas-cupiditate-amet-nihil-eum/index.html +0ms
  nuxt:generate Generate file: /posts/aspernatur-nostrum-illum-vero/index.html +0ms
  nuxt:generate Generate file: /posts/ipsam-consequatur-incidunt-quia-in-asperiores/index.html +0ms
  nuxt:generate Generate file: /posts/aut-aut-nihil-impedit-eum-ea-quae-et/index.html +4ms
  nuxt:generate Generate file: /posts/est-fuga-est-excepturi-excepturi-est/index.html +1ms
  nuxt:generate Generate file: /posts/aliquam-repellat-tempora-modi-aut-molestiae-est-quisquam/index.html +0ms
  nuxt:generate Generate file: /posts/quis-est-facilis-sit-magni/index.html +0ms
~~~

## 記事

- [Nuxt.jsのvue-routerの自動生成で詰んだ話 - Qiita](https://qiita.com/masaakikunsan/items/c150c8f21459b6819890)
