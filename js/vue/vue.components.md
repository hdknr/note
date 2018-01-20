- [コンポーネント](https://jp.vuejs.org/v2/guide/components.html)

## 双方向バインド(`v-model` + `$emit("input", newValue)`)

- 基本的には 親 -> 子の単横方で、 子 -> 親 はない
- が、 `v-model` を使えば双方向`っぽく`動く
- 子の中で、 `$emit('input', newValue)` すればVueが親の値を変更してくれる


    ... v-model is just syntactic sugar for v-bind:value and v-on:input.

親:

~~~html
<mymedia-inplace-edit
  v-model="content.title">   {# title属性を双方向バインドする #}
</mymedia-inplace-edit>
~~~


子(さらにINPUTコンポーネントと双方向バインドしている):

~~~html
<b-form-input
  type="text"
  required="true"
  @change="editing=false; $emit('input', $event);"     {# 変更イベントがおきたら新しい値を input イベントで emmit する#}
  v-model="value"                                      {# 実際の入力処理: 子valueをINPUTと双方向バインドする #}
>
</b-form-input>
~~~


## サブコンポーネントの更新

- 自身が管理している配列(`albums`)の更新があった時に、 サブコンポーネント(`mymedia-album`, `mymedia-dropload`) の内容を更新する
- `Vue.set` で関連するコンポーネントに変更が会ったことを伝える
- `$forceUpdate` で自身のテンプレートに対して更新を伝える

~~~html
    <mymedia-album
        :modal-state="true"
        :mediafiles="album.mediafiles">
    </mymedia-album>

    <mymedia-dropload :album="album"></mymedia-dropload>
~~~

~~~js
  components: {
    'mymedia-album': AlbumComponent,
    'mymedia-dropload': DroploadComponent
    ...
  },
  data:{
    ...
    albums: []
  },
  methods: {
    updateAlbum(album){
      var url = this.get_endpoint(album);
      var vm = this;
      var config = {};
      axios.defaults.xsrfCookieName = 'csrftoken';
      axios.defaults.xsrfHeaderName = 'X-CSRFToken';
      var method = album.id ? 'patch': 'post';
      return axios[method](url, album, config).then((res) =>{
          vm.albums[vm.albums.indexOf(album)] = res.data;
          Vue.set(vm, 'albums', Object.assign([], vm.albums));    //
          vm.$forceUpdate();
      });
    },
    ...
  },
~~~      

## コンポーネントのクラスを生成

~~~js
var app = new Vue({
  components: {
    'myarticles_article' : myArticlesArticle,
    'myarticles_section' : myArticlesSection,
    ....
  },
}
~~~

~~~js
get_component(element){
  // element.content_type がコンポーネント名と 1:1 で定義されている
  return new Vue(this.$options.components[element.content_type]);
}
~~~

## コンポーネントネーミング

- [vue: スタイルガイド](https://jp.vuejs.org/v2/style-guide/index.html)
- [Vueコンポーネントの強く推奨される名付け方](https://qiita.com/suin/items/e4d6a0e0d4912fbf9b77)
