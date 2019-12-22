# Latex (TeX Live)

## MacTeX

### 1. MacTeX

- pLaTeXという文書作成システムはTeX Liveと呼ばれく巨大なソフトウェアパッケージの一部として提供されています。
- TeX LiveはLinux, macOS (Mac), Windowsで動作します。それぞれのシステムごとにインストール方法は異なります。
- macOS向けにはMacTeXと呼ばれるMac専用のTeX Liveのインストーラが提供されています。

.pkg ファイル形式のパッケージをインストールする

~~~bash
brew cask install mactex
~~~

### 2. PDF

~~~bash
brew install ghostscript
brew install imagemagick
~~~

~~~bash
brew cask install skim
~~~

### 3. latexmk の設定

~~~perl
#!/usr/bin/env perl
$latex            = 'platex -synctex=1 -halt-on-error';
$latex_silent     = 'platex -synctex=1 -halt-on-error -interaction=batchmode';
$bibtex           = 'pbibtex';
$biber            = 'biber --bblencoding=utf8 -u -U --output_safechars';
$dvipdf           = 'dvipdfmx %O -o %D %S';
$makeindex        = 'mendex %O -o %D %S';
$max_repeat       = 5;
$pdf_mode         = 3;
$pvc_view_file_via_temporary = 0;
$pdf_previewer    = "open -ga /Applications/Skim.app";
~~~

### 4. update

~~~bash
sudo tlmgr update --self --all
~~~

- `/usr/local/texlive/2018/bin/x86_64-darwin/tlmgr` がフルパス

パスを通す:

~~~bash
sudo /usr/local/texlive/2018/bin/x86_64-darwin/tlmgr path add
~~~

### 5. ヒラギノ

~~~bash
sudo cjk-gs-integrate --link-texmf --force
sudo mktexlsr
sudo kanji-config-updmap-sys hiragino-elcapitan-pron
~~~

## 参考

- [MacBook Pro(macOS Sierra)にTeXを導入 - かっくんの学習記録](https://kakubari-ryusei.hatenablog.com/entry/2017/07/03/193907)
