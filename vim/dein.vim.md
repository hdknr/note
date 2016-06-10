- [Shougo/dein.vim](https://github.com/Shougo/dein.vim)
- [dein.vimを使ってみる](http://qiita.com/yoza/items/2f8bd33a18225754f346)
- [NeoBundle から dein.vim に乗り換えたら爆速だった話](http://qiita.com/delphinus35/items/00ff2c0ba972c6e41542)
- [NeoVim、そしてdein.vimへ](http://qiita.com/okamos/items/2259d5c770d51b88d75b)
- [NeoBundleからDein.vimへの移行](http://rcmdnk.github.io/blog/2016/03/10/computer-vim/)
- [VimとNeoVimのプラグインマネージャDein.vim ](http://kaworu.jpn.org/vim/Vim%E3%81%A8NeoVim%E3%81%AE%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3Dein.vim)


動作環境
- Vim 7.4 以上、もしくは、neovim
- gitコマンド


## install

~~~
$ curl https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh > installer.sh
~~~
~~~
$ sh installer.sh ~/.vim/dein
Install to "/Users/you/.vim/dein/repos/github.com/Shougo/dein.vim"...

git is /usr/local/bin/git

Begin fetching dein...
Cloning into '/Users/you/.vim/dein/repos/github.com/Shougo/dein.vim'...
remote: Counting objects: 2100, done.
remote: Compressing objects: 100% (208/208), done.
remote: Total 2100 (delta 125), reused 0 (delta 0), pack-reused 1876
Receiving objects: 100% (2100/2100), 311.95 KiB | 346.00 KiB/s, done.
Resolving deltas: 100% (1192/1192), done.
Checking connectivity... done.
Done.
~~~

~~~
Please add the following settings for dein to the top of your vimrc (Vim) or init.vim (NeoVim) file:


"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath^=/Users/you/.vim/dein/repos/github.com/Shougo/dein.vim

" Required:
call dein#begin(expand('/Users/you/.vim/dein'))

" Let dein manage dein
" Required:
call dein#add('Shougo/dein.vim')

" Add or remove your plugins here:
call dein#add('Shougo/neosnippet.vim')
call dein#add('Shougo/neosnippet-snippets')

" You can specify revision/branch/tag.
call dein#add('Shougo/vimshell', { 'rev': '3787e5' })

" Required:
call dein#end()

" Required:
filetype plugin indent on

" If you want to install not installed plugins on startup.
"if dein#check_install()
"  call dein#install()
"endif

"End dein Scripts-------------------------


Done.
Complete setup dein!
~~~
