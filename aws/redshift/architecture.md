# アーキテクチャ

- 列指向ストレージ
- 超並列処理（MPP）
- Redshift Spectrum
- コールドクエリ
- Data Sharing
- クロスデータベースクエリ
- [データレイククエリ](https://qiita.com/zumax/items/84534883f8ba8ffd0a41)
- [クラスタ間データ共有](https://qiita.com/zumax/items/555efda12bd1c3a65343)
- [AQUA((アドバンストクエリアクセラレータ)](https://docs.aws.amazon.com/ja_jp/redshift/latest/mgmt/managing-cluster-aqua.html)
- [マテリアライズドビュー](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/materialized-view-overview.html)	
- [Spectrum](https://docs.aws.amazon.com/ja_jp/redshift/latest/dg/c-using-spectrum.html)

## psql

~~~
psql -h {エンドポイント名} -p {ポート番号} -U {ユーザ名} -d {データベース名}
~~~

## varchar

- MySQL : 文字数
- PostgreSQL : 文字数
- Redshift : バイト数