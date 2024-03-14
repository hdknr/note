# OLAP(Online Analytical Processing)


## 記事

- [OLAP分析とは？DWHやOLTPとの違いを理解し、BIツールの活用を！](https://yellowfin.co.jp/blog/17-jpblog1-what-is-olap)
- [WHAT IS OLAP?](https://www.snowflake.com/data-cloud-glossary/olap/?lang=ja)
- [What is a Snowflake Schema?](https://olap.com/learn-bi-olap/olap-bi-definitions/snowflake-schema/)
- [Oracle: 2 データ・ウェアハウスの論理設計](https://docs.oracle.com/cd/E16338_01/server.112/b56309/logical.htm)
- [データモデリングにおける非正規化とスタースキーマ](https://blog.flinters-base.co.jp/entry/2022/09/28/000000)

- [データベースの正規化(第1〜第3正規形) ](https://tech.012grp.co.jp/entry/db_normalization)   

## スノーフレークスキーマ

- スタースキーマのディメンションが正規化されたスキーマ
- 正規化することでストレージは節約できるが、クエリは複雑になる
- [スノーフレークとスタースキーマの違いと比較](https://www.integrate.io/jp/blog/snowflake-schemas-vs-star-schemas-what-are-they-and-how-are-they-different-ja/)
- [スノーフレークスキーマ](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%8E%E3%83%BC%E3%83%95%E3%83%AC%E3%83%BC%E3%82%AF%E3%82%B9%E3%82%AD%E3%83%BC%E3%83%9E)




## 関数従属性

[「関数従属性」を理解する](https://atmarkit.itmedia.co.jp/ait/articles/1703/01/news181.html):

- ある属性Xを決めると、他の属性Yの値が一意に決まる場合、「YはXに関数従属している」といいX→Yと表現します。
- このときXを **決定項**、Yを **被決定項** と呼びます。
- 関数従属の方向: ER図のリレーションシップ( X <- Y) の逆

- [推移的関数従属](http://database090212.com/dword/dbword1_71.html)

推論則:

| ルール | 内容                                                   |
| ------ | ------------------------------------------------------ |
| 反射律 | Y がX の部分集合ならば、X→Y が成立する                 |
| 増加律 | X → Y が成立するならば、｛X、Z｝→｛Y、Z｝が成立する    |
| 推移律 | X → Y かつY → Zが成立するならば、X →Zが成立する        |
| 合併律 | X → Y かつX → Zが成立するならば、X →｛Y、Z｝が成立する |
