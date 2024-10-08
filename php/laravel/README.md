# Laravel

## artisan

- `php artisan migrate` : マイグレーション
- `php artisan db` : データベースコンソール
- `php artisan key:generate`: APP_KEY の生成と設定(`.env`)
- `php artisan tinker`: REPL コンソール

## `.env`

- デフォルト値
- OSから引き継がれる 値が優先されます

## キャッシュ

クリア:

~~~zsh
php artisan cache:clear
php artisan config:clear
php artisan route:clear
php artisan view:clear
~~~

## トピック

- [ジョブとキュー](queue.md)
