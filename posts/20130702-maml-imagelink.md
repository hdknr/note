Date: 2013-07-02  11:30
Title:  Sandcastle Help File Builder : 画像を入れる
Type: post  
Excerpt:   

[Sandcastle Help File Builder](https://shfb.codeplex.com/)で画像を入れるには、MAML(.aml)ファイルに /imagelink/image タグを書き込むと良いみたい。


        <para>
			<mediaLink>
          		<image placement="center" xlink:href="chibi"/>
        	</mediaLink>
        </para>


でな感じで。 .amlと同じパスにある chibi.png が読み込まれます。


	 C:\Users\Administrator\Documents\Visual Studio 2012\Projects\chibi\Docs のディレクトリ

	2013/07/02  11:17    <DIR>          .
	2013/07/02  11:17    <DIR>          ..
	2013/07/02  10:44            26,706 chibi.png
	2013/07/02  11:17             3,744 Chibi.shfbproj
	2013/07/02  11:17             5,318 Chibi.shfbproj_Administrator
	2013/07/02  11:15             3,708 Conceptual.aml
	2013/07/02  10:28               165 Content Layout.content
	2013/07/02  11:17    <DIR>          Help
	               5 個のファイル              39,641 バイト
	               3 個のディレクトリ  14,938,828,800 バイトの空き領域