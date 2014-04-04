jQuery: POSTだけではなくAnchorでもモーダルダイアログを出せるようにする

[改造](http://qiita.com/hidelafoglia/items/adf786fdff632b9b95e7)

HTML. dialog="ダイアログセレクタ" でダイアログを指定する:

    <form id="main-form" method="get">

       <!-- ボタンでダイアログをだす -->
       <input id="id-harajuku" class="modal" dialog="#id-modal-post" 
        type="image" src="harajuku_st.jpg" name="harajuku" />

       <input id="id-prince" class="modal" dialog="#id-modal-post"
        type="image" src="prince.jpg" name="prince"   />

       <hr/> 

       <!-- アンカーでもダイアログを出す -->
       <a id="id-google" class="modal" dialog="#id-modal-get" 
        href="http://www.google.com"> Google</a>

       <a id="id-home" class="modal" dialog="#id-modal-get"
        href="index.html?home" >Home</a>
    </form>



HTML :

    <div class="modal-dialog" id="id-modal-post">
      <span class="alert">よろしければデータを送信します</span>
      <span class="button cancel">取消</span>
      <span class="button ok" >送信</span>
    </div>

    <div class="modal-dialog" id="id-modal-get">
      <span class="alert">よろしければサイトに移動します</span>
      <span class="button cancel">取消</span>
      <span class="button ok" >送信</span>
    </div>


スクリプト:

    $(function(){

        $("div.modal-dialog")
            .dialog({autoOpen:false});

        $("input.modal,a.modal").click(function(e){ 
            clicker = $(this);
            if ( clicker.attr('gate') == 'open'){
                clicker.attr('gate','close');
                if(clicker.prop('tagName').toUpperCase() == 'A')
                    // return true だと移動しない...
                    window.location = clicker.attr('href');
                return ;    
            }

            dialog = $(clicker.attr("dialog") );
            dialog.dialog('open');

            dialog.find('.ok').click(function(e){
               dialog.dialog("close");
               clicker.attr("gate","open").click();
            }).button();

            dialog.find('.cancel').click(function(e){
              dialog.dialog("close");
            }).button();

            e.preventDefault() ;
        });

    });
