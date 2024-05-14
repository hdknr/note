# Bedlock Knowlege Base

![](aws_bedrock_kb.jpg)

## トークン見積もり

- 100K トークン == 約 10 万文字分
- 1000 文字/doc とすると 100 ファイル

## リージョンとモデル

リージョン:

- 米国東部 (バージニア北部)
- 米国西部 (オレゴン)

埋め込み:

- Titan G1 埋め込み - テキスト
- Cohere Embed 英語
- Cohere Embed 多言語

生成:

- Anthropic Claude Instant v1
- Anthropic Claude v2.0
- Anthropic Claude v2.1

## Vector Store

４種:

- Amazon OpenSearch Serverless
- Amazon Aurora
- Pinecone
- Redis Enterprise Cloud

### Aurora:Aurora Serverless v2

- 0.5[ACU](https://zenn.dev/yama_1998/articles/515cfe30b712e4) で作成することができる
- 月額$43.2(0.12USD(/h) x 0.5(ACU) x 24(時間) x 30(日))
- 1 ドル 150 円換算で月額 6480 円

## S3 -> Vector Store

埋め込みモデル:

- Amazon Titan Embeddings G1 - Text v1.2
- Corhere Embed English v3
- Corhere Embed Multilingual v3

Cohere 料金:

| Cohere モデル     | 入力トークン 1,000 個あたりの価格 | 出力トークン 1,000 個あたりの価格 |
| ----------------- | --------------------------------- | --------------------------------- |
| Command           | 0.0015 USD                        | 0.0020 USD                        |
| コマンドライト    | 0.0003 USD                        | 0.0006 USD                        |
| 埋め込み — 英語   | 0.0001 USD                        | 該当なし                          |
| 埋め込み — 多言語 | 0.0001 USD                        | 該当なし                          |

Tital 料金(テキストモデルのオンデマンドおよびバッチ価格):

| Amazon Titan モデル  | 入力トークン 1,000 個あたりの価格 | 出力トークン 1,000 個あたりの価格 |
| -------------------- | --------------------------------- | --------------------------------- |
| Titan Text – Lite    | USD 0.0003                        | USD 0.0004                        |
| Titan Text – Express | USD 0.0008                        | USD 0.0016                        |
| Titan Text 埋め込み  | USD 0.0001                        | N/A                               |

1000 ファイル -> 1M トークン -> 0.0001 x 1000 = 1 ドル

## 生成(Claude3 (Oregon, virginia))

note:

- Tokyo だと (Claude2.1, Tital)

| Anthropic モデル | 入力トークン 1,000 個あたりの価格 | 出力トークン 1,000 個あたりの価格 |
| ---------------- | --------------------------------- | --------------------------------- |
| Claude Instant   | 0.00080 USD                       | 0.00240 USD                       |
| Claude           | 0.00800 USD                       | 0.02400 USD                       |

1000 ファイル -> 1M トークン -> 0.008 x 1000 = 80 ドル

## サンプル

- [langchain で RAG](kb_lc.py)
