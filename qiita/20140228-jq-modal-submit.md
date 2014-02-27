jQuery: フォームを送信する前に確認ダイアログを出す

Imageボタンで送信するフォーム:

    <div>
    <form id="main-form" method="get">
       <input type="image" src="harajuku_st.jpg" name="harajuku" />
       <input type="image" src="prince.jpg" name="prince" />
    </form>
    </div>

クリックしたら同意を促すダイアログ:

    <div class="modal-dialog" id="modal-for-form">
      <span class="button cancel">取消</span>
      <span class="button ok" >送信</span>
    </div>

jqueryでフォームのイメージボタンがクリックした時にダイアログを表示して同意したらサブミットするようにする。:

        // 最初はダイアログを表示しない
        $("div.modal-dialog")
            .dialog({autoOpen:false}); 
        
        // ボタン表示    
        $("div.modal-dialog .button").button();
            
        // キャンセルボタンでダイアログを閉じる
        $("div.modal-dialog .cancel").click(function(e){
            e.preventDefault();
            $(this).parents(".modal-dialog").dialog("close");
        });

        // OKボタンで、イメージボタンのgateをopenにする
        // modal-for に イメージボタンのセレクタが入っている
        $("div.modal-dialog .ok").click(function(e){
            e.preventDefault();
            dlg = $(this).parents(".modal-dialog");
            dlg.dialog("close");
            $(dlg.attr("modal-for"))
				.attr("gate","open")
				.click();
             
        });

        // フォームのイメージボタンが押されたら
        $("form input[type='image']").click(function(e){
            // gateが開いていたらフォームをサブミットする
            if ($(this).attr('gate') == 'open'){
                $(this).attr('gate','close');
                return true;
            }
            
            // 開いていないので、確認ダイアログをモーダルで表示
            // イメージボタンのセレクタをmodal-for にセット
            $("div#modal-for-form")
                .attr("modal-for", 
                    "form input[name='"+ $(this).attr("name") +"']")
                .dialog("open");

			// 今はフォーム送信しない
            return false;
        });
