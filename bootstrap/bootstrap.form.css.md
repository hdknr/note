## input-group: 入力フィールドを並べる

~~~html
<div class="input-group">
    <input type="text" class="form-control" placeholder="Start"/>
    <span class="input-group-addon">-</span>
    <input type="text" class="form-control" placeholder="End"/>
</div>
~~~

- [Input group](http://v4-alpha.getbootstrap.com/components/input-group/)
- [インプット・グループ](http://bootstrap3.cyberlab.info/components/inputGroups.html)


## Radioボタンを横並びに変える

~~~js
$("input[type=radio]")
  .parent('label')
    .parent('div')
      .addClass('radio-inline');
~~~

## radio-inline の左マージンがきになる

~~~css
.radio,
.checkbox {
    padding-left: 20px;
}
.radio label,
.checkbox label {
    display: inline;
    padding: 0;
}
~~~
