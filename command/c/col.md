# col -- filter reverse line feeds from input

~~~bash
man zshexpn | col -bx > ~/Downloads/zshexpn.md
~~~

| 項目	| 説明 | 
| :-----| :---- |
| -b	| 使用中の出力デバイスにバックスペース文字機能がないものと想定します。このとき、2 文字以上が同じ位置に表示されることになると、出力には最後に読み取られた文字が表示されます。 |
| -f	| 入力の中の半行動作のデフォルトの処理を抑制します。通常 col コマンドは、入力の中で半行動作を受け入れても、出力に半行動作を行うことはありません。このフラグを使うと、出力中に正方向半改行 (hlf) は含まれますが、逆方向改行 (flr および hlr) は含まれません。 |
| -p	| 逆方向改行動作による過剰出力の発生を仮定して、未知のエスケープ・シーケンスを文字として表示します。 通常 col コマンドはエスケープ・シーケンスを無視します。 |
| -x	| タブをホワイト・スペースに変換します。| 
| -T *Name* |	Name 変数で指定したワークステーション仕様を使用します。「タイプライター型デバイスとライン・プリンターの端末名」のための Name 変数については、nroff コマンドの -TName フラグのセクションを参照してください。デフォルトは 37 です。 |
| -l *Number* | (小文字の L) 指定された行数のテキストを、処理中にメモリーからバッファーに送信します。 |

## 関連

- [man](../m/man)