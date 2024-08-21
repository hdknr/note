# Markdown

## フォーマッターの変更

prettierからmarkdownlintに変更。 不必要にインデントを削除してしまうので。

~~~json
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
~~~

~~~json
  "[markdown]": {
    "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
  },
~~~
