# `--mirror`

`wget` コマンドの `--mirror` オプションを使うと、ウェブサイト全体をローカルPCにコピーすることができます。以下のコマンドを実行してみてください：

```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com
```

このコマンドの各オプションの意味は次の通りです：

- `--mirror`: 再帰的にダウンロードし、タイムスタンプをチェックして新しいものだけをダウンロードします。
- `--convert-links`: ダウンロードしたHTMLファイル内のリンクをローカルのリンクに変換します。
- `--adjust-extension`: HTMLファイルに適切な拡張子を付けます。
- `--page-requisites`: ページを表示するために必要なすべての画像やCSS、JavaScriptファイルをダウンロードします。
- `--no-parent`: 親ディレクトリを辿らないようにします。

例えば、`https://example.com` をダウンロードする場合は、上記のコマンドをそのまま使用できます
[1](https://qiita.com/suin/items/7241135f1684636652ac)
[2](https://stysk.com/posts/2024/04/01/download_entire_website_using_wget/)。
