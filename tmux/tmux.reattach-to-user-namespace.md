# reattach-to-user-namespace

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