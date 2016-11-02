- [条件式の真偽に応じて表示を切り替えるには？（ng-if） ](http://www.buildinsider.net/web/angularjstips/0010)


~~~html

<label ng-if="activities['美術部'].length > 0">活動報告:</label>           <!-- 武術部のactivitiesがあるときだけラベル表示 -->

<ul ng-repeat="entry in activities[美術部]" ng-show="$index < 3" > <!-- activitiesの最初の３件飲み -->
    <li>{{ entry.last_activity.updated_at | date: 'yyyy年M月d日（EEE）' }}:
        <a href="{{ entry.last_activity.link }}">
            {{ entry.name }}:{{ entry.last_activity.title}}
        </a>
    </li>
</ul>

~~~
