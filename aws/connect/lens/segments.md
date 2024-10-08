# ListRealtimeContactAnalysisSegments

`ListRealtimeContactAnalysisSegments` APIを呼び出し、トランスクリプトを取得します。

```python
import boto3

# Amazon Connectのクライアントを作成
client = boto3.client('connect')

# 必要なパラメータを設定
instance_id = 'your_instance_id'
contact_id = 'your_contact_id'

# ListRealtimeContactAnalysisSegments APIを呼び出し
response = client.list_realtime_contact_analysis_segments(
    InstanceId=instance_id,
    ContactId=contact_id
)

# トランスクリプトのセグメントを取得
transcript_segments = response.get('Segments', [])

# トランスクリプトのテキストを表示
for segment in transcript_segments:
    if 'Transcript' in segment:
        print(segment['Transcript']['Content'])
```

このコードでは、`instance_id`と`contact_id`を適切な値に置き換えてください。`list_realtime_contact_analysis_segments`メソッドを呼び出し、返されたレスポンスからトランスクリプトのセグメントを取得し、それぞれのセグメントのテキストを表示します。

## 定期的に実行

- 5秒ごとにセグメントを取得するなど

## outputtype

The `OutputType` parameter in the `list_realtime_contact_analysis_segments_v2` function specifies the format of the data returned. Here are the meanings of the two options:

- **`Raw`**: This option returns the data in its original, unaltered form. It includes all the details captured during the analysis without any modifications or redactions.
- **`Redacted`**: This option returns the data with sensitive information removed or masked. This is useful for maintaining privacy and compliance with data protection regulations.

Choosing between `Raw` and `Redacted` depends on your specific needs for data handling and privacy considerations.

If you have any more questions or need further clarification, feel free to ask!

ソース: Copilot との会話、 2024/9/30
(1) connect_list_realtime_contact_analysis_segments_v2 - R .... <https://rdrr.io/cran/paws.customer.engagement/man/connect_list_realtime_contact_analysis_segments_v2.html>.
(2) aws_sdk_connect::operation::list_realtime_contact_analysis .... <https://docs.rs/aws-sdk-connect/latest/aws_sdk_connect/operation/list_realtime_contact_analysis_segments_v2/index.html>.
(3) aws connect-contact-lens list-realtime-contact-analysis-segments. <https://fig.io/manual/aws/connect-contact-lens/list-realtime-contact-analysis-segments>.
(4) undefined. <https://www.paws-r-sdk.com/docs/connect_list_realtime_contact_analysis_segments_v2/>.
