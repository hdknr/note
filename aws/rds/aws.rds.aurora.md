- [Aurora](http://dev.classmethod.jp/cloud/aws/cm-advent-calendar-2015-aws-re-entering-rds/#aurora)
- [Amazon RDS での Aurora](https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/CHAP_Aurora.html)


## Amazon Aurora のストレージ

- SSD（Solid State Disk）ドライブを利用する単一の仮想ボリュームであるクラスターボリュームに保存されます。
- クラスターボリュームは、単一リージョンの複数のアベイラビリティーゾーン間のデータのコピーで構成されます。
- データはアベイラビリティーゾーン間で自動的にレプリケートされるため、データ損失の可能性は低く、耐久性は非常に高くなります。
- このレプリケーションは、フェイルオーバー中のデータベースの可用性をさらに高めることも保証します。
- その理由は、データのコピーは既に他のアベイラビリティーゾーンに存在し、DB クラスター内のインスタンスに対するデータ要求を処理し続けるためです。
- クラスターボリュームは、データベースのデータ量が増えるにつれて自動的に増加します。
- 最大 64 テラバイト (TB) のサイズまで増やすことができます。
- テーブルサイズの上限はクラスターボリュームのサイズです。つまり、最大テーブルサイズは 64 TB です。
- 使用する領域に対してのみ料金が請求されます。[料金表](https://aws.amazon.com/jp/rds/aurora/pricing/)
