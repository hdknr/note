# 複数レポジトリ

- [複数の入力ソースと出力アーティファクトのサンプル](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/sample-multi-in-out.html)

プライマリソース:

- source 属性で定義されます。

セカンダリソース:

- 他のすべてのソースはセカンダリソース
- secondarySources の下に表示されます。
- すべてのセカンダリソースは、独自のディレクトリにインストールされます。このディレクトリは、組み込みの環境変数 CODEBUILD_SRC_DIR_sourceIdentifer に保存されます。
