- [Intrepid command line directory traversal  ](http://brettterpstra.com/2015/04/01/intrepid-command-line-directory-traversal/)
- [fasdチュートリアル(メモ)](http://qiita.com/S-Ito/items/bf877f1f50af75865273)


## Debian

~~~bash
~/src$ git clone https://github.com/clvv/fasd.git
~/src$ cd fasd

~/src/fasd$ sudo make install
install -d /usr/local/bin
install -m 755 fasd /usr/local/bin
install -d /usr/local/share/man/man1
install -m 644 fasd.1 /usr/local/share/man/man

$ which fasd
/usr/local/bin/fasd

~~~

- .bashrc

~~~bash
eval "$(fasd --init auto)"
~~~


## zz : インタラクティブにディレクトリの移動

- ディレクトリの候補がでる
- `左端番号` + `enter`  で移動
