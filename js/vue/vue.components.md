- [コンポーネント](https://jp.vuejs.org/v2/guide/components.html)


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
