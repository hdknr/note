Date: 2014-02-14 16:30 
Title: PowerShell: VisualBasic のライブラリをロードして呼んでみる  
¥Type: post  
Excerpt:   


コード xxx.ps1:

    $asm = [System.Reflection.Assembly]
    [void] $asm::LoadWithPartialName("Microsoft.VisualBasic")
    
    $strnv = [Microsoft.VisualBasic.VbStrConv]
    $strings = [Microsoft.VisualBasic.Strings]
    
    $strings::StrConv("アイウエオ",$strnv::Hiragana )


実行:

	PS C:\Users\hdknr\Documents\Share\note> 
		C:\Users\hdknr\Documents\Share\note\xxx.ps1

	あいうえお
