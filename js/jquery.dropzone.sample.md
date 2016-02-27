- [【JavaScript】ドラッグ＆ドロップで画像を非同期アップロードできるライブラリ dropzone.js の デフォルトCSS を有効にしたままカスタマイズする](http://d.hatena.ne.jp/pospome/20130713/1373699451)
- [pospome/DropzoneJsSample](https://github.com/pospome/DropzoneJsSample)

~~~html
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8">
	<title></title>
	<link rel="stylesheet" href="./css/dropzone.css"/>
	<script src="./jquery.js"></script>
	<script src="./dropzone.js"></script>
	<script src="./upload.js"></script>

	<style>
		#image_drop_area{
			background-color:#ffffe0;
			width:300px;
			height:200px;
		}
		#preview_area{
			background-color:#e6e6e6;
			min-height:200px;
			width:600px;
		}
	</style>
</head>
<body>

<!-- ここにドロップします --->
<div id="image_drop_area">DROP ZONE</div>

<!-- ここでプレビューします -->
<div id="preview_area" class="dropzone-custom"></div>

</body>
</html>
~~~

~~~js
$(function(){
	$('#image_drop_area').dropzone({
		url:'./api.php',
		paramName:'file',
		maxFilesize:1, //MB
		addRemoveLinks:true,

		previewsContainer:'#preview_area',      // ここでプレビューします
		thumbnailWidth:100, //px
		thumbnailHeight:100, //px

		uploadprogress:
      function(_file, _progress, _size){
			_file.previewElement.querySelector(
          "[data-dz-uploadprogress]").style.width = "" + _progress + "%";
		},

		success:
      function(_file, _return, _xml){
			//引数の _return には サーバ側 で出力(echo or print)された値が格納される。
			//サーバ側のエラーを検知するのに使うといい。
			_file.previewElement.classList.add("dz-success");
		},

		error:
      function(_file, _error_msg){
			var ref;
			(ref = _file.previewElement) != null ? ref.parentNode.removeChild(_file.previewElement) : void 0;
		},

		removedfile:
      function(_file){
			var ref;
			(ref = _file.previewElement) != null ? ref.parentNode.removeChild(_file.previewElement) : void 0;
		},

		previewTemplate:
      "<div class=\"dz-preview dz-file-preview\">\n  <div class=\"dz-details\">\n    <div class=\"dz-filename\"><span data-dz-name></span></div>\n    <div class=\"dz-size\" data-dz-size></div>\n    <img data-dz-thumbnail />\n  </div>\n  <div class=\"dz-progress\"><span class=\"dz-upload\" data-dz-uploadprogress></span></div>\n  <div class=\"dz-success-mark\"><span>&#10004;</span></div>\n  <div class=\"dz-error-mark\"><span>&#10008;</span></div>\n  <div class=\"dz-error-message\"><span data-dz-errormessage></span></div>\n</div>",

		dictRemoveFile: '削除',
		dictCancelUpload:'キャンセル'
	});
});
~~~

## dropzone

~~~html
<div id="dropzone">
  <form action="/upload" class="dropzone needsclick" id="demo-upload">
  <div class="dz-message needsclick">
   Drop files here or click to upload.<br />
   <span class="note needsclick">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
 </div>
  </form>
</div>
~~~
