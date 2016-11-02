AngularJS: イベントテーブルの年、月をrowspanでブレークさせる

- 今日からAngularJS始めたのですがむずかしい。こんなんでいいのだろうか。
- 年度件数、年度+月件数をカウントしてレンダリングの時の`rowspan`にする
- Django のテンプレート

~~~html

<!doctype html>
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.0/angular.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/angular-i18n/1.2.15/angular-locale_ja-jp.js"></script> {# 日本語曜日 #}
    <script>

    var myApp = angular.module('myApp', []);

    myApp.controller('EventListController', function($scope, $http) {
      $http.get('{{ data }}')       //  {# JSONのURL #}
      .success(function(data, status, headers, config) {
        month_count = [];
        year_count = [];
        for(var i in data){
          var d = new Date(data[i].opening_on)              // {# 日付 #}
            var y = d.getFullYear().toString() + '年' ;
            var m = (1 + d.getMonth()).toString() + '月' ;

			data[i].year = y;
            data[i].month = m;

            if( y in month_count == false ){
                month_count[y] = []; 
            }   

            if( y in year_count == false ){
                year_count[y] = 0;
            }   

            if( m in month_count[y] == false ){
                month_count[y][m] = 0;
            }   
            month_count[y][m] = month_count[y][m] + 1;
            year_count[y] =  year_count[y] + 1;
        }   


        $scope.events = data;
        $scope.month_count = month_count;
        $scope.year_count = year_count;
        
      })
      .error(function(data, status, headers, config) {
        // log error
      });
    });

    </script>
  </head>
  <body>

  {# Django テンプレート展開させない #}
  {% verbatim %}
  <div ng-app="myApp" ng-controller="EventListController">
    <table  border="1">
      <tr ng-repeat="ev in events"> 
        <th ng-show="events[$index-1].year != events[$index].year" rowspan="{{ year_count[ev.year] }}"> {{ ev.year }}</th>
        <th ng-show="events[$index-1].month != events[$index].month" rowspan="{{ month_count[ev.year][ev.month]}}"> {{ ev.month}}</th>
      <td>({{ ev.opening_on|date:'EEE'}})</td>
      <td>{{ ev.title }} {{ ev.presenter }}</td>
    </tr>
    </table>
  </div>
  {% endverbatim %}
  
  </body>
</html>
~~~
