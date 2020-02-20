## [DEFAULT KEY BINDINGS](http://man7.org/linux/man-pages/man1/tmux.1.html#DEFAULT_KEY_BINDINGS)

プレフィックスキーのデフォルトは `C-b` (Ctrl-b)

| キー          | 内容                                                 | コマンドなど       |
|--------------|----------------------------------------------------- | ---------------- |
| C-b          | プレフィックスキー送信                                   |                  |
| C-o          | Rotate the panes in the current window forwards.     |                  |
| C-z          |Suspend the tmux client.                              |                  |
| !            |Break the current pane out of the window.             | [break-pane](../windows_and_pances/break-pane.md)       |
| "            |Split the current pane into two, top and bottom.      | [split-window -h](../windows_and_pances/split-window.md)|
| #            |List all paste buffers.                               |                  |
| $            |Rename the current session.                           |                  |
| %            |Split the current pane into two, left and right.      | [split-window -h](../windows_and_pances/split-window.md)|
| &            |Kill the current window.                              |                  |
| '            |Prompt for a window index to select.       | [confirm-before -p "kill-window #W? (y/n)" kill-window](../windows_and_pances/split-window.md)|
| (            |Switch the attached client to the previous session.  |                  |
| )            |Switch the attached client to the next session.      |                  |
| ,            |Rename the current window.                           |                  |
| -            |Delete the most recently copied buffer of text.      |                  |
| .            |Prompt for an index to move the current window.     |                  |
| 0 to 9       |Select windows 0 to 9.                              |[select-window -t :=n](../windows_and_pances/select-window.md) |
| :            |Enter the tmux command prompt.                      |[command-prompt](../status_line/command-prompt.md)     |
| ;            |Move to the previously active pane.                 |                  |
| =            |Choose which buffer to paste interactively from a list. |                  |
| ?            |List all key bindings.                              |[list-keys](../key_binding/list-keys.md) |
| D            |Choose a client to detach.                          |                  |
| L            |Switch the attached client back to the last session.|                  |
| [            |Enter copy mode to copy text or view the history. | [copy-mode](../windows_and_pances/copy-mode.md)      |
| ]            |Paste the most recently copied buffer of text.    |                  |
| c            |Create a new window.                              |                  |
| d            |Detach the current client.                        |                  |
| f            |Prompt to search for text in open windows.        |                  |
| i            |Display some information about the current window. |                  |
| l            |Move to the previously selected window.            |                  |
| n            |Change to the next window.                         |                  |
| o            |Select the next pane in the current window.        |                  |
| p            |Change to the previous window.                     |                  |
| q            |Briefly display pane indexes.                      |[display-panes](../windows_and_panes/display-panes.md) |
| r            |Force redraw of the attached client.               |                  |
| m            |Mark the current pane (see select-pane -m).        |                  |
| M            |Clear the marked pane.                              |                  |
| s            |Select a new session for the attached client interactively.    |                  |
| t            |Show the time.                              |                  |
| w            |Choose the current window interactively.    | [choose-tree -Zw](../windows_and_pances/close-tree.md)   |
| x            |Kill the current pane.  |[confirm-before -p "kill-pane #P? (y/n)" kill-pane](../windows_and_panes/kill-pane.md) |
| z            |Toggle zoom state of the current pane.              |                  |
| {            |Swap the current pane with the previous pane.       | [swap-pane -U](../windows_and_panes/swap-pane.md) |
| }            |Swap the current pane with the next pane.           | [swap-pane -D](../windows_and_panes/swap-pane.md) |
| ~            |Show previous messages from tmux, if any.           |                  |
| Page Up      |Enter copy mode and scroll one page up.             |                  |
| Up, Down Left, Right  | Change to the pane above, below, to the left, or to the right of the current pane. |                  |
| M-1 to M-5            | Arrange panes in one of the five preset layouts: even-horizontal, even-vertical, main-horizontal, main-vertical, or tiled.|                  |
| Space        | Arrange the current window in the next preset layout.   |                  |
| M-n          | Move to the next window with a bell or activity marker. |                  |
| M-o          | Rotate the panes in the current window backwards.       |                  |
| M-p          | Move to the previous window with a bell or activity marker.     |                  |
| C-Up, C-Down ,C-Left, C-Right | Resize the current pane in steps of one cell.  |                  |
| M-Up, M-Down ,M-Left, M-Right | Resize the current pane in steps of five cells.|                  |
