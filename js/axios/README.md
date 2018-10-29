
# axios

- https://github.com/axios/axios
- [#69](https://github.com/hdknr/scriptogr.am/issues/69)

## Tips

- [クエリパラメータ](axios.queryparameter.md)
- [プロミス](aixos.promise.md)

## POST(PUT, PATCH)

### 1. JSON

~~~js

updateInstance(instance, endpoint, method){
  var config = {};
  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';
  return axios[method](endpoint, instance, config).then((res) =>{
      // do something....
  });
}
~~~

### 2. Form + File

~~~js
  uploadData(instance){
    var vm = this;
    var formData = new FormData();
    ['access', 'data', 'tags', 'filename', 'title'].forEach((i) => {
       val = instance[i];
       if (instance.id){    //Update
         if(vm.original[i] != val){
              // 更新されたフィールドのみ
             formData.append( i,  (i == 'tags') ? vm.tags_json : val);
         }
       }else { // New
         formData.append(i,  val);
       }
    });
    return formData;
  }
  uploadInstance(instance, endpoint, method){
      var vm = this;
      var config = {headers: {'content-type': 'multipart/form-data'}};
      var data = uploadData(instance);

      axios.defaults.xsrfCookieName = 'csrftoken';
      axios.defaults.xsrfHeaderName = 'X-CSRFToken';
      axios[method](endpoint, data, config)
        .then(function(res) {vm.$refs.dialog.hide(); })
        .catch(function(error){console.log(error.response); });
  }
~~~

ちなみにアップロードファイルの更新があったら

~~~js
onFileChanged(e){       // From INPUT[type=file] の変更イベントハンドラ
    var files = e.target.files || e.dataTransfer.files;
    var image = new Image();
    var reader = new FileReader();
    var vm = this;
    reader.onload = function(e) {
        // ファイルの読み込みが完了したら...
        var img = {thumbnail: e.target.result, uploadFile: file, name: file.name};
        vm.image = img; // イメージオブジェく音を作る
    };
    reader.readAsDataURL(file);
},
~~~

### 3. Form ファイルなし

- application/x-www-form-urlencoded

~~~js
var config = {headers: {'content-type': 'application/x-www-form-urlencoded'}};
~~~
