# [WINDOWS AND PANES](http://man7.org/linux/man-pages/man1/tmux.1.html#WINDOWS_AND_PANES)

## モード

- [コピーモード](copy-mode.md)

## Window

Each window displayed by tmux may be split into one or more panes; each
pane takes up a certain area of the display and is a separate terminal.
A window may be split into panes using the split-window command.  Win‐
dows may be split horizontally (with the -h flag) or vertically.  Panes
may be resized with the resize-pane command (bound to ‘C-Up’, ‘C-Down’
‘C-Left’ and ‘C-Right’ by default), the current pane may be changed
with the select-pane command and the rotate-window and swap-pane com‐
mands may be used to swap panes without changing their position.  Panes
are numbered beginning from zero in the order they are created.

A number of preset layouts are available.  These may be selected with
the select-layout command or cycled with next-layout (bound to ‘Space’
by default); once a layout is chosen, panes within it may be moved and
resized as normal.

The following layouts are supported:

`even-horizontal`:

- Panes are spread out evenly from left to right across the window.

`even-vertical`:

- Panes are spread evenly from top to bottom.

`main-horizontal`:

- A large (main) pane is shown at the top of the window and the remaining panes are spread from left to right in the leftover space at the bottom.  
- Use the `main-pane-height` window option to specify the height of the top pane.

`main-vertical`:

- Similar to main-horizontal but the large pane is placed on the left and the others spread from top to bottom along the right.
- See the `main-pane-width` window option.

`tiled`

- Panes are spread out as evenly as possible over the window in both rows and columns.

In addition, select-layout may be used to apply a previously 
used layout - the [list-windows](list-windows.md) command displays the layout of each window in a form suitable for use with [select-layout](select-layout.md).  

For example:

        $ tmux list-windows
        0: ksh [159x48]
        layout: bb62,159x48,0,0{79x48,0,0,79x48,80,0}
        $ tmux select-layout bb62,159x48,0,0{79x48,0,0,79x48,80,0}

tmux automatically adjusts the size of the layout for the current window size.  

Note that a layout cannot be applied to a window with more
panes than that from which the layout was originally defined.

## コマンド

### Windows

- find-window
- kill-window
- last-window
- link-window
- [list-windows](list-windows.md)
- move-window
- new-window
- [next-window](next-window.md)
- previous-window
- [rename-window](rename-windows.md)
- resize-window
- respawn-window
- rotate-window
- select-window
- [split-window](split-window.md): ウインドウを２つのペインに分割 (`[prefix]` + `%`, `[prefix]` + `"`)
- swap-window
- unlink-window

## Layouts

- next-layout
- previous-layout
- select-layout

### Panes

- break-pane
- capture-pane
- choose-client
- choose-tree
- [display-panes](display-panes.md): 番号表示と移動 (`[prefix]` + `q`)
- [join-pane](join-pane.md)
- [kill-pane](kill-pane.md):ペインを閉じる (`[prefix]` + `x`)
- [last-pane](last-pane.md):前回のペインを選択する  (`[prefix]` + `;`)
- [list-panes](list-pane.md): 一覧
- [move-pane](move-pane.md)
- pipe-pane
- resize-pane
- respawn-pane
- [swap-pane](swap-pane.md): ２つのペインを交換する (`[prefix]` + `{` / `[prefix]` + `}`)
- [select-pane](select-pane.md): 指定したペインへ移動 (`selectp`)
