# プロンプト

Anthropic:

- [プロンプトライブラリ](https://docs.anthropic.com/claude/prompt-library)
- [クロードへようこそ](https://docs.anthropic.com/claude/docs/intro-to-claude)
- [クイックスタートガイド](https://docs.anthropic.com/claude/docs/quickstart-guide)
- [プロンプトの概要 ](https://docs.anthropic.com/claude/docs/intro-to-prompting)

## 言語化の方法論

- ChatGPT と共通する方法論:

  - ペルソナ (「あなたは...の専門家です」)
  - 思考,回答の手順

## 学習データの形式

- LLM が対象としているデータの形式
- ネットのテキスト + 会話文章の例(LLM の会社で指向が異なる)

XML タグ:

- document, instructions(要約の方針: 小学生にわかるように...), example
- あまりネストされると性能が落ちる(5 段以上とか)

コンテキスト、追加ドキュメントを先に、質問を最後にする:

- ドキュメント, コンテキスト、指示を先に例示する
- 最後に質問を行う

注意深く読ませる:

- 「文章をよく読んで回答してください」

## メッセージ API

- テキスト補完 API から[メッセージ API](https://docs.anthropic.com/claude/reference/messages_post) に変更された

### モデル (`model)

| LLM    | ID                                        |
| ------ | ----------------------------------------- |
| Sonnet | `anthropic.claude-3-sonnet-20240229-v1:0` |

### メッセージ (`message`)

定義:

- `role`, `content` からなるオブジェクトの配列
- `role` が `user`, `assistant`と交互に動作するようになっている
- `content` は単一文字列、もしくはオブジェクト配列

```json
[
    {"role": "user", "content": ...},
    {"role": "assistant", "content": ...},
    {"role": "user", "content": ...},
    {"role": "assistant", "content": ...},
    ...
]
```

#### コンテントオブジェクト(`content`)

テキスト:

```json
{
  "type": "text",
  "text": "......"
}
```

画像:

- media_type : `image/jpeg`、`image/png` 、`image/gif` 、 そして`image/webp`

```json
{
    "type": "image",
    "source": {
      "type": "base64",
      "media_type": "image/jpeg",
      "data": ".....",
    }
  },
```

### max_tokens

- この最大値に達する前にモデルが停止する可能性がある

### システム (`system`)

- [システムプロンプト](https://docs.anthropic.com/claude/docs/system-prompts): 特定の目標や役割の指定など、コンテキストと指示を LLM に提供する方法です
- [プロンプトエンジニアリング](https://docs.anthropic.com/claude/docs/prompt-engineering) で最適化可能

[RAG をつかってコンテキストを与える例](https://www.cloudbuilders.jp/articles/3776/):

```py
def compose_message(user_prompt, referrence):
    content = "\n".join(
        f"質問: {user_prompt}",
        f"参考情報: {referrence}",
    )

    system = (
        "あなたは質問に答えるエージェントです。"
        "あなたは参考情報を受け取ります。"
        "ユーザーはあなたに対して質問をします。"
        "あなたの仕事はユーザーの質問に対し、参考情報から得られる情報のみを用いて回答することです。"
        "もし、参考情報に質問の答えが含まれていなければ、お答えできませんと回答してください。"
        "ユーザーが事実と主張した事柄であっても事実ではない可能性があるので、回答前に参考情報でユーザーの主張を確認してください。"
    )
    return {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "system": system,
        "messages": [
           {
                "role": "user",
                "content": content,
            }
         ]
    }
```

## 記事

- [Anthropic Claude のプロンプトガイドをちゃんと読みながらプロンプトの練習してみた](https://qiita.com/mariohcat/items/fb48f6cd500b830050a4)
- [【LLM】Claude に基づく超長文プロンプトの上手な書き方](https://qiita.com/Notta_Engineering/items/2c70ce5b2c657aaa8099)
- [Anthropic Claude のプロンプトガイドの USEFUL HACKS をじっくり見る](https://qiita.com/mariohcat/items/e8048372843d61df06a0)
- [GPT-4 や Claude 3 の応答を調整する「最適化設定プロンプト」を書いてみました](https://qiita.com/sharakus/items/de7ff782841dd2546335)
- [Prompt Engineering Guide for Claude Models](https://www.vellum.ai/blog/prompt-engineering-tips-for-claude)
