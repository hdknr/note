# [asyncData](https://ja.nuxtjs.org/api/)

- `ページコンポーネント` がロードされる前に毎回呼び出される
- asyncData([context](https://ja.nuxtjs.org/api/context)) の結果は data とマージされる

~~~js
export default {
  data () {
    return { project: 'default' }
  },
  asyncData (context) {
    // `context`
    return { project: 'nuxt' }
  }
}
~~~

## [変数の登録の仕方](https://ja.nuxtjs.org/guide/async-data/)

asynDataでサーバーサイドでデータを用意し、コンポーネントの `data` にマージさせます

３つの方式があります:

1. Promise
2. async/await
3. callback  

### 1. promise

~~~js
asyncData ({ params }) {
  // 変数の分割代入(Destructuring assignment) で コンテキストから`params` だけを受ける
  return axios.get('http://develop.local:9900/posts/')
   .then((res) => {
      return {post: res.data.find(post => post.id === parseInt(params.id))}
   });
},
~~~  

### 2. async/await

~~~js
async asyncData ({ params }) {
    // 変数の分割代入(Destructuring assignment) で `data` を抜く
    let { data} = await axios.get('http://develop.local:9900/posts/')
    return { post: data.find(post => post.id === parseInt(params.id)) }
  },
~~~  

### 3. callback


~~~
callback(null, {<変数名>: <データ>})
~~~

~~~js
...
asyncData ({ params }, callback) {
  axios.get('http://develop.local:9900/posts/')
   .then((res) => {
      const post = res.data.find(post => post.id === parseInt(params.id))
      if (post) {
        callback(null, { post })
      } else {
        callback({ statusCode: 404, message: 'Post not found' })
      }
   });
},
~~~

## 関連

- [Process | Node.js v10.11.0 Documentation](https://nodejs.org/api/process.html#process_process)

## 記事

- [SSRしないNuxt.jsでページロード時に非同期部分を更新する方法 | なすびブログ](https://blog.nasbi.jp/programming/frontend/javascript/ssr%E3%81%97%E3%81%AA%E3%81%84nuxt-js%E3%81%A7%E3%83%9A%E3%83%BC%E3%82%B8%E3%83%AD%E3%83%BC%E3%83%89%E6%99%82%E3%81%AB%E9%9D%9E%E5%90%8C%E6%9C%9F%E9%83%A8%E5%88%86%E3%82%92%E6%9B%B4%E6%96%B0%E3%81%99/)
