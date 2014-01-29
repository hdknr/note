Date: 2013-08-31 16:00
Title:  CSS:LIR方式でSUBMITボタンを画像にする
Type: post  
Excerpt:   

フォームのボタンを画像にしたい。IEだと、

* history.back()で確認画面からその前のフォームの入力画面に戻れない
* buttonタグの name,valueを送ってくれないので、どのボタンでPOSTされたかサーバーで判断付かない
* が、inputタグだと name, valueを送ってくれる

ので、inputタグをCSSで画像に置き換えるのが楽。

LIR(Leahy/Langridge Image Replacement:リーフィー/ラングリッジ)式画像置換で SUBMITボタンを画像ボタンにする例：

    <html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <meta http-equiv="Content-Style-Type" content="text/css" />
      <style>
    
      /* LIR（Leahy/Langridge Image Replacement　リーフィー/ラングリッジ式画像置換） */
      .image-button {
          text-indent: -9999px;                             /* テキストを隠す       */ 
          overflow: hidden;                                 /* floatの指定が有る要素の親要素に高さを算出させる */
          display: block!important;                         /* 必ずブロック         */ 
          border:none!important;                            /* 必ずボーダー無し     */
          cursor: pointer;                                  /* カーソルを指に       */
          width: 248px; height: 58px;                       /* <input>サイズ        */
      }
      
      /* 背景にセンタリングしたイメージを設定(イメージサイズは .image-button と同じ) */
      #submit-reedit { background: url(submit-reedit.png) no-repeat; margin:0 auto; }
      #submit-commit { background: url(submit-commit.png) no-repeat; margin:0 auto; }
      
      #panel { width:500px;     margin: 0 auto;  }          /* パネルセンタリング   */
      #panel p.left  { float: left; display: inline; }      /* 左寄せ               */
      #panel p.right { float: right; display: inline; }     /* 右寄せ               */
    
      </style>
    </head>
    
    <body>
    
      <form>
        <div id="panel" class="clearfix">
            <p class="left">
                <input  type="submit" id="submit-reedit" class="image-button" name="submit-reedit"  value="修正する"/>
            </p>
            <p class="right">
                <input type="submit" id="submit-commit" class="image-button" name="submit-commit" value="登録する" />
            </p>
        </div>
      </form>
    
    </body>
    

参考:
    
* [Fahrner Image Replacement](https://en.wikipedia.org/wiki/Fahrner_Image_Replacement)
* [Revised Image Replacement](http://www.mezzoblue.com/tests/revised-image-replacement/)