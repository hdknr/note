# プラグイン開発

## 概要

### 作成

- 構造(名前、PHP ファイル, wp-content/plugins/ディレクトリ)
- ヘッダ(メタ情報, ライセンス)
- コード(....)
- 多言語化
- ルール([WordPress コーディング基準](http://wpdocs.osdn.jp/WordPress_%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E5%9F%BA%E6%BA%96)....)

#### コード

- テンプレートタグ
- データベース
- 設定(add_option, get_option, update_option)
- 管理パネル

## `add_action`

`save_post`:

- [How to run this plugin every time a post is saved?](https://wordpress.stackexchange.com/questions/422343/how-to-run-this-plugin-every-time-a-post-is-saved)

## Plugin API

- https://developer.wordpress.org/reference/
- [Plugin API の訳](https://wp.tekapo.com/2008/01/30/wordpress-plugin-api/)
- [プラガブル関数](https://codex.wordpress.org/Pluggable_Functions)
- [フィルターフック](https://developer.wordpress.org/apis/hooks/filter-reference/)
- [アクションフック](https://developer.wordpress.org/apis/hooks/action-reference/)

## 開発リソース

- [プラグイン・リソース](http://wpdocs.osdn.jp/Plugin_Resources)
- [Writing a Plugin](https://codex.wordpress.org/Writing_a_Plugin)

## テスト

- [PHPUnit](https://phpunit.de/)
- [The Beginner’s Guide to Unit Testing: Building a Testable Plugin](http://code.tutsplus.com/articles/the-beginners-guide-to-unit-testing-building-a-testable-plugin--wp-25741)
- [Wordpress trunk/test](https://develop.svn.wordpress.org/trunk/tests/phpunit/)

## その他

- [WordPress フィードで pre_get_posts の posts_per_page は使えない](http://dogmap.jp/2013/08/21/post-2984/)
