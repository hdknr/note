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

### 1. KEY BINDINGS

- わすれたら `プロンプト` で [:list-keys](key_binding/list-keys.md)
- [デフォルトバインディング](key_bindings)

### 2. [COMMANDS](commands)

### 3. CLIENTS AND SESSIONS

- [attach-session](client_and_session/attach-session.md) セッションを再現

### 4. [WINDOWS AND PANES](windows_and_panes)

- [rename-window](windows_and_panes/rename-window.md) タイトルの変更

### 5. [KEY BINDINGS](key_binding)(設定)

- [bind-key](key_bindings/bind-key.md) (`bind`) キーバインドの設定
- [list-keys](key_bindings_list-keys.md) (`lsk`) キーバイドの一覧
- [unbind-key](key_bindings/unbind-key.md) (`unbind`) キーバインドの解除

### 6. OPTIONS

- [set-option](options/set-option.md) (`set`)
- [set-window-option](options/set-window-option.md) (`setw`)
- [show-options](options/show-options.md) (`show`)
- [show-window-options](options/show-window-options.md)(`showw`)

### 7. HOOKS

### 8. MOUSE SUPPORT

### 9. [FORMATS](formats)

### 10. NAMES AND TITLES

### 11. ENVIRONMENT

### 12. [STATUS LINE](status_line)

### 13. BUFFERS

### 14. MISCELLANEOUS

### 15. CONTROL MODE

### 16. FILES

| ファイル          | 内容                      |
|------------------|--------------------------|
| `~/.tmux.conf`   | デフォルトの設定ファイル     |
| `/etc/tmux.conf` | システムワイドの設定ファイル  |

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
