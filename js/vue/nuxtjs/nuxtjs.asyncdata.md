## [asyncData](https://ja.nuxtjs.org/api/)

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
