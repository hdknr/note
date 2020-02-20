# `break-pane`

    break-pane [-dP] [-F format] [-n window-name] [-s src-pane] [-t dst-window]
    (alias: breakp)

Break src-pane off from its containing window to make it the only pane in dst-window.  

If `-d` is given, the new window does not become the current window.  

The `-P` option prints information about the new window after it has been created.  

By default, 
it uses the format `‘#{session_name}:#{window_index}’`
but a different format may be specified with `-F`.
