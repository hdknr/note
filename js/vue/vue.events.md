## `@change` で変更を処理すること


`@click` だとクリック直後に発火するので、 `v-model` の反映が間に合わない

~~~html
<input type="checkbox" @click="$emit('on-select', image)" v-model="image.selected">
~~~

以下のハンドラで、期待と逆の判定がされてしまう:

~~~js
  image_selected(image){
      if(image.selected){
          //  チェックされた
      } else {
          // 解除された
      }
  }
~~~

`@change` に変える

~~~html
<input type="checkbox" @change="$emit('on-select', image)" v-model="image.selected">
~~~

## v-model 

- `@input` に対して、 `$event` を引数としてコールバックされる

~~~html
<input v-model="date">
~~~

~~~html
<input :value="date" @input="onDateChange($event.target.value)">
~~~