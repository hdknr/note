## 正規表現

- [Vimで使える正規表現](http://archiva.jp/web/tool/vim_regexps.html)

## 挿入モードになったらアンダーライン
- .vimrc

```
"" 挿入モードの時だけハイライト処理
""
autocmd InsertLeave * set nocursorline
autocmd InsertEnter * set cursorline

"" ハイライト設定
"" 		- ctermbg = 背景色を変えたい時(NONEでなし)
"" 		- cterm = underline 
highlight CursorLine ctermbg=NONE cterm=underline
```

- [色の参考](http://d.hatena.ne.jp/connvoi_tyou/20080306/1204825179)

## vimproc_linux64.so

~~~
vimproc's DLL: "/home/hdknr/.vim/bundle/vimproc/autoload/

vimproc_linux64.so" is not found.  Please read :help vimproc and make it.
~~~

~~~
$ cd .vim/bundle/vimproc

$ make
make -f make_unix.mak
make[1]: ディレクトリ `/home/hdknr/.vim/bundle/vimproc' に入ります
cc -W -O2 -Wall -Wno-unused -Wno-unused-parameter -std=gnu99 -pedantic -shared -fPIC -o autoload/vimproc_linux64.so autoload/proc.c -lutil
make[1]: ディレクトリ `/home/hdknr/.vim/bundle/vimproc' から出ます
~~~	

## neobundle#rc() is deprecated function

- [参考](https://rcmdnk.github.io/blog/2014/10/27/computer-vim-markdown/)

~~~
$ more ~/.vimrc.neobundle 

"call neobundle#rc(expand('~/.vim/bundle/'))
call neobundle#begin(expand('~/.vim/bundle/'))

....

call neobundle#end()

NeoBundleCheck
~~~

## Debian:7.4 ソースインストール

~~~
$ sudo apt-get install ncurses-dev build-essential mercurial
~~~

~~~
$ hg clone https://vim.googlecode.com/hg/ vim
~~~

~~~
$ cd vim/src
$ make distclean
$ ./configure --with-features=huge --enable-pythoninterp --enable-rubyinterp
$ make
$ sudo make install
~~~

~~~
$ which vim
/usr/local/bin/vim
~~~