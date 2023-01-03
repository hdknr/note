# cut

- [cut command in Linux with examples
](https://www.geeksforgeeks.org/cut-command-linux-examples/)


## `-f` フィールド

~~~bash
% VG | grep virtualbox | cut -f 1 -d " "
2a5c0c7
41fbc96
e682552
~~~


## `-d` デリミタ

~~~bash
% head -n 1 ~/Downloads/instance.txt 
"i-0e7b7290dceb44acc"

% cat ~/Downloads/instance.txt| cut -d '"' -f 2
i-06d15d4c353a9e0c8
...
~~~


## 関連

- [tr](../t/tr.md)


## 資料

- [cutコマンドでtsvファイルを処理するには。](https://cufl.hateblo.jp/entry/2020/07/07/231725)
- [cut - ファイルの各行から一部分を切り出す - Linuxコマンド](https://webkaru.net/linux/cut-command/)