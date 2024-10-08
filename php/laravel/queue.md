# ジョブとキュー

- [Queues](https://laravel.com/docs/11.x/queues)

## `database`

Laravelで`queue connections`に`database`を指定した場合、キューの受け渡しは以下のような仕組みで行われます
[¹](https://qiita.com/KyuKyu/items/1316ab89703519427c56)²(<https://qiita.com/yagiryu/items/ba10dca6750735a356f9)：>

1. **ジョブのキューイング**:
   - ジョブがキューに追加されると、Laravelはそのジョブをデータベースの`jobs`テーブルにレコードとして保存します。
   - このテーブルには、ジョブの名前、データ、キュー名、ステータスなどが含まれます。

2. **ワーカーの実行**:
   - `php artisan queue:work`コマンドを実行すると、キューワーカーが起動します。
   - ワーカーは`jobs`テーブルを監視し、新しいジョブが追加されるとそれを取得して処理します。

3. **ジョブの処理**:
   - ワーカーがジョブを取得すると、そのジョブを実行します。
   - ジョブが成功すると、そのレコードは`jobs`テーブルから削除されます。
   - ジョブが失敗した場合、`failed_jobs`テーブルに記録され、再試行が設定されている場合は再度キューに追加されます。

4. **再試行と失敗**:
   - ジョブが失敗した場合、Laravelは設定に基づいて再試行を行います。
   - 再試行がすべて失敗すると、ジョブは`failed_jobs`テーブルに移動され、管理者が確認できるようになります。

この仕組みにより、データベースドライバを使用することで、ジョブのキューイングと処理が効率的に行われます。
データベースドライバは、特に小規模なアプリケーションやデータベースを中心としたインフラストラクチャに適しています。

[¹](https://qiita.com/KyuKyu/items/1316ab89703519427c56): [Laravelでジョブとキューを理解する - Qiita](https://qiita.com/KyuKyu/items/1316ab89703519427c56)
[²](https://qiita.com/yagiryu/items/ba10dca6750735a356f9): [Queues - Laravel 11.x - The PHP Framework For Web Artisans](https://laravel.com/docs/11.x/queues)

(1) Laravelでジョブとキューを理解する - Qiita. <https://qiita.com/KyuKyu/items/1316ab89703519427c56>.
(2) 【勉強メモ】Laravelのqueueとjobについて - Qiita. <https://qiita.com/yagiryu/items/ba10dca6750735a356f9>.
