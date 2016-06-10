vim: PHP PSR-2 チェック

- [PSR-2](http://www.php-fig.org/psr/psr-2/)
- [新標準PSRに学ぶきれいなPHP](http://www.slideshare.net/yandod/psrphp)


## neobundle でsyntasticをバンドルする

- [neobundle](https://github.com/Shougo/neobundle.vim)
- [syntastic](https://github.com/scrooloose/syntastic)


~~~
$ vi ~/bin/home/.vimrc.neobundle 


NeoBundle 'scrooloose/syntastic'
~~~

~~~
$ grep neo ~/.vimrc 
source ~/bin/home/.vimrc.neobundle
~~~

### バンドル

~~~
$ vim

Not installed bundles:  ['syntastic']
Install bundles now?
(y)es, [N]o: y

[neobundle/install] Update started: (2014/11/12 10:30:52)
(1/1) [====================] syntastic
[neobundle/install] (1/1): |syntastic| Updated
[neobundle/install] |syntastic|  -> de5e025ef0b8a9eec588d618ebaebd104945af4c
[neobundle/install] Installed/Updated bundles:
syntastic
[neobundle/install] Update done: (2014/11/12 10:31:02)
続けるにはENTERを押すかコマンドを入力してください
~~~

## PHP_CodeSniffer 設定

- [Vim の Syntastic で PSR-2 コーディング規約でチェックするお話](http://yuzuemon.hatenablog.com/entry/2014/08/13/135412)。

### PEARでインストール

~~~
$ sudo pear install PHP_CodeSniffer
Unknown remote channel: pear.phpunit.de
Did not download optional dependencies: channel://pear.phpunit.de/PHP_Timer, use --alldeps to download automatically
pear/PHP_CodeSniffer can optionally use package "channel://pear.phpunit.de/PHP_Timer"
downloading PHP_CodeSniffer-1.5.5.tgz ...
Starting to download PHP_CodeSniffer-1.5.5.tgz (412,025 bytes)
.........................................done: 412,025 bytes
install ok: channel://pear.php.net/PHP_CodeSniffer-1.5.5
~~~

~~~
$ phpcs --version
PHP_CodeSniffer version 1.5.5 (stable) by Squiz (http://www.squiz.net)
~~~

~~~
$ phpcs -i 
The installed coding standards are MySource, PEAR, Squiz, PHPCS, PSR2, Zend and PSR1
~~~

### .vimrc

~~~

$ vim ~/.vimrc

" -- for PHP syntastic  -----------------------
let g:syntastic_mode_map = {
  \ 'mode': 'active',
  \ 'active_filetypes': ['php']
  \}
let g:syntastic_auto_loc_list = 1
let g:syntastic_php_checkers = ['phpcs']
let g:syntastic_php_phpcs_args='--standard=psr2'
~~~


