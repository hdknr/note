## ファイルアップロード( input[type=file] )

注意:

- input[type=file] はスクリプトで値を設定できません。これはセキュリティ上のDOMの制約です
- よってユーザーがクリックしてファイルを選択して input[type=file]にファイルを割り付ける動作が必ず必要です

### 簡単なコンポーネント

- `value` でイメージファイルの保存先を指定してもらう
- `name` でフォームでの名前を指定してもらう
- ファイルが指定されたら、読み込んで、 `input` イベントで親に通知する(`value`として同期される)

~~~js
<template>
<div>
  <div v-show="!value">
    <input type="file" :name="name" @change="onFileChange">
  </div>

  <div v-if="value">
    <el-button type="warning" round @click="removeImage">変更</el-button>
  </div>
</div>
</template>

<style>
</style>

<script>
import Vue from 'vue'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ja';

Vue.use(ElementUI, {locale});

export default {
  name: 'image-input',
  props: ['value', 'name'],
  methods: {
     onFileChange(e) {
       var files = e.target.files || e.dataTransfer.files;
       if (!files.length)
         return;
       this.createImage(files[0]);
     },
     createImage(file) {
       var reader = new FileReader();

       reader.onload = (e) => {
         this.$emit('input', e.target.result);
       };
       reader.readAsDataURL(file);
     },
     removeImage: function (e) {
       this.$emit('input', null);
     }
   }
}
</script>
~~~


### 親

~~~html
<form ...>
  <div>
      <img :src="params.image"
        v-if="params.image" width="100px"/>                              <!-- 新しく指定されたらイメージを表示 -->

      <img :src="form.photo_url"
        v-else-if="form.photo_url" width="100px"
        @click="imagepop=true"/>                                         <!-- 既存のファイルがあったら表示/クリックしたら拡大写真 -->

      <i class="far fa-image" v-else></i>                                <!-- それ以外はプレースホルダーの画像 -->

      <el-dialog title="写真拡大" :visible.sync="imagepop">
          <img :src="form.photo">
      </el-dialog>
    </div>
  </div>

  <div>
    <p>あなたの顔写真</p>
    <image-input :name="'profile-photo'" :value="params.image" @input="on_image"></image-input>
  </div>
</form>
~~~            
