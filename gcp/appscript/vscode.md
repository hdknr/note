# AppScript VSCode


~~~zsh
% npm install @google/clasp -g
~~~

~~~zsh
% clasp --version
2.4.1
~~~

~~~zsh
% clasp login
Logging in globally…
🔑 Authorize clasp by visiting this url:
https://accounts.google.com/o/oauth2/v2/auth?access_type=..........

Authorization successful.
~~~ 

既存のスクリプトの`プロジェクトの設定`より`スクリプトID` を指定する
~~~zsh
% clasp clone 1Xx9ZysZYL2aPIzK2xm6qPR9ErwzQFLXFgLisTjkZf-BGYiFnGiW_IV0Y

Warning: files in subfolder are not accounted for unless you set a '/Users/hdknr/Projects/shaper/yourproj/.claspignore' file.
Cloned 6 files.
└─ /Users/hdknr/Projects/shaper/yourproj/appsscript.json
└─ /Users/hdknr/Projects/shaper/yourproj/code.js
└─ /Users/hdknr/Projects/shaper/yourproj/main.js
└─ /Users/hdknr/Projects/shaper/yourproj/trigger.js
└─ /Users/hdknr/Projects/shaper/yourproj/index.html
└─ /Users/hdknr/Projects/shaper/yourproj/rss.js
Not ignored files:
└─ /Users/hdknr/Projects/shaper/yourproj/appsscript.json
└─ /Users/hdknr/Projects/shaper/yourproj/code.js
└─ /Users/hdknr/Projects/shaper/yourproj/index.html
└─ /Users/hdknr/Projects/shaper/yourproj/main.js
└─ /Users/hdknr/Projects/shaper/yourproj/rss.js
└─ /Users/hdknr/Projects/shaper/yourproj/trigger.js

Ignored files:
└─ /Users/hdknr/Projects/shaper/yourproj/.clasp.json
~~~

## 記事

- [Visual Studio Code + clasp で Google Apps Script 開発（Windows編)](https://qiita.com/draqoon/items/1bd74785f362bd138f65)
- [GAS用のCLIツール clasp を使ってGASをローカルで開発して実行するの巻。](https://qiita.com/jiroshin/items/dcc398285c652554e66a)
- [【GAS】clasp pushコマンド実行時に出たエラーの対処](https://qiita.com/shin_moto/items/debfaa61e431542a12a0)
