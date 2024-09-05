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

## コード

- <https://github.com/Amatobahn/FigmaPy>
- <https://github.com/the-dataface/figma2html?tab=readme-ov-file#how-it-works> (OpneAI使ってる) (<https://www.builder.io/>)
- <https://github.com/px2code/Figma-to-HTML?tab=readme-ov-file>
- <https://github.com/ayush013/fig-gen>

## JSON to HTML

- <https://github.com/abhaykatheria/json2tree>

## データ

### ノード

- [Plugin API:Node Types](https://www.figma.com/plugin-docs/api/nodes/)
- [REST API: Node types](https://www.figma.com/developers/api#node-types)
