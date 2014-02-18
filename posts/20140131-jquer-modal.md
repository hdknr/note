Date: 2014-01-31 11:30
Title:  jQuery: ダウンロードの許諾をとる
Type: post  
Excerpt:   


ダイアログをHTMLに仕込む:

    <div id="dialog-confirm">
       <div class="message" style="margin:50px" ></div>
       <div class="buttons">
          <a class="cancel" hef="#">取消</a>
          <a class="ok" hef="#">はい</a>
       </div>
    </div>

スクリプト:

    <script >
    $(function(){
   
     $("#dialog-confirm a").button();       // アンカーをボタンに

     $("#dialog-confirm").dialog({autoOpen: false }) // 隠しダイアログにする
     .find("a.cancel").click(function(e){   // 取消
       e.preventDefault();
       $("#dialog-confirm").dialog("close"); // ダイアログをクローズ
     });
   
     $("a.do_modal[href]:not(#dialog-confirm a)").click(function(e){    //アンカーをクリックしたら
       e.preventDefault();
       $("#dialog-confirm div.message").text( $(this).attr("message") ); // ダイアログのメッセージ
       $("#dialog-confirm")
       .dialog("option","title", $(this).text() )   // タイトル
       .dialog("open")
       .find("a.ok").attr({href: this.href, target: this.target})   // OKのアンカーにURLをセット
       .click(function(e){
         $("#dialog-confirm").dialog("close");  // ダイアログを閉じる
       });
     });
    });
    </script>

ダウンロードアンカー:

    <a class="do_modal"
         message="ダウンロードしますか？"
         href="./donwload">一覧ダウンロード</a>
