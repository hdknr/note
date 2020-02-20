# tmux (#96)

- [tmux/tmux](https://github.com/tmux/tmux)
- [man](http://man7.org/linux/man-pages/man1/tmux.1.html)

## 最小設定

~/.tmux.conf:

~~~conf
unbind C-b
set -g prefix C-a            # [prefix] = Ctrl + A
setw -g mode-keys vi         # コピーモード(viキーバインド)
~~~

## 機能

### [DEFAULT KEY BINDINGS](default_key_bindings)

### [COMMAND PARSING AND EXECUTION](http://man7.org/linux/man-pages/man1/tmux.1.html#COMMAND_PARSING_AND_EXECUTION)

### [PARSING SYNTAX](http://man7.org/linux/man-pages/man1/tmux.1.html#PARSING_SYNTAX)

### [COMMANDS](commands)

### [CLIENTS AND SESSIONS](client_and_session)

- [attach-session](client_and_session/attach-session.md) セッションを再現

### [WINDOWS AND PANES](windows_and_panes)

- [rename-window](windows_and_panes/rename-window.md) タイトルの変更

### [KEY BINDINGS](key_bindings)

- わすれたら `プロンプト` で [:list-keys](key_binding/list-keys.md)
- [デフォルトバインディング](key_bindings)

コマンド:

- [bind-key](key_bindings/bind-key.md) (`bind`) キーバインドの設定
- [list-keys](key_bindings_list-keys.md) (`lsk`) キーバイドの一覧
- [unbind-key](key_bindings/unbind-key.md) (`unbind`) キーバインドの解除

### [OPTIONS](options)

- [set-option](options/set-option.md) (`set`)
- [set-window-option](options/set-window-option.md) (`setw`)
- [show-options](options/show-options.md) (`show`)
- [show-window-options](options/show-window-options.md)(`showw`)

### [HOOKS](http://man7.org/linux/man-pages/man1/tmux.1.html#HOOKS)

### [MOUSE SUPPORT](http://man7.org/linux/man-pages/man1/tmux.1.html#MOUSE_SUPPORT)

### [FORMATS](formats)

### [STYLES](http://man7.org/linux/man-pages/man1/tmux.1.html#STYLES)

### [NAMES AND TITLES](http://man7.org/linux/man-pages/man1/tmux.1.html#NAMES_AND_TITLES)

### [GLOBAL AND SESSION ENVIRONMENT](http://man7.org/linux/man-pages/man1/tmux.1.html#GLOBAL_AND_SESSION_ENVIRONMENT)

### [STATUS LINE](status_line)

- command-prompt
- [confirm-before](status_line/confirm-before.md): 確認プロンプト
- display-menu
- display-message

### [BUFFERS](http://man7.org/linux/man-pages/man1/tmux.1.html#BUFFERS)

### [MISCELLANEOUS](http://man7.org/linux/man-pages/man1/tmux.1.html#MISCELLANEOUS)

### [TERMINFO EXTENSIONS](http://man7.org/linux/man-pages/man1/tmux.1.html#TERMINFO_EXTENSIONS
)
### [CONTROL MODE](http://man7.org/linux/man-pages/man1/tmux.1.html#CONTROL_MODE)

### [ENVIRONMENT](http://man7.org/linux/man-pages/man1/tmux.1.html#ENVIRONMENT)

### [FILES](http://man7.org/linux/man-pages/man1/tmux.1.html#FILES)

| ファイル          | 内容                      |
|------------------|--------------------------|
| `~/.tmux.conf`   | デフォルトの設定ファイル     |
| `/etc/tmux.conf` | システムワイドの設定ファイル  |

### [EXAMPLES](http://man7.org/linux/man-pages/man1/tmux.1.html#EXAMPLES)

## トピック

- [インストール](tmux.install.md)
- [tmux-cssh](tmux-cssh.md)
- [reattach-to-user-namespace](tmux.reattach-to-user-namespace.md) (クリップボード共有)

## 問題

- [tmuxへのアタッチで画面サイズが合わない時は-d - Qiita](https://qiita.com/maueki/items/dec71193560955f15e5f)

## リンク

- [A tmux Crash Course](https://thoughtbot.com/blog/a-tmux-crash-course)
- [達人に学ぶ.tmux.confの基本設定 - Qiita](https://qiita.com/succi0303/items/cb396704493476373edf)
- [Quickly open projects in tmux with split window configuration](https://bbs.archlinux.org/viewtopic.php?id=192923)
- [tmuxを使い始めたので基本的な機能の使い方とかを整理してみた](http://kanjuku-tomato.blogspot.jp/2014/02/tmux.html)

## 参考

- [dotfiles/tmux.conf at master · kei500/dotfiles](https://github.com/kei500/dotfiles/blob/master/tmux.conf)
