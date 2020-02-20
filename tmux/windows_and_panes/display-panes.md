# `display-panes`: 番号表示と移動 (`[prefix]` + `q`)

    display-panes [-b] [-d duration] [-t target-client] [template]
    (alias: displayp)

Display a visible indicator of each pane shown by `target-client`.  

See the `display-panes-colour` and `display-panes-active-colour` session options.  

The indicator is closed when a key is pressed or duration milliseconds have passed.  

If `-d` is not given, `display-panes-time` is used.  

A duration of `zero` means the indicator stays until a key is pressed.  
(`0` を設定するとキープレスされるまで待つ)

While the indicator is on screen, 
a pane may be chosen with the `‘0’` to `‘9’` keys, 
which will cause template to be executed as a command with `‘%%’` substituted by the pane ID.

The default template is `"select-pane -t '%%'"`.  

(数字キーを入力すると [select-pane -t '%%'](select-pane.md) でペインが移動される!)

With `-b`,
other commands are not blocked from running until the indicator is closed.

## 記事

- [tmuxで快適にpane移動 - Qiita](https://qiita.com/pocari/items/b1828c8aea8e3545cadd)
