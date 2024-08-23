# Contentful

## 構造

- Organization
- Space
  - Users
  - Role & Permission
  - Environments
  - API Keys
  - CMA Tokens
  - Embargoed assets
  - Webhooks
- Environment
  - Locales
  - Tags

## Publish にする

Contentful の環境内のすべてのコンテンツを一括で公開するには、Content Management API を使用するスクリプトを作成するのが一般的です。以下はその一例です：

```javascript
const contentful = require("contentful-management");

const sleep = (msec) => new Promise((resolve) => setTimeout(resolve, msec));

(async () => {
  const client = contentful.createClient({
    accessToken: process.env.ACCESS_TOKEN,
  });

  const space = await client.getSpace(process.env.SPACE_ID);
  const environment = await space.getEnvironment("master"); // 環境名を指定
  const entries = await environment.getEntries({ limit: 1000 });

  for (const entry of entries.items) {
    if (!entry.isPublished()) {
      await entry.publish();
      console.log(`Published: ${entry.sys.id}`);
      await sleep(200); // API制限を避けるための待機時間
    } else {
      console.log(`Already published: ${entry.sys.id}`);
    }
  }
})();
```

このスクリプトは、指定された環境内のすべてのエントリーを取得し、未公開のものを公開します。API 制限を避けるために、各エントリーの公開後に少し待機時間を設けています ¹。

何か他にお手伝いできることがあれば教えてください！

ソース: Copilot との会話、 2024/8/20
(1) Contentful で管理しているブログ記事を一括公開する. https://sunday-morning.app/posts/2021-01-10-contentful-contents-multiple-publish.
(2) Largest contentful paint エラーの改善方法！パフォーマンスが .... https://40daimama.tokyo/net-sns/largest-contentful-paint-error/.
(3) Contentful で記事とコンテンツモデルのスナップショットを取得する. https://dev.classmethod.jp/articles/contentful-snapshot/.
