- [autocomplete](https://jqueryui.com/autocomplete/)
- [jQuery autoComplete view all on click?](http://stackoverflow.com/questions/1268531/jquery-autocomplete-view-all-on-click)


## オブジェクトリストをAjaxで取得

~~~js
$( "#id_food_menu" ).autocomplete({
 source: function( request, response ) {
      $.ajax({
          dataType: "json", type : 'Get',
          url: "{% url 'bar_foodmenu' %}", // Django URL
          success: function(data) {
              response( $.map( data, function(item) { return item.name; }));
          },
          error: function(data) { /* error handling */}
      });
  },
  select: function( event, ui ) { /* debug ... */ }
});
~~~

### クリックしたら全一覧

- 現在の値で `search` する

~~~js
$("#id_food_menu").focus(function() {
   $(this).autocomplete('search', $(this).val());
 });
~~~


## 少なめの選択肢をあらかじめページロード時にキャッシュする方式

- `$.ajax` 自体は基本的にはキャッシュするはず

~~~html
{% block head_style%} {{ block.super }}
<link href="{% static 'jquery-ui/themes/smoothness/jquery-ui.css' %}" rel="stylesheet">
{% endblock %}


{% block bottom_script %} {{ block.super }}
<script src="{% static 'jquery-ui/jquery-ui.min.js' %}"></script>
<script>
  $(function() {
    // ページロードした時にデータを取得しておく / 取得 URL は {{ office_json }}
    $.ajax({
      dataType: 'json', type: 'Get', url: "{{ office_json }}",
      success: function(data){
          var offices = data;         // 取得されたらキャッシュする

          $("#id_office").autocomplete({  // オートコンプリートを設定
            minLength: 1,
            source: function(request, response){
                // 入力(request.term)で絞り込む
                var results = offices.filter(function(item){
                      // 複数文字をカンマか空白で区切ってAND条件
                      var words = request.term.split(/[\s,\u3000]/);
                      return words.filter(
                          function(i){ return i == '' || item.name.indexOf(i) != -1 ;}
                      ).length == words.length;
                    }).map(function(item) { return item.name; });

                response(results);  // 絞り込んだ結果を設定
              },
            // 選択されたらchangeイベント発火
            select: function( event, ui ){
                $(this).val(ui.item.value).change();
          });
      }
    });

    // フォームの自動送信
    $("form input,select,textarea").change(function() {
      $("form").submit();
    })
  });
</script>
{% endblock %}
~~~
