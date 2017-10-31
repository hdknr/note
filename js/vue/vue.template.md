## テンプレートがマウントされない

コンテナタグがないのでは？:

以下のような場合、 `sub-component` のテンプレートがロードされない. `.container`の部分のみがレンダリングされる:

~~~html
<script type="text/x-template" id="picker-template">
  <div class="container">
      ....
  </div>
  <sub-component> </sub-component>
</script>
~~~

`div` とかで囲うとロードされる:

~~~html
<script type="text/x-template" id="picker-template">
<div>
  <div class="container">
    ....
  </div>
  <sub-component> </sub-component>
</div>
</script>
~~~
