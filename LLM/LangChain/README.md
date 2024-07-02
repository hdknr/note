# LnagChain

- https://www.langchain.com/

## BaseModel

- [PyDantic BaseModel](https://docs.pydantic.dev/latest/api/base_model/) から継承されている

例: [ChatPromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) を JSON にシリアライズする。

```py
from langchain import hub

smith_name = "hdknr/helper"
prompt = hub.pull(smith_name, api_url="https://api.hub.langchain.com")
print(promt.json())
```
