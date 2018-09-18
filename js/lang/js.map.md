# Map

- [Map - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Map)

|              | Map             | Object                 |
| ------------ | --------------- | ---------------------- |
| キー          | 任意の値         | String, Symbols        |
| 大きさ        | size            | プログラマが管理          |
| 反復          | iterable        | キーを取得して反復処理     |
| 規定のキー     | なし             | あり(`map = Object.create(null)` で回避可能) |

- Map は、頻繁に要素を追加したり削除したりするシナリオでは、パフォーマンスがObject に比べて良い場合があります。
