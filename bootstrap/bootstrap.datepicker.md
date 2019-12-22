# bootstrap-datepicker

- https://github.com/uxsolutions/bootstrap-datepicker

CSS:

~~~html
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker3.min.css" />
~~~

Dependencies(JQuery, Bootstrap)

~~~html
<script src="//code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
~~~

bootstrap-datepicker:

~~~html
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/js/bootstrap-datepicker.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/locales/bootstrap-datepicker.ja.min.js"></script>
~~~


Application:

~~~javascript
$(".birthdate, .graduate").datepicker({
      startDate: moment().toDate(),
      format: 'yyyy-mm-dd',
      autoclose: true,
      language: "ja"
});
~~~

## [最小表示(minViewMode)](https://bootstrap-datepicker.readthedocs.io/en/stable/options.html#minviewmode)

- `0` (`days`,`month`)  : 日にちまで(デフォルト)選択
- `1` (`months`,`year`) : 月まで選択可能 (日にちは 1日)
- `2` (`years` ,`decade`) : 年まで選択可能(月は1月)
- `3` (`decades`, `centurry`) : 10年単位の年まで(最後が1年)
- `4` (`centuries`, `millenium`) : 世紀まで選択可能(最後が１年)


## 開始、終了

- [startDate](https://bootstrap-datepicker.readthedocs.io/en/latest/options.html#startdate)
- [endDate](https://bootstrap-datepicker.readthedocs.io/en/latest/options.html#enddate)

~~~html
<input type="text" class="form-control datepicker"
    data-date-start-date="1900-01-01"
    data-date-end-date="2000-12-31">
~~~