## フォーム検証

- [フォームデータの検証](https://developer.mozilla.org/ja/docs/Learn/HTML/Forms/Data_form_validation)

## ライブ検証

エラー設定:[setCustomValidity(https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/setCustomValidity):

~~~js
function seterror(elm, msg){
  elm.setCustomValidity(msg);               //  msg != '' ででエラー状態にする, = '' でクリア

  // Bootstrap4 のエラー状態
  if(msg == ''){
    $(elm).removeClass('is-invalid');       // エラーなし
  }else {
    $(elm).addClass('is-invalid');          // エラーあり
  }
}
~~~

検証(メールアドレス、確認入力):

~~~js
$(function(){

  function validate_email(elm){
    seterror(elm, '');                    // 一旦クリア

    // Check.1: メールアドレスルール
    if(! /\S+@\S+\.\S+/.test($(elm).val()) ){
      seterror(elm, '正しいアドレスを指定してください');
      return;
    }

    // Check.2: アドレス == 確認入力 判定
    const inputs = $(elm).closest('.email-block').find("input").map(function(i, e){
      return e;
    }).get();

    if($(inputs[0]).val() != $(inputs[1]).val()) {
      seterror(inputs[1], '同じアドレスを入力してください');
    } else{
      seterror(inputs[1], '');
    }
  }

  // emal-block のフィールド(input[name=email, email_confirm))
  // `input` イベントごとにライブ検証
  $(".email-block input").map(function(i, elm){
    elm.addEventListener("input", function(e){
      validate_email(e.target);
    }, false);
    validate_email(elm);
  });

});
~~~

## サブミット前に検証

- checkValidity(): エラーがセットされたフィールドがないかを検証
- reportValidity(): エラーが起きたフィールドでメッセージを表示(スクロール移動)

~~~js
$(function(){
  $("a.submit").click(function(e){
    e.preventDefault()  ;

    const form =  $(this).closest("form");
    if(!form[0].checkValidity()){
        form[0].reportValidity();
        return;
    }
    form.submit();
  })
});

~~~

## reportValidity は IE11 でサポートされません

~~~js
$(function(){

  function reportError(form){
    try{
      form[0].reportValidity();
    }catch(e){
      // IE11 対応
      const err = form.find(".is-invalid")[0];        // エラーがある先頭要素
      $('html, body').animate({scrollTop: $(err).offset().top }, 800);  // スクロール
    }
  }

  $("a.submit").click(function(e){
    e.preventDefault()  ;

    const form =  $(this).closest("form");
    if(!form[0].checkValidity()){
      reportError(form);
      return ;
    }
    form.submit();
  })
});
~~~

## `display:none` 内の要素対応

~~~
An invalid form control with input[name='email'] is not focusable.
~~~

例えば、メールアドレスの入力セットが 会社と自宅の２セットあって、 自宅を選んだ時だけ自宅のアドレスを検証する、というケース。


### 1. フラグの内容でエラーを初期化/検証する

 チェックボックスのトグルで エラーの初期化/検証
 - off:  `checkValidity` の時に例外が起きないようにする
 - on:  `checkValidity` の時エラー確認漏れが起きないようにする

~~~js
$(function(){

  // 自宅を連絡するチェックボックス
  $("form input[name=home-contact]").change(function(){
      const visible = $(this).prop('checked')
      $("#home-contact-block .email-block input").map(function(i, elm){
        if(visible){
          validate_email(elm);  // 検証する
        } else {
          seterror(elm, '');    // エラーをクリアする
        }
      });

  })
});
~~~

### 2. validate_email した時に `display:none` であればエラーがなかったことにする


~~~js
function seterror(elm, msg){
  if(!$("form input[name=home-contact]").prop('checked')){
    if($('#home-contact-block').has(elm)[0] != null ){
      // 自宅がチェックされていないときに、自宅のメールアドレスエラーが報告されたらエラーがなかったことにする
      msg = '';
    }
  }

  elm.setCustomValidity(msg);
  if(msg == ''){
    $(elm).removeClass('is-invalid');
  }else {
    $(elm).addClass('is-invalid');
  }
}
~~~
