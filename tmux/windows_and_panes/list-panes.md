# `list-panes`: ペインの一覧

    list-panes [-as] [-F format] [-t target]
    (alias: lsp)

If `-a` is given, target is ignored and all panes on the server are listed.  

If `-s` is given, target is a session (or the current session).  

If neither is given, 
target is a window (or the current window).  

For the meaning of the -F flag, see the [FORMATS](../formats) section.
