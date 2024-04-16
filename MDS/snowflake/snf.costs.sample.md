# 評価基盤費用概算

- https://www.snowflake.com/pricing/pricing-guide/
- [Guides > Cost & Billing > Cost & billing](https://docs.snowflake.com/en/guides-overview-cost)

## Snowflake コスト要因

| コスト項目         | 内容                                                   | コスト内訳                                       |
| ------------------ | ------------------------------------------------------ | ------------------------------------------------ |
| 契約               | Starndad ,Enterprise, Business Critical, VPS           | それぞれクレジット単価が異なる                   |
| 仮想ウェアハウス   | クラウドで起動するサーバー料金                         | サーバーサイズごとにクレジットが決まっている     |
| サーバーレス費用   | Snowflake が提供する便利機能を使う場合に発生する料金　 | 機能ごとに時間当たりのクレジット数が決まっている |
| ストレージ　　　　 | ストレージ維持費                                       | サーバーが起動していない場合も必要               |
| データ転送         | 問い合わせの転送料金(ロードは無料 )                    | クラウド内部とクラウド間で異なる                 |
| LLM                | 大規模言語モデル利用料金                               | 利用機能のクレジット単価で異なる                 |

## サーバーレス費用を除く金額シュミレーション

契約:

| 利用　     | 単価　  |
| ---------- | ------- |
| Enterprise | 4.3 USD |

仮想ウェアハウス:

| 項目　　　　   | データロード         | 問い合わせ           |
| -------------- | -------------------- | -------------------- |
| 頻度           | 20 日/月             | 20 日/月             |
| 利用時間       | 1 時間/日            | 1 時間/日            |
| サイズ         | Mediam(4 クレジット) | Mediam(4 クレジット) |
| 月次クレジット | 80 クレジット        | 80 クレジット        |
| 月次利用金額　 | 344 USD              | 344 USD              |

ストレージ

| 項目             | 内容      |
| ---------------- | --------- |
| ストレージ単価   | 23 USD/TB |
| 使用ストレージ　 | 2TB       |
| 月次利用料       | 46 USD    |

データ転送

| 項目                           | 内容        |
| ------------------------------ | ----------- |
| AWS 同一リージョン内転送単価　 | 90 USD / TB |
| データ転送月次想定　           | 200 GB      |
| 月次データ転送量               | 18 USD      |

LLM 利用料金:

- https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#usage-quotas

| LLM 機能        | クレジット単価/1M トークン | トークン/リクエスト | リクエスト数/日付 | 日数 | クレジット単価 | USD   |
| --------------- | -------------------------- | ------------------- | ----------------- | ---- | -------------- | ----- |
| Complete(llama) | 0.45                       | 50000               | 100               | 20   | 4.3            | 193.5 |
| Translate       | 0.33                       | 50000               | 100               | 20   | 4.3            | 141.9 |
| Summarize       | 0.1                        | 50000               | 100               | 20   | 4.3            | 43    |
| Extract Answer  | 0.08                       | 50000               | 100               | 20   | 4.3            | 34.4  |
| Sentiment       | 0.08                       | 50000               | 100               | 20   | 4.3            | 34.4  |
| Embed Text      | 0.03                       | 50000               | 100               | 20   | 4.3            | 12.9  |
|                 |                            |                     |                   |      |                | 460.1 |

月次総額

    合計 = 344 + 344 + 46 + 18 + 460
        = 1204 USD
        = 1204 x 153.23 JPY
        = 184,489円

## サーバーレス費用

- [Serverless credit usage](https://docs.snowflake.com/en/user-guide/cost-understanding-compute#serverless-credit-usage)
- [Guides > Snowflake Cortex > Large Language Model Functions > Usage Quotas](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#usage-quotas)
