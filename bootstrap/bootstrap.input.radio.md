# ラジオボタン


## インラインで横に並べる

部門選択(Djangoの ChoiceField):

~~~css

/* ラジオボタン本体を消す */
.dept-choice input[type=radio]{
  display:none;
}

/* チェックされたラジオボタンの次のラベルの色を変更する */
.dept-choice input[type=radio]:checked + label{
  color:white;
  background-color: blue;
}

/* ラジオボタンのラベルのデフォルトの状態 */
.dept-choice input[type=radio]+ label{
  width: 70px;                      /* 均等幅 */
  background-color: #e6e6e6;        /* 背景(iOSで見えなくなるので) */
  margin-bottom: 0.5rem;            /* ２段に跨った場合のマージン設定 */
}
~~~

~~~html
<div class="radio dept-choice">
{% for choice in form.dept1_name.field.choices %}
    <span class="radio-inline">
        <input
            name="{{ form.dept1_name.name }}"
            type="radio" id="{{ form.dept1_name.auto_id }}_{{forloop.counter}}"
            value="{{ choice.0 }}">
        <label
            for="{{ form.dept1_name.auto_id }}_{{forloop.counter}}"
            class="btn btn-outline-secondary">{{ choice.0 }}</label>
    </span>
{% endfor %}
</div>
~~~

## 記事

- [【Rails】Bootstrap 4 でラジオボタンの見た目をトグルボタンにする - Qiita](https://qiita.com/NaokiIshimura/items/faac08d8380b79ea108e)