# `select-pane` : 指定したペインへ移動 (`[prefix]` + `;`)

    select-pane [-DdeLlMmRU] [-T title] [-t target-pane]
    (alias: selectp)

Make pane `target-pane` the active pane in window target-window.

If one of `-D`, `-L`, `-R`, or `-U` is used, respectively the pane
below, to the left, to the right, or above the target pane is
used.  

`-l` is the same as using the [last-pane](last-pane.md) command.  

`-e` enables or `-d` disables input to the pane.  

`-T` sets the pane title.

`-m` and `-M` are used to set and clear the marked pane.  

There is one marked pane at a time,
setting a new marked pane clears the last.  

The marked pane is the default target for `-s` to [join-pane](join-pane.md), [swap-pane](swap-pane.md) and [swap-window](swap-window.md).
