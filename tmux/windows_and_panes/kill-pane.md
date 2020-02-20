# `kill-pane`: ペインを閉じる (`[prefix]` + `x`)

    kill-pane [-a] [-t target-pane]
    (alias: killp)

Destroy the given pane.  

If no panes remain in the containing window, it is also destroyed.  
(最後のペインだと`window`も閉じます)

The `-a` option kills all but the pane given with `-t`.
(`-a` で全閉じ。ただし`-t ターゲット` は除く)

## デフォルトのバインディング(`[prefix]` + `x`)

[confir-before](../status_line/confirm-before.md) で確認プロンプトが出ます:

    confirm-before -p "kill-pane #P? (y/n)" kill-pane
