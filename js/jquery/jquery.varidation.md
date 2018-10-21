# バリデーション

- デカすぎるフォームの対応
- jQuery + Bootstrap +(underscore.js + jsRender) の場合

## 1. ルールを定義する

- 単体フィールドチェック行う
- 相関チェックはコードで書く

単体フィールドルールの例:

~~~yml
- id: 38
  name: office_name
  required: false
  regex: ^.{1,10}$
~~~

### ルールのレンダリング

JSONで `script` にレンダリングする。

~~~html
<script type="application/json" id="json-data">
{
  "field_meta": {{ fieldmeta|jsonize|safe }},
}
</script>
~~~

### ルールの読み込み

~~~js
// pageData.field_meta でスクリプトからアクセスできる
var pageData = JSON.parse(document.getElementById("json-data").textContent);
~~~

## 2. エラー処理(エラーが発生したら)

エラー時:

- エラー文言を書いた `.invalid-feedback` を表示させる ( `display: block`  スタイルを追加 )
- 入力ブロックに ボーダースタイルを追加する ( `border border-danger` とか)

その他:

- エラーチェックする前に一旦すべてリセットし、エラーのフィールドに関して上記を行う
- セレクタで引っかけやすいように上記のタグには、 例えば `err-フィールド名` とかを追加して奥

コード:

~~~js
// エラー表示のクリア
function resetAllErrors(){
    $(".border,.border-danger").removeClass('border border-danger');
    $(".invalid-feedback").css('display', 'none');
}
// エラーの設定
function setError(name){
    $("div.err-" + name).addClass('border border-danger');
    $("small.err-" + name).css('display', 'block');
}
~~~

### フィールドチェッカー

- フォームデータごとにフィールドチェッカーを通す

~~~js
function findFieldErrors(data_obj){
    // エラー確認
    var errors = _.omit(
        data_obj,
        function (value, name) {
            return check_field(name, value);
        });
    return errors;
}
~~~

~~~js
// 単体フィールドエラー
function check_field(field, value, is_required) {
    var def = pageData.field_meta[field]; // フィールド情報
    if (def) {
        if (value) {
            return new RegExp(def.regex).test(value);
        }
        // 以下の優先
        // 1) 呼び出しの必須チェック
        // 2) YAMLでの required 定義
        // 3) 必須ではないがデフォルト
        is_required = is_required || def.required || false;
        if (is_required){
            return false;
        }
    }
    return true;
}
~~~

### 相関関係エラー

例) ３つのアドレスはそれぞれオプションだが、どれか１つは指定すること:

- エラーが起きたら `email3` というタグ名でエラー表示させる

~~~js
// メールアドレス:3のうちどれか必須
function check_emails(data_obj){
    var errors = _.filter(
        ['pc_email', 'office_email', 'mobile_email'], 
        function(i){ return check_field(i, data_obj[i], true) ;});

    if(_.isEmpty(errors)) {
        return {'emails3': errors};
    }
    return {};
}
~~~

相関エラーをフィールドエラーにマージさせる:

~~~js
function findErrors(data_obj){
    var errors = findFieldErrors(data_obj);
    errors = _.extend(errors, check_emails(data_obj));  // 3メールアドレス確認
    return errors;
}
~~~

## 3. エラーがなければ確認画面表示

- Bootstrap のモーダル表示させる
- テンプレートを使って流し込めるようにする

### テンプレート( jsRender https://www.jsviews.com/ の場合)

`text/x-jsrender` の `script` ブロックに定義する
~~~html
<script id="confirm-template" type="text/x-jsrender">
  {% include 'accounts/register/confirm.template.html' %}
</script>
~~~

confirm.template.html には、 Bootstrap モーダルのHTMLを jsRenderの記法で記載する。

レンダリング:

~~~js
function  renderConfirm(data_obj){
    var template = $.templates("#confirm-template");    // テンプレートをscriptブロックから読み込み
    var innerHtml = template.render(data_obj);          // テンプレートに対してフォームデータ(data_obj)でレンダリング
    $("#form-confirm form").html(innerHtml);            // html を動的に埋め込む
}
~~~

## 4. フォームデータの取得

- `serializeArray` をつかう
- チェックされていないradio, checkbox は上記で取得できないので、チェックされていない要素を探しで、ブランクでセットする

~~~js
// underscore.js をつかってる
function getFormData(form){
    // フォームデータ
    var data = form.serializeArray();
    var data_obj = _.object(
        _.map(data, function (i) {
            return [i.name, i.value]
        }));

    form.find("input:not([type=image],[type=button],[type=submit],:checked)").each(function(){
        // チェックされていない radio button
        if (!(this.name in data_obj)) {
            data_obj[this.name] = '';
        }
    });
    return data_obj;
}
~~~

## 5. バリデーション

~~~js
// 確認処理
$('button[name=confirm]').click(function () {
    // リセット
    resetAllErrors();

    // フォームデータ取得
    var data_obj = getFormData($('#form-main'));

    // エラー確認
    var errors = findErrors(data_obj);

    if (!_.isEmpty(errors)) {
        // エラー表示
        _.map(errors, function (value, name) {setError(name);});
    } else {
        renderConfirm(data_obj);
        // ポップアップ
        $('#form-confirm').modal('show');
    }
});
~~~

## 6. 送信

- 確認ポップアップのボタンがクリックされたら入力フォーム(`#form-main`) を `submit` する
~~~js
$('#form-confirm button[name=submit]').click(function () {
    $('#form-main').submit();
});
~~~