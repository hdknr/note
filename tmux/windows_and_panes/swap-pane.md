# `swap-pane`: ２つのペインを交換する (`[prefix]` + `{` / `[prefix]` + `}`)

    swap-pane [-dDU] [-s src-pane] [-t dst-pane]
    (alias: swapp)

Swap two panes.  

If `-U` is used and no source pane is specified with `-s`, 
**dst-pane** is swapped with the previous pane 
(before it numerically);
`-D` swaps with the next pane (after it numeri‐ cally).  
`-d` instructs tmux not to change the active pane.

If `-s` is omitted and a marked pane is present
(see [select-pane -m](select-pane.md)),
the marked pane is used rather than the current pane.
