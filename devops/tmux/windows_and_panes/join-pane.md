# `join-pane`

    join-pane [-bdhv] [-l size | -p percentage] [-s src-pane] [-t dst-pane]
    (alias: joinp)

Like split-window, 
but instead of splitting dst-pane and creating a new pane, 
split it and move src-pane into the space. 

This can be used to reverse break-pane.  
The -b option causes src-pane to be joined to left of or above dst-pane.

If -s is omitted and a marked pane is present 
(see select-pane -m), 
the marked pane is used rather than the current pane.

