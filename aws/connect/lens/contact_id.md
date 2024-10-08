# contact_id の取得

現在通話中の `contact_id` を取得するには、Amazon Connectの`list_contacts` APIを使用します。以下にboto3を使ったサンプルコードを示します。

```python
import boto3

# Connectクライアントの作成
client = boto3.client('connect')

# 現在通話中のコンタクトIDを取得する関数
def get_current_contact_id(instance_id):
    response = client.list_contacts(
        InstanceId=instance_id,
        MaxResults=10  # 必要に応じて変更
    )
    # 通話中のコンタクトをフィルタリング
    active_contacts = [contact for contact in response['ContactSummaryList'] if contact['State'] == 'CONNECTED']
    return [contact['ContactId'] for contact in active_contacts]

# 使用例
instance_id = 'your_instance_id'

contact_ids = get_current_contact_id(instance_id)
for contact_id in contact_ids:
    print(contact_id)
```

このコードでは、`list_contacts` APIを使用して現在のコンタクトリストを取得し、その中から状態が`CONNECTED`のコンタクトをフィルタリングして`contact_id`を取得します。

ソース: Copilot との会話、 2024/9/30
(1) Python boto3 でAWSを自在に操ろう ~入門編~ - Qiita. <https://qiita.com/kimihiro_n/items/f3ce86472152b2676004>.
(2) Boto3（AWS SDK for Python）の利用する認証情報 - Qiita. <https://qiita.com/tsukamoto/items/00ec8ef7e9a4ce4fb0e9>.
(3) 【小ネタ】AWS Python SDK (boto3)からアカウントID .... <https://dev.classmethod.jp/articles/get-aws-account-id-and-region-name-from-boto3/>.
(4) Boto3で利用中のAWSアカウントIDを取得する #Python3 - Qiita. <https://qiita.com/shinsaka/items/b8304f35866367ebf45d>.
(5) undefined. <https://reboooot.net/post/why-boto/>.
(6) undefined. <https://aws.amazon.com/jp/developers/access-keys/>.
