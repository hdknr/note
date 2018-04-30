電話番号(nnnn-nnnn-nnnn)の入力

## HTML

- 実際のフィールドは '-' 区切りの電話番号で、`hidden` フィールドに入れる
- UIの入力３フィールドをjavascriptで処理する

~~~html
<div class="form-group row">
     <label for="id-profile-mobile_phone" class="col-sm-2 col-form-label">携帯電話</label>
     <div class="col-sm-4 phone-fields">
       <input  id="id-profile-phone" type="hidden" name="profile-mobile_phone" value="{{ profile.mobile_phone|default:'' }}" />

       <dl>
         <dd>
           <input type="tel" class="form-control grouped-field" size="5" maxlength="5">
           <span class="form-control-static">-</span>
         </dd>
         <dd>
           <input type="tel" class="form-control grouped-field" size="4" maxlength="4">
           <span class="form-control-static">-</span>
         </dd>
         <dd>
           <input type="tel" class="form-control grouped-field"  size="4" maxlength="4">
         </dd>
       </dl>
     </div><!-- /.phone-fields-->
</div><!-- /.form-group-->
~~~

## CSS

横並びにする:

~~~css
<style>
.phone-fields .grouped-field { width: auto; text-align: center; border: 1px solid #CCC; float: left; }
.phone-fields span { float: left; display: inline-block; margin-left: .5em; margin-right: .5em;}
</style>
~~~


## javascript

~~~js
$(function(){

    // 既存データで初期化
    $(".phone-fields input:hidden").map(function(index, elm){
       const vals = $(elm).val().split('-');
       const container = $(elm).closest('.phone-fields');
       if(vals.length == 3){
         const items = container.find('input.grouped-field');
         items.map(function(index, elm){
           $(elm).val(vals[index]);
        });
      }
    });

    // 変更処理
    $(".phone-fields input.grouped-field").change(function(){
      const container = $(this).closest('.phone-fields')
      const items = container.find('input.grouped-field');

      const vals = items.map(function(index, elm){
        const v = $(elm).val();
        return (v.length > 0 ) ? v :null;     // nullだと追加されない
      }).get();                               // get() をすると object -> array

      if(vals.length == 3){
        container.find('input:hidden').val(vals.join('-'));
      }
    });
})
~~~
