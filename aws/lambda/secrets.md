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
