## スムーススクロール

- https://github.com/Teddy-Zhu/vue-smoothscroll

~~~bash
$ yarn add vue-smoothscroll
~~~

~~~js
...
import VueSmoothScroll from 'vue-smoothscroll'

Vue.use(VueSmoothScroll)
...
~~~


~~~js

  methods:{
      ...
      scrollTo(id){
          this.$SmoothScroll(document.getElementById(id), 800);
      }
      ...
  }
~~~


~~~html
<input
  v-model="agreed"
  @change="scrollTo('scroll-submit')"
  type="checkbox" class="checkbox" name="agreed" />  

...
  <a name="submit" id="scroll-submit" ></a>
  <input type="submit"...>

~~~
