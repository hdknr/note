
# [KEY BINDINGS](http://man7.org/linux/man-pages/man1/tmux.1.html#KEY_BINDINGS)

- [デフォルト](../default_key_bindings)

tmux allows a command to be bound to most keys, with or without a pre‐
fix key.  When specifying keys, most represent themselves (for example
‘A’ to ‘Z’).  Ctrl keys may be prefixed with ‘C-’ or ‘^’, and Alt
(meta) with ‘M-’.  In addition, the following special key names are
accepted: Up, Down, Left, Right, BSpace, BTab, DC (Delete), End, Enter,
Escape, F1 to F12, Home, IC (Insert), NPage/PageDown/PgDn,
PPage/PageUp/PgUp, Space, and Tab.  Note that to bind the ‘"’ or ‘'’
keys, quotation marks are necessary, for example:

           bind-key '"' split-window
           bind-key "'" new-window

## コマンド

- [bind-key](bind-key.md) (`bind`)
- [list-keys](list-keys.md) (`lsk`)
- send-keys (`send`)
- send-prefix
- [unbind-key](unbind-key.md)  (`unbind`)

## 確認

- [tmux のキーバインドを調べる方法 - Qiita](https://qiita.com/catatsuy/items/5c80ff1f15bb226640eb)

手順:

- `[prefix]` + `:` でプロンプト
- プロンプトで `:list-keys`
