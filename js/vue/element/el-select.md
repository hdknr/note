## 選択されていない時のスクロールポジションを指定する

年の選択支がおおいので、もっとも選択されやすい年の位置にスクロールさせる

`ref=yearSelect` で指定した `el-select`

~~~html
<el-select ref="yearSelect" v-model="selectedYear" @change="on_year">
  <el-option v-for="year in years" :label="year_label(year)" :key="year" :value="year"></option>
</select>
~~~

`mounted` で 1990 のあたりにスクロールさせるように設定

~~~js
mounted(){

  this.setScrollPosition(this.$refs.yearSelect, 1990);
  ...
}
~~~

実際の設定:

- `el-select` の `handleMenuEnter` をオーバーライドする
- `scrollToOption` に対して選択されていたらその `el-option` を渡す(デフォルトの処理)
- 選択がない場合、 `getOption(val)` で見つけた `el-option` を渡す

~~~js
methods: {
    setScrollPosition(selector, val){
      selector.handleMenuEnter = function(){
          const opt = selector.selected.value == null ? selector.getOption(val) :　selector.selected;
          selector.$nextTick(() => selector.scrollToOption(opt));
      };
    },
    ...
~~~  
