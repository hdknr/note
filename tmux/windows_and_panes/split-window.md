# `split-window`: ウインドウを２つのペインに分割 

     split-window [-bdfhIvP] [-c start-directory] [-e environment] [-l size | -p percentage] [-t target-pane] [shell-command] [-F format]
    (alias: splitw)

Create a new pane by splitting `target-pane`: 
`-h` does a horizontal split(左右) and 
`-v` a vertical split(上下); 
if neither is specified, `-v` is assumed.  

デフォルトバインド:

- `-v`:  `[prefix]` + `"`
- `-h`:  `[prefix]` + `%`

The `-l` and `-p` options specify the size of the new pane in **lines**
(for vertical split) or in **cells** (for horizontal split),
or as a **percentage**, respectively.  

The `-b` option causes the new pane to be created to the left of or above **target-pane**.

The `-f` option creates a new pane spanning the full window height (with `-h`) 
or full window width (with `-v`), 
instead of splitting the active pane.

An empty shell-command ('') will create a pane with no command running in it.  
Output can be sent to such a pane with the [display-message](../status_line/display-message.md) command.  

The -I flag (if shell-command is not specified or empty) 
will create an empty pane and forward any output from **stdin** to it.  

For example:

    $ make 2>&1|tmux splitw -dI &

All other options have the same meaning as for the [new-window](new-window.md) command.
