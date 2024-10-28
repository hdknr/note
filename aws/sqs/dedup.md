# 重複排除(Deduplication)

## The queue should either have ContentBasedDeduplication enabled or MessageDeduplicationId provided explicitly

このエラーは、Amazon SQSのFIFO（First-In-First-Out）キューに関連しています。
FIFOキューでは、メッセージの重複排除を行うために、以下のいずれかの方法を使用する必要があります：

1. **ContentBasedDeduplication**を有効にする：このオプションを有効にすると、メッセージの内容に基づいて重複排除IDが自動的に生成されます。
2. **MessageDeduplicationId**を明示的に指定する：メッセージを送信する際に、重複排除IDを手動で指定します。

このエラーが発生するのは、これらの設定が正しく行われていない場合です。
具体的には、FIFOキューでメッセージを送信する際に、どちらの方法も使用していないときにこのエラーが表示されます
[¹](https://pod.hatenablog.com/entry/2020/01/18/144551)[²](https://qiita.com/matsumura-yzrh/items/e614e55c0a7f1383aa0b)³(<https://qiita.com/YusukeSuzuki1213/items/68305bb03996bd4b0f24)。>

解決方法としては、キューの設定を確認し、ContentBasedDeduplicationを有効にするか、メッセージ送信時にMessageDeduplicationIdを指定するようにしてください。

[¹](https://pod.hatenablog.com/entry/2020/01/18/144551): <https://pod.hatenablog.com/entry/2020/01/18/144551>
[²](https://qiita.com/matsumura-yzrh/items/e614e55c0a7f1383aa0b): <https://qiita.com/matsumura-yzrh/items/e614e55c0a7f1383aa0b>
[³](https://qiita.com/YusukeSuzuki1213/items/68305bb03996bd4b0f24): <https://qiita.com/YusukeSuzuki1213/items/68305bb03996bd4b0f24>

- (1) SQSのdeduplication Idについてよくわかっていなかったのでメモ .... <https://pod.hatenablog.com/entry/2020/01/18/144551>.
- (2) motoによるSQSキュー(FIFO)のモック作成 - Qiita. <https://qiita.com/matsumura-yzrh/items/e614e55c0a7f1383aa0b>.
- (3) AWSのSQS(FIFO)でContentBasedDeduplicationで怒られた .... <https://qiita.com/YusukeSuzuki1213/items/68305bb03996bd4b0f24>.
- (4) Troubleshoot AccessDenied errors on Amazon SQS API calls. <https://repost.aws/knowledge-center/sqs-accessdenied-errors>.
- (5) AWS队列:队列应该启用ContentBasedDeduplication或显式提供 .... <https://cloud.tencent.com/developer/ask/sof/108096709>.
- (6) undefined. <https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html>.
- (7) undefined. <https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html>.
- (8) undefined. <https://gist.github.com/podhmo/135cd16142243c6cd46479251de47c0e>.
- (9) undefined. <https://hogefuga.com>.
- (10) undefined. <https://docs.getmoto.org/en/latest/docs/services/sqs.html>.
- (11) undefined. <https://github.com/spulec/moto/blob/3.1.12/tests/test_sqs/test_sqs.py>.
