# zcat


macOS(FreeBSD):

- gzcat
- `gunzip -c` 
- `gzip -cd`
  
~~~
zcat は、 gunzip -c と同一です。 
(いくつかのシステムでは、 zcat は compress へのオリジナルのリンクを保存しておくために gzcat としてインストールされているかもしれません。) 
zcat は、コマンドラインで指定されたファイルか標準入力からの入力を伸長し、 標準出力へ伸長したデータを出力します。 
zcat は、 .gz 拡張子であろうとなかろうと、マジックナンバが正しければファイルを伸長 します。
~~~
