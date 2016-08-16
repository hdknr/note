- [jQueryでフォームをAjax送信する際の基本パターンのチュートリアル。二重送信の防御とか。](http://ginpen.com/2013/05/07/jquery-ajax-form/)


## 再編集ボタンでPOSTするときに必須チェックスクリプトを回避

- 再編集`INPUT` を強制追加して送信

~~~js
$(function(){
  $("#edit-again").click(function(){
    var input = $("<input>").attr("name", "edit-again").val("edit-again");
    $("#form-upload").append(input).submit();
  })
});
~~~
