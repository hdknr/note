## 基本

- [Bootstrap使い方メモ１（基本＋CSS）](http://qiita.com/opengl-8080/items/2764b6db143b1a4411f6)

## 画面作成

- [15 Bootstrap Frameworks for Developers](http://codecondo.com/bootstrap-frameworks-for-developers/)

レイアウト

- [レイアウト www.layoutit.com](http://www.layoutit.com/)
- [jetstrap.com](https://jetstrap.com/)(有料)
- [pingendo.com](http://pingendo.com/)

カラー

- [カラーパターン lavishbootstrap.com](http://www.lavishbootstrap.com/)

CSS

 - [bootswatchr.com](http://bootswatchr.com/)


## メール

- [advancedrei/BootstrapForEmail](https://github.com/advancedrei/BootstrapForEmail)


## フォーム

- [bootstrap3で横並びのボックスを実現する方法
](http://qiita.com/fagai/items/d25357a52adb4cfc6ba4)

- [Bootstrap inline form button alignment](https://stackoverflow.com/questions/22102493/bootstrap-inline-form-button-alignment)

- [Bootstrap’s .form-horizontal with nested rows](http://output.jsbin.com/kemumu/1/)

### 水平方向で上向きに合わせる

~~~css
.form-inline fieldset > .form-group {
    vertical-align: top;
}
~~~
~~~html
form class="form-inline" method="get">
<fieldset>
  <legend>{% trans 'Search Alumnus' %}</legend>
    <div class="form-group">
      <input class="form-control" placeholder="First Name" name="firstname" type="text" />
    </div>

    <div class="form-group">
      <input class="form-control" placeholder="Last Name" name="lastname" type="text" />
    </div>
    ....
</fieldset>
</form>
~~~

## INPUTを横並びに

~~~html
<div class="form-group has-success">
    <label class="control-label" for="id_grad_year_0">Grad year</label>
    <div class="input-group">
    <input class="form-control" id="id_grad_year_0" name="grad_year_0" title="" type="text">
     <span class="input-group-addon">-</span>
    <input class="form-control" id="id_grad_year_1" name="grad_year_1" title="" type="text">
    </div>
</div>
~~~

## テーブル

- [wenzhixin/bootstrap-table-examples](https://github.com/wenzhixin/bootstrap-table-examples)
