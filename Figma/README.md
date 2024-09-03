# Figma

## REST API

ファイル:

~~~py
import requests

api_token = 'YOUR_API_TOKEN'
file_key = 'YOUR_FILE_KEY'

headers = {
    'X-Figma-Token': api_token
}

url = f'https://api.figma.com/v1/files/{file_key}'

response = requests.get(url, headers=headers)

print(response.json())
~~~

イメージ
