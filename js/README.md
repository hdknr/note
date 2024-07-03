# Javascript

## Web Storage API

- [ウェブストレージ API](https://developer.mozilla.org/ja/docs/Web/API/Web_Storage_API)
- [Next.js と TypeScript で、ユーザーの閲覧履歴を表示する方法](https://commte.net/nextjs-history)

- localStorage
- sessionStorage

## Origin Private File System (OPFS)

- [Origin Private File System を使ってブラウザ上でファイルを高速に操作しよう](https://zenn.dev/cybozu_frontend/articles/origin-private-file-system)
- [オリジンプライベートファイルシステム](https://developer.mozilla.org/ja/docs/Web/API/File_System_API/Origin_private_file_system)

## 違い

オリジンプライベートファイルシステム (OPFS) と Web Storage API の違いについて説明します。

- OPFS (オリジンプライベートファイルシステム):

  - OPFS は、[ファイルシステム API](https://developer.mozilla.org/ja/docs/Web/API/File_System_API) の一部として提供されるストレージエンドポイントです。
  - ページのオリジンに対して非公開で、ユーザーからは見えません。
  - パフォーマンスのために最適化されており、その場での書き込みアクセスを提供します。
  - ファイルシステムアクセス API を使用してファイルで作業する際に利用されます。
  - メインスレッドをブロックしない同期呼び出しも可能です。
  - ブラウザーストレージ容量制限の対象となります。
  - ユーザーから見えないため、権限プロンプトやセキュリティチェックは不要です .

- Web Storage API:

  - Web Storage API は、ブラウザー内でキーと値のペアを保存するための API です。
  - 主に localStorage と sessionStorage の 2 つのストレージメカニズムがあります。
  - ユーザーから見えるストレージであり、容量制限があります。
  - シンプルなデータの保存に適していますが、ファイルシステムのような高度な操作はできません。

簡潔に言えば、OPFS は高度なファイルアクセスを提供し、Web Storage API はシンプルなキー/値ストレージです。
