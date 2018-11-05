# tmux (#96)

- [tmux/tmux](https://github.com/tmux/tmux)
- [man](http://man7.org/linux/man-pages/man1/tmux.1.html)

## トピック

### 1. KEY BINDINGS

### 2. COMMANDS

### 3. CLIENTS AND SESSIONS

- [attach-session](client_and_session/attach-session.md) セッションを再現

### 4. WINDOWS AND PANES

- [rename-window](windows_and_panes/rename-window.md) タイトルの変更

### 5. KEY BINDINGS(設定)

- [bind-key](key_bindings/bind-key.md) キーバインドの設定

### 6. OPTIONS

### 7. HOOKS

### 8. MOUSE SUPPORT

### 9. FORMATS

### 10. NAMES AND TITLES

### 11. ENVIRONMENT

### 12. STATUS LINE

### 13. BUFFERS

### 14. MISCELLANEOUS

### 15. CONTROL MODE

### 16. FILES

| ファイル          | 内容                      |
|------------------|--------------------------|
| `~/.tmux.conf`   | デフォルトの設定ファイル     |
| `/etc/tmux.conf` | システムワイドの設定ファイル  |

## インストール

### install: Mac Homebrew

~~~
$ brew install tmux
~~~

### install: CentOS

- [tmux: CentOS 6.3にインストール記録](https://github.com/hdknr/scriptogr.am/blob/master/posts/20140128-tmux-centos.md)

~~~
$ sudo yum groupinstall 'Development Tools'

$ mkdir src && cd src
$ wget https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz --no-check-certificate
$ tar zxvf libevent-2.0.21-stable.tar.gz
$ cd libevent-2.0.21-stable
$ cd /etc/ld.so.conf.d/
$ echo /usr/local/lib  |sudo tee -a libevent2.conf
/usr/local/lib
$ sudo ldconfig  
~~~

- tmux 2.0

~~~
$ cd && cd src
$ sudo yum install ncurses-devel
$ wget http://downloads.sourceforge.net/tmux/tmux-2.0.tar.gz
$ tar xvfz tmux-2.0.tar.gz
$ cd tmux-2.0
$ tmux -V
tmux 2.0
~~~

### install : Ubuntu LTS 14.04

- [ppa:pi-rho/dev](https://launchpad.net/~pi-rho/+archive/ubuntu/dev)

~~~bash
$ sudo apt-get update
$ sudo apt-get install -y python-software-properties software-properties-common
$ sudo add-apt-repository -y ppa:pi-rho/dev
$ sudo apt-get update
$ sudo apt-get install -y tmux
$ tmux -V
tmux 2.0
~~~

## tmux-cssh : TMUX-C(luster)-SSH

- https://github.com/dennishafemann/tmux-cssh
- http://yuuki.hatenablog.com/entry/tmux-ssh-mackerel




## reattach-to-user-namespace

- [ChrisJohnsen/tmux-MacOSX-pasteboard](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard)
- [tmuxとMacのクリップボードを共有する（copy-mode, vim）](http://qiita.com/upinetree/items/cd80bc7865c52091be10)
- [tmux下でElectronがうまく動作しない](http://qiita.com/itkrt2y/items/dee87c406617d1bd45a6)


~~~bash
$ brew install reattach-to-user-namespace
==> Downloading https://homebrew.bintray.com/bottles/reattach-to-user-namespace-2.4.el_capitan.bottle.tar.gz
######################################################################## 100.0%
==> Pouring reattach-to-user-namespace-2.4.el_capitan.bottle.tar.gz
🍺  /usr/local/Cellar/reattach-to-user-namespace/2.4: 6 files, 34K

$ which reattach-to-user-namespace
/usr/local/bin/reattach-to-user-namespace
~~~

~~~bash
$ reattach-to-user-namespace atom -v
Atom    : 1.8.0
Electron: 0.36.8
Chrome  : 47.0.2526.110
Node    : 5.1.1
~~~

## 問題

- [tmuxへのアタッチで画面サイズが合わない時は-d - Qiita](https://qiita.com/maueki/items/dec71193560955f15e5f)

## リンク

- http://robots.thoughtbot.com/a-tmux-crash-course
- http://qiita.com/succi0303/items/cb396704493476373edf
- [Quickly open projects in tmux with split window configuration](https://bbs.archlinux.org/viewtopic.php?id=192923)
- [
tmuxを使い始めたので基本的な機能の使い方とかを整理してみた](http://kanjuku-tomato.blogspot.jp/2014/02/tmux.html)
