- [http://www.dropzonejs.com/](http://www.dropzonejs.com/)

## 作成

- Dropzoneクラス

~~~js
// Dropzone class:
var myDropzone = new Dropzone(
    "div#myId",
    { url: "/file/post"});
~~~

- jQuery

~~~js
$("div#myId").dropzone({ url: "/file/post" });
~~~


## 設定

### = Dropzone.options ================

- HTMLでの要素IDをで、設定オブジェクトを与えることができます

~~~html
<div id="myAwesomeDropzone"></div>
~~~

~~~js
Dropzone.options.myAwesomeDropzone = {
  paramName: "file", // The name that will be used to transfer the file
  maxFilesize: 2, // MB
  accept: function(file, done) {
    if (file.name == "justinbieber.jpg") {
      done("Naha, you don't.");
    }
    else { done(); }
  }
};
~~~

- 設定オブジェクトの制御

~~~js
Dropzone.options.myAwesomeDropzone = false;     // 無効にする

Dropzone.autoDiscover = false;    // 自動検知を無効にする
~~~

### = 設定オプション ================

#### url

- `<form action=...>` でURLを指定しない場合にURLを指定できる。
- 関数でも定義できます

~~~js
function(files){
  ///......
  return "/upload/files";
}
~~~

#### method

- デフォルトは`POST` ですが、`PUT` に変更できます
- `url`と同じように関数でも定義できます

~~~js
function(files){
  ///......
  return "PUT";
}
~~~

#### parallelUploads

- 同時アップロード数を指定します
- (See the Enqueuing file uploads section for more info))

#### maxFilesize

- MB 単位で指定

#### filesizeBase

- デフォルト == 1000
- 1024 にしてもいい

#### paramName

- 転送パラメータ名
- デフォルト `file`

#### uploadMultiple

-  'true' にすると複数ファイルをアップロードする
-  (See the events section for more information.)


#### headers

- リクエストヘッダーにフィールドを追加

~~~
headers: { "My-Awesome-Header": "header value" }
~~~

#### addRemoveLinks

- 'true' にするとプレビューに削除/取り消しリンクを追加可能
- dictCancelUpload, dictCancelUploadConfirmation, dictRemoveFile がつかわれます

#### previewsContainer

- プレビューエレメント
- `null` だとDropzone のエレメントが使われます
- `dropzone-previews` クラスを要素に指定すること

~~~html
<div class="dropzone-previews" ...>
~~~

#### clickable

- Dropzoneがクリック可能かどうか？(`true`/`false`)

#### createImageThumbnails

- ???

#### maxThumbnailFilesize

- サムネールを作成する上限(Mbyte)

#### thumbnailWidth

- `null` だと自動計算

#### thumbnailHeight

- thumbnailWidthと同様
- ともに`null` だとリサイズされない

#### maxFiles

- 指定されると(`null`じゃないと)ファイル数を制限
- 上限を越えると `maxfilesexceeded` が呼ばれる
- `dz-max- files-reached` クラスの要素にフィードバックできる

#### resize

- リサイズ情報を決定するために呼ばれるコールバック暗数の定義

~~~js

function(file){
    /....
    return {
    rcX: 100 , srcY: 100, srcWidth:100, srcHeight: 100};
}

~~~

#### init

- Dropzone が初期化された時のコールバック

#### acceptedFiles

- `accept`
- デフォルトではファイルの拡張子で自動決定(image/*,application/pdf,.psd....)


#### accept

- accept したときのコールバック関数

~~~js
function(file, done){
    ///
    if( success )
        done();
    else
        done(error_message);
}
~~~

#### autoProcessQueue

- `false` だと `myDropzone.processQueue()` を明示的に呼ぶこと
- (See below for more information on handling queues.)

####  previewTemplate

- プレビューテンプレート

#### forceFallback

- デフォルト `false`
- `true` だとフォールバックさせる

#### fallback

- フォールバック関数

#### dictDefaultMessage

- ファイルがドロップされる前のメッセージ
- デフォルト:  "Drop files here to upload"

#### dictFallbackMessage

- デフォルト: "Your browser does not support drag'n'drop file uploads"

#### dictFallbackText

- デフォルト: "Please use the fallback form below to upload your files like in the olden days."

#### dictInvalidFileType

- ファイルタイプが一致しない時のメッセージ

#### dictFileTooBig

- Shown when the file is too big. {{filesize}} and {{maxFilesize}} will be replaced.

#### dictResponseError

- Shown as error message if the server response was invalid. {{statusCode}} will be replaced with the servers status code.

#### dictCancelUpload

- addRemoveLinks == true のとき
- 取り消しリンクのテキスト


#### dictCancelUploadConfirmation

- addRemoveLinks == true のとき
- 取り消しの時

#### dictRemoveFile

- addRemoveLinks == true のとき
- 取り消しの時


#### dictMaxFilesExceeded

- maxFilesがセットされたとき
- 超えたメッセージ

#### drop

- `drop` イベントハンドラもオーバーライドできます


### = レイアウト ============

- [デモ](http://www.dropzonejs.com/bootstrap.html)
- 以下のようになります
- `previewTemplate` で設定可能です
- 要素には data-dz-* 属性を入れます

~~~html
<div class="dz-preview dz-file-preview">
  <div class="dz-details">
    <div class="dz-filename"><span data-dz-name></span></div>
    <div class="dz-size" data-dz-size></div>
    <img data-dz-thumbnail />
  </div>
  <div class="dz-progress"><span class="dz-upload" data-dz-uploadprogress></span></div>
  <div class="dz-success-mark"><span>✔</span></div>
  <div class="dz-error-mark"><span>✘</span></div>
  <div class="dz-error-message"><span data-dz-errormessage></span></div>
</div>
~~~

- 関数の`file` パラメータで アクセス可能です

~~~js
file.previewElement
~~~

- 削除リンクは以下のように入れます

~~~html
<img src="removebutton.png"
  alt="Click me to remove the file."
  data-dz-remove />
~~~



#### dz-preview

- コンテナ
- アップロード中は `dz-processing` クラスが設定される
- アプロードが終わると `dz-success`  クラスが設定される
- エラーでおわると `dz-error`  クラスが設定される
- サーバーがおくったエラーメッセージは `data-dz-errormessage`クラスの要素にセットされる

## イベント
