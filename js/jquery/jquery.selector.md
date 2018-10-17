# セレクタいろいろ

## チェックされていない `radio` もしくは `checkbox` をすべて一覧

~~~js
// フォームデータのリスト化
var data = $('#form-main').serializeArray();

// リストを辞書に変換(underscore.js)
var data_obj = _.object(
    _.map(data, function (i) {
        return [i.name, i.value]
    }));

// image, button, submit 以外の typeで、 チェックされていない input 
$("#form-main input:not([type=image],[type=button],[type=submit],:checked)").each(function(){

    // チェックされていない radio button
    if (!(this.name in data_obj)) {
            data_obj[this.name] = '';
    }
});
~~~


## 記事

- [jquery: find element whose id has a particular pattern](http://stackoverflow.com/questions/1487792/jquery-find-element-whose-id-has-a-particular-pattern)
