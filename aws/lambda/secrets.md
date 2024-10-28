# AWS Secrete Manager

```py
import ast
import boto3
import base64
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    secret_name = "YourSecretName"
    region_name = "YourSecretManagerRegion"

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret_data = get_secret_value_response['SecretString']
            secret = ast.literal_eval(secret_data)
            name = secret['name']
            pw = secret['pw']
            print(f'name: {name}, pw: {pw}')
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            # Use the binary secret as needed

# Deploy your Lambda function and test it.

```

## VPCエンドポイント

VPC内で動作するLambda関数がAWS Secrets Managerにアクセスする際にタイムアウトする場合、VPCエンドポイントの設定が必要です。
VPCエンドポイントを設定することで、Lambda関数がインターネットを経由せずにSecrets Managerにアクセスできるようになります。

以下の手順で設定を行うことをお勧めします[¹](https://docs.aws.amazon.com/ja_jp/secretsmanager/latest/userguide/vpc-endpoint-overview.html)²(<https://qiita.com/gossan/items/b1b37c61bc3ffa3d5486>):

1. **VPCエンドポイントの作成**:
   - AWS Management Consoleにログインし、VPCサービスに移動します。
   - 「エンドポイント」を選択し、「エンドポイントを作成」をクリックします。
   - サービス名に `com.amazonaws.<region>.secretsmanager` を選択します（例: `com.amazonaws.ap-northeast-1.secretsmanager`）。
   - VPC、サブネット、およびセキュリティグループを選択します。

2. **Lambda関数の設定**:
   - Lambda関数の設定画面に移動し、「設定」タブを開きます。
   - 「VPC」を選択し、適切なVPC、サブネット、およびセキュリティグループを選択します。
   - Lambda関数に必要なIAMロールに `AWSLambdaVPCAccessExecutionRole` と `SecretsManagerReadWrite` ポリシーをアタッチします。

3. **プライベートDNSの有効化**:
   - VPCエンドポイントの設定でプライベートDNSを有効にします。これにより、Secrets ManagerへのAPIリクエストがリージョンのデフォルトDNS名（例: `secretsmanager.ap-northeast-1.amazonaws.com`）を使用して行われます。

これらの設定を行うことで、Lambda関数がSecrets Managerにタイムアウトせずにアクセスできるようになるはずです。

- (1) AWS Secrets Manager VPC エンドポイントの使用. <https://docs.aws.amazon.com/ja_jp/secretsmanager/latest/userguide/vpc-endpoint-overview.html>.
- (2) VPC Lambda（Node.js）からSecretsManagerのシークレットを .... <https://qiita.com/gossan/items/b1b37c61bc3ffa3d5486>.
- (3) Getting secret from Lambda times out when attached to VPC .... <https://repost.aws/questions/QU1WLg4Q2-TCqznkgmpPnW0g/getting-secret-from-lambda-times-out-when-attached-to-vpc-subnet>.
- (4) Lambda 関数の Amazon VPC 接続タイムアウトを防ぐ | AWS .... <https://repost.aws/ja/knowledge-center/lambda-vpc-timeout>.
- (5) VPC での Lambda 関数によるタイムアウトエラーのトラブル .... <https://repost.aws/ja/knowledge-center/lambda-vpc-troubleshoot-timeout>.
