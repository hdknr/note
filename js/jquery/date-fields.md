日付フィールド

## HTML

- Bootstrap4 Dropdown で実装
- `hidden` フィールドに `yyyy-mm-dd` 形式でフォームデータを保持

~~~html
<div class="form-group row birthdate-fields">  // Container

    <input
      id="id-profile-birth_date"
      type="hidden"
      name="profile-birth_date"
      value="{{ profile.birth_date|default:'' }}"/>

    <label  class="col-sm-2 col-form-label">生年月日</label>

    <div class="d-flex">{# d-flex : 水平ならび #}

      <div>
       <button
        id="profile-birth_date_year"
        class="btn btn-outline-primary dropdown-toggle"
        type="button"
        data-toggle="dropdown">
        <span class="label">年</span>
        <span class="caret"></span></button>

        <ul
          class="dropdown-menu year-list scrollable-menu"  
          data-part="year"
          aria-labelledby="profile-birth_date_year">
        </ul>
      </div> {# 年 #}

      <div>
       <button
        id="profile-birth_date_month"
        class="btn btn-outline-primary dropdown-toggle"
        type="button"
        data-toggle="dropdown">
        <span class="label">月</span>
        <span class="caret"></span></button>

        <ul
          class="dropdown-menu month-list scrollable-menu"  
          data-part="month"
          aria-labelledby="profile-birth_date_month">
        </ul>
      </div> {# 月 #}

      <div>
       <button
        id="profile-birth_date_day"
        class="btn btn-outline-primary dropdown-toggle"
        type="button"
        data-toggle="dropdown">
        <span class="label">日</span>
        <span class="caret"></span></button>

        <ul
          class="dropdown-menu day-list scrollable-menu"  
          data-part="day"
          aria-labelledby="profile-birth_date_day">
        </ul>
      </div>{# 日 #}
    </div><!-- /.d-flex -->
  </div><!-- /.birthdate-fields-->
~~~

## CSS

~~~css
<style>

.scrollable-menu {     // ドロップダウンをスクロールさせる
  height: auto;
  max-height: 500px;
  overflow-x: hidden;
}

.birthdate-fields .d-flex div { // 横並びDropdownのマージン
  margin-left: 10px;
}
</style>
~~~


## Javascript


~~~javascript

function convert_wareki(year){      // 和暦ラベルに変換する
    const reki = [
        {prefix: '平成', year: 1988},
        {prefix: '昭和', year: 1925},
        {prefix: '大正', year: 1911},
        {prefix: '明治', year: 1857},
        {prefix: '', year:0},
    ].filter(function(i){ return year > i.year})[0];
    return reki.prefix + (year - reki.year).toString();
}

function on_select(e){
  /* <li>が選択されたのでボタンのラベルを変更 */
  const li = $(e.target)
  const dropmenu = li.closest(".dropdown-menu");
  dropmenu.data('value', li.data('value'));
  li.siblings().removeClass('active');
  li.addClass('active');
  dropmenu.siblings('button').find('.label').text(li.text());
}

function init_dropdown(dropmenu, items, formatter){
  /* ドロップダウンの<li>を初期化する */
  dropmenu.empty();

  items.map(function(i){
    let text = formatter(i);
    let li = $('<li>').addClass('dropdown-item').text(text).data('value', i);

    if(parseInt(dropmenu.data('value')) == i){
      li.addClass('active');
      $(dropmenu).siblings('button').find('.label').text(text);
    }
    dropmenu.append(li);
  })
}


function change_days(container){
  /* 年月が変更されたら日の選択リストを設定し直す */
  const dls = container.find('ul.dropdown-menu').get();

  const year = $(dls[0]).data('value');
  const month = $(dls[1]).data('value');
  const day = $(dls[2]).data('value');

  let days = _.range(1, 32);
  if(month != null && year != null){
    days = _.range(1, 1 + moment([year,month - 1]).daysInMonth());
  }

  if(day != null && days.indexOf(parseInt(day)) < 0 ){
    $(dls[2]).data('value', null);
    $(dls[2]).siblings('button').find('.label').text('日');
  }

  init_dropdown($(dls[2]), days, function(i){return i.toString() + "日";}
  );
}
function update_date(container){
  /* ドロップダウンの内容で、フォームデータを変更 */
  const vals = container.find('ul.dropdown-menu').map(function(i, elm){
    return $(elm).data('value');
  }).get();

  if( _.every(vals, function(i){ return i != null;})){
    container.find('input:hidden').val(vals.join('-'));
  }
}

function init_year(dropdown){
  /* 年リストの初期化 */
  init_dropdown(
    $(dropdown), _.range(1940, 2000),
    function(i){return i.toString() + "年" + "(" + convert_wareki(i)  +  ")";}
  );
  // 年の選択肢が多いので、値がなかったら1980近辺に移動させる
  $(dropdown).closest('div').on('shown.bs.dropdown', function () {
    let e = $(this).find('li.active');
    e = (e.length) ? e : $(this).find('li:contains("1980")');
    const e0 = $(this).find('li:first');

    if(e){
      const posi = e.offset().top - e0.offset().top;
      $(dropdown).animate({scrollTop: posi}, 500);
    }
  });
}

function init_month(dropdown){
  /* 月リストの初期化 */
  init_dropdown(
    $(dropdown), _.range(1, 13),
    function(i){return i.toString() + "月";}
  );
}

function init_day(dropdown){
  /* 日リストの初期化 */
  change_days($(dropdown).closest('.birthdate-fields'));
}


$(function(){
  /* メイン */

  $(".birthdate-fields").map(function(i, container){
    /* YMD 選択は複数ありえる */

    // 初期値
    const date = $(container).find("input:hidden").val().split('-');

    // Y, M, D のドロップダウンの設定
    $(container).find("ul.dropdown-menu").map(function(i, dl){
        const part = ['year', 'month', 'day'].indexOf($(dl).data('part'));
        const inits = [init_year, init_month, init_day];

        if(date.length == 3){
          $(this).data('value', date[part]);    // 初期値
        }

        inits[part](dl);                        // リストの初期化

        $(dl).on('click','li', function(e){
          on_select(e);
          if(part < 2){
            // 年月の変更で日リストを変更
            change_days($(e.target).closest('.birthdate-fields'));
          }
          // フォームの送信データを変更
          update_date($(e.target).closest('.birthdate-fields'));
        });
    });
  });

});

~~~
