# WINDOWS AND PANES

- [コピーモード](copy-mode.md)

## ウィンドウ

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

     even-horizontal
             Panes are spread out evenly from left to right across the win‐
             dow.

     even-vertical
             Panes are spread evenly from top to bottom.

     main-horizontal
             A large (main) pane is shown at the top of the window and the
             remaining panes are spread from left to right in the leftover
             space at the bottom.  Use the main-pane-height window option to
             specify the height of the top pane.

     main-vertical
             Similar to main-horizontal but the large pane is placed on the
             left and the others spread from top to bottom along the right.
             See the main-pane-width window option.

     tiled   Panes are spread out as evenly as possible over the window in
             both rows and columns.

     In addition, select-layout may be used to apply a previously used lay‐
     out - the list-windows command displays the layout of each window in a
     form suitable for use with select-layout.  For example:

           $ tmux list-windows
           0: ksh [159x48]
               layout: bb62,159x48,0,0{79x48,0,0,79x48,80,0}
           $ tmux select-layout bb62,159x48,0,0{79x48,0,0,79x48,80,0}

     tmux automatically adjusts the size of the layout for the current win‐
     dow size.  Note that a layout cannot be applied to a window with more
     panes than that from which the layout was originally defined.

     Commands related to windows and panes are as follows:

     break-pane [-dP] [-F format] [-n window-name] [-s src-pane] [-t
             dst-window]
                   (alias: breakp)
             Break src-pane off from its containing window to make it the
             only pane in dst-window.  If -d is given, the new window does
             not become the current window.  The -P option prints informa‐
             tion about the new window after it has been created.  By
             default, it uses the format ‘#{session_name}:#{window_index}’
             but a different format may be specified with -F.

     capture-pane [-aepPqCJ] [-b buffer-name] [-E end-line] [-S start-line]
             [-t target-pane]
                   (alias: capturep)
             Capture the contents of a pane.  If -p is given, the output
             goes to stdout, otherwise to the buffer specified with -b or a
             new buffer if omitted.  If -a is given, the alternate screen is
             used, and the history is not accessible.  If no alternate
             screen exists, an error will be returned unless -q is given.
             If -e is given, the output includes escape sequences for text
             and background attributes.  -C also escapes non-printable char‐
             acters as octal \xxx.  -J joins wrapped lines and preserves
             trailing spaces at each line's end.  -P captures only any out‐
             put that the pane has received that is the beginning of an as-
             yet incomplete escape sequence.

             -S and -E specify the starting and ending line numbers, zero is
             the first line of the visible pane and negative numbers are
             lines in the history.  ‘-’ to -S is the start of the history
             and to -E the end of the visible pane.  The default is to cap‐
             ture only the visible contents of the pane.

     choose-client [-NZ] [-F format] [-f filter] [-O sort-order] [-t
             target-pane] [template]
             Put a pane into client mode, allowing a client to be selected
             interactively from a list.  -Z zooms the pane.  The following
             keys may be used in client mode:

                   Key    Function
                   Enter  Choose selected client
                   Up     Select previous client
                   Down   Select next client
                   C-s    Search by name
                   n      Repeat last search
                   t      Toggle if client is tagged
                   T      Tag no clients
                   C-t    Tag all clients
                   d      Detach selected client
                   D      Detach tagged clients
                   x      Detach and HUP selected client
                   X      Detach and HUP tagged clients
                   z      Suspend selected client
                   Z      Suspend tagged clients
                   f      Enter a format to filter items
                   O      Change sort order
                   v      Toggle preview
                   q      Exit mode

             After a client is chosen, ‘%%’ is replaced by the client name
             in template and the result executed as a command.  If template
             is not given, "detach-client -t '%%'" is used.

             -O specifies the initial sort order: one of ‘name’, ‘size’,
             ‘creation’, or ‘activity’.  -f specifies an initial filter: the
             filter is a format - if it evaluates to zero, the item in the
             list is not shown, otherwise it is shown.  If a filter would
             lead to an empty list, it is ignored.  -F specifies the format
             for each item in the list.  -N starts without the preview.
             This command works only if at least one client is attached.

     choose-tree [-GNswZ] [-F format] [-f filter] [-O sort-order] [-t
             target-pane] [template]
             Put a pane into tree mode, where a session, window or pane may
             be chosen interactively from a list.  -s starts with sessions
             collapsed and -w with windows collapsed.  -Z zooms the pane.
             The following keys may be used in tree mode:

                   Key    Function
                   Enter  Choose selected item
                   Up     Select previous item
                   Down   Select next item
                   x      Kill selected item
                   X      Kill tagged items
                   <      Scroll list of previews left
                   >      Scroll list of previews right
                   C-s    Search by name
                   n      Repeat last search
                   t      Toggle if item is tagged
                   T      Tag no items
                   C-t    Tag all items
                   :      Run a command for each tagged item
                   f      Enter a format to filter items
                   O      Change sort order
                   v      Toggle preview
                   q      Exit mode

             After a session, window or pane is chosen, ‘%%’ is replaced by
             the target in template and the result executed as a command.
             If template is not given, "switch-client -t '%%'" is used.

             -O specifies the initial sort order: one of ‘index’, ‘name’, or
             ‘time’.  -f specifies an initial filter: the filter is a format
             - if it evaluates to zero, the item in the list is not shown,
             otherwise it is shown.  If a filter would lead to an empty
             list, it is ignored.  -F specifies the format for each item in
             the tree.  -N starts without the preview.  -G includes all ses‐
             sions in any session groups in the tree rather than only the
             first.  This command works only if at least one client is
             attached.

     display-panes [-b] [-d duration] [-t target-client] [template]
                   (alias: displayp)
             Display a visible indicator of each pane shown by
             target-client.  See the display-panes-colour and
             display-panes-active-colour session options.  The indicator is
             closed when a key is pressed or duration milliseconds have
             passed.  If -d is not given, display-panes-time is used.  A
             duration of zero means the indicator stays until a key is
             pressed.  While the indicator is on screen, a pane may be cho‐
             sen with the ‘0’ to ‘9’ keys, which will cause template to be
             executed as a command with ‘%%’ substituted by the pane ID.
             The default template is "select-pane -t '%%'".  With -b, other
             commands are not blocked from running until the indicator is
             closed.

     find-window [-CNTZ] [-t target-pane] match-string
                   (alias: findw)
             Search for the fnmatch(3) pattern match-string in window names,
             titles, and visible content (but not history).  The flags con‐
             trol matching behavior: -C matches only visible window con‐
             tents, -N matches only the window name and -T matches only the
             window title.  The default is -CNT.  -Z zooms the pane.

             This command works only if at least one client is attached.

     join-pane [-bdhv] [-l size | -p percentage] [-s src-pane] [-t dst-pane]
                   (alias: joinp)
             Like split-window, but instead of splitting dst-pane and creat‐
             ing a new pane, split it and move src-pane into the space.
             This can be used to reverse break-pane.  The -b option causes
             src-pane to be joined to left of or above dst-pane.

             If -s is omitted and a marked pane is present (see select-pane
             -m), the marked pane is used rather than the current pane.

     kill-pane [-a] [-t target-pane]
                   (alias: killp)
             Destroy the given pane.  If no panes remain in the containing
             window, it is also destroyed.  The -a option kills all but the
             pane given with -t.

     kill-window [-a] [-t target-window]
                   (alias: killw)
             Kill the current window or the window at target-window, remov‐
             ing it from any sessions to which it is linked.  The -a option
             kills all but the window given with -t.

     last-pane [-de] [-t target-window]
                   (alias: lastp)
             Select the last (previously selected) pane.  -e enables or -d
             disables input to the pane.

     last-window [-t target-session]
                   (alias: last)
             Select the last (previously selected) window.  If no
             target-session is specified, select the last window of the cur‐
             rent session.

     link-window [-adk] [-s src-window] [-t dst-window]
                   (alias: linkw)
             Link the window at src-window to the specified dst-window.  If
             dst-window is specified and no such window exists, the
             src-window is linked there.  With -a, the window is moved to
             the next index up (following windows are moved if necessary).
             If -k is given and dst-window exists, it is killed, otherwise
             an error is generated.  If -d is given, the newly linked window
             is not selected.

     list-panes [-as] [-F format] [-t target]
                   (alias: lsp)
             If -a is given, target is ignored and all panes on the server
             are listed.  If -s is given, target is a session (or the cur‐
             rent session).  If neither is given, target is a window (or the
             current window).  For the meaning of the -F flag, see the
             FORMATS section.

     list-windows [-a] [-F format] [-t target-session]
                   (alias: lsw)
             If -a is given, list all windows on the server.  Otherwise,
             list windows in the current session or in target-session.  For
             the meaning of the -F flag, see the FORMATS section.

     move-pane [-bdhv] [-l size | -p percentage] [-s src-pane] [-t dst-pane]
                   (alias: movep)
             Like join-pane, but src-pane and dst-pane may belong to the
             same window.

     move-window [-ardk] [-s src-window] [-t dst-window]
                   (alias: movew)
             This is similar to link-window, except the window at src-window
             is moved to dst-window.  With -r, all windows in the session
             are renumbered in sequential order, respecting the base-index
             option.

     new-window [-adkP] [-c start-directory] [-F format] [-n window-name]
             [-t target-window] [shell-command]
                   (alias: neww)
             Create a new window.  With -a, the new window is inserted at
             the next index up from the specified target-window, moving win‐
             dows up if necessary, otherwise target-window is the new window
             location.

             If -d is given, the session does not make the new window the
             current window.  target-window represents the window to be cre‐
             ated; if the target already exists an error is shown, unless
             the -k flag is used, in which case it is destroyed.
             shell-command is the command to execute.  If shell-command is
             not specified, the value of the default-command option is used.
             -c specifies the working directory in which the new window is
             created.

             When the shell command completes, the window closes.  See the
             remain-on-exit option to change this behaviour.

             The TERM environment variable must be set to ‘screen’ or ‘tmux’
             for all programs running inside tmux.  New windows will auto‐
             matically have ‘TERM=screen’ added to their environment, but
             care must be taken not to reset this in shell start-up files.

             The -P option prints information about the new window after it
             has been created.  By default, it uses the format
             ‘#{session_name}:#{window_index}’ but a different format may be
             specified with -F.

     next-layout [-t target-window]
                   (alias: nextl)
             Move a window to the next layout and rearrange the panes to
             fit.

     next-window [-a] [-t target-session]
                   (alias: next)
             Move to the next window in the session.  If -a is used, move to
             the next window with an alert.

     pipe-pane [-IOo] [-t target-pane] [shell-command]
                   (alias: pipep)
             Pipe output sent by the program in target-pane to a shell com‐
             mand or vice versa.  A pane may only be connected to one com‐
             mand at a time, any existing pipe is closed before
             shell-command is executed.  The shell-command string may con‐
             tain the special character sequences supported by the
             status-left option.  If no shell-command is given, the current
             pipe (if any) is closed.

             -I and -O specify which of the shell-command output streams are
             connected to the pane: with -I stdout is connected (so anything
             shell-command prints is written to the pane as if it were
             typed); with -O stdin is connected (so any output in the pane
             is piped to shell-command).  Both may be used together and if
             neither are specified, -O is used.

             The -o option only opens a new pipe if no previous pipe exists,
             allowing a pipe to be toggled with a single key, for example:

                   bind-key C-p pipe-pane -o 'cat >>~/output.#I-#P'

     previous-layout [-t target-window]
                   (alias: prevl)
             Move to the previous layout in the session.

     previous-window [-a] [-t target-session]
                   (alias: prev)
             Move to the previous window in the session.  With -a, move to
             the previous window with an alert.

     rename-window [-t target-window] new-name
                   (alias: renamew)
             Rename the current window, or the window at target-window if
             specified, to new-name.

     resize-pane [-DLMRUZ] [-t target-pane] [-x width] [-y height]
             [adjustment]
                   (alias: resizep)
             Resize a pane, up, down, left or right by adjustment with -U,
             -D, -L or -R, or to an absolute size with -x or -y.  The
             adjustment is given in lines or cells (the default is 1).

             With -Z, the active pane is toggled between zoomed (occupying
             the whole of the window) and unzoomed (its normal position in
             the layout).

             -M begins mouse resizing (only valid if bound to a mouse key
             binding, see MOUSE SUPPORT).

     resize-window [-aADLUR] [-t target-window] [-x width] [-y height]
             [adjustment]
                   (alias: resizew)
             Resize a window, up, down, left or right by adjustment with -U,
             -D, -L or -R, to an absolute size with -x or -y, or to the size
             of the smallest or largest session (with -a or -A).  The
             adjustment is given in lines or cells (the default is 1).

             This command automatically sets the window-size option to
             manual for the window.

     respawn-pane [-c start-directory] [-k] [-t target-pane] [shell-command]
                   (alias: respawnp)
             Reactivate a pane in which the command has exited (see the
             remain-on-exit window option).  If shell-command is not given,
             the command used when the pane was created is executed.  The
             pane must be already inactive, unless -k is given, in which
             case any existing command is killed.  -c specifies a new work‐
             ing directory for the pane.

     respawn-window [-c start-directory] [-k] [-t target-window]
             [shell-command]
                   (alias: respawnw)
             Reactivate a window in which the command has exited (see the
             remain-on-exit window option).  If shell-command is not given,
             the command used when the window was created is executed.  The
             window must be already inactive, unless -k is given, in which
             case any existing command is killed.  -c specifies a new work‐
             ing directory for the window.

     rotate-window [-DU] [-t target-window]
                   (alias: rotatew)
             Rotate the positions of the panes within a window, either
             upward (numerically lower) with -U or downward (numerically
             higher).

     select-layout [-Enop] [-t target-pane] [layout-name]
                   (alias: selectl)
             Choose a specific layout for a window.  If layout-name is not
             given, the last preset layout used (if any) is reapplied.  -n
             and -p are equivalent to the next-layout and previous-layout
             commands.  -o applies the last set layout if possible (undoes
             the most recent layout change).  -E spreads the current pane
             and any panes next to it out evenly.

     select-pane [-DdegLlMmRU] [-P style] [-T title] [-t target-pane]
                   (alias: selectp)
             Make pane target-pane the active pane in window target-window,
             or set its style (with -P).  If one of -D, -L, -R, or -U is
             used, respectively the pane below, to the left, to the right,
             or above the target pane is used.  -l is the same as using the
             last-pane command.  -e enables or -d disables input to the
             pane.

             -m and -M are used to set and clear the marked pane.  There is
             one marked pane at a time, setting a new marked pane clears the
             last.  The marked pane is the default target for -s to
             join-pane, swap-pane and swap-window.

             Each pane has a style: by default the window-style and
             window-active-style options are used, select-pane -P sets the
             style for a single pane.  For example, to set the pane 1 back‐
             ground to red:

                   select-pane -t:.1 -P 'bg=red'

             -g shows the current pane style.

             -T sets the pane title.

     select-window [-lnpT] [-t target-window]
                   (alias: selectw)
             Select the window at target-window.  -l, -n and -p are equiva‐
             lent to the last-window, next-window and previous-window com‐
             mands.  If -T is given and the selected window is already the
             current window, the command behaves like last-window.

     split-window [-bdfhvP] [-c start-directory] [-l size | -p percentage]
             [-t target-pane] [shell-command] [-F format]
                   (alias: splitw)
             Create a new pane by splitting target-pane: -h does a horizon‐
             tal split and -v a vertical split; if neither is specified, -v
             is assumed.  The -l and -p options specify the size of the new
             pane in lines (for vertical split) or in cells (for horizontal
             split), or as a percentage, respectively.  The -b option causes
             the new pane to be created to the left of or above target-pane.
             The -f option creates a new pane spanning the full window
             height (with -h) or full window width (with -v), instead of
             splitting the active pane.  All other options have the same
             meaning as for the new-window command.

     swap-pane [-dDU] [-s src-pane] [-t dst-pane]
                   (alias: swapp)
             Swap two panes.  If -U is used and no source pane is specified
             with -s, dst-pane is swapped with the previous pane (before it
             numerically); -D swaps with the next pane (after it numeri‐
             cally).  -d instructs tmux not to change the active pane.

             If -s is omitted and a marked pane is present (see select-pane
             -m), the marked pane is used rather than the current pane.

     swap-window [-d] [-s src-window] [-t dst-window]
                   (alias: swapw)
             This is similar to link-window, except the source and destina‐
             tion windows are swapped.  It is an error if no window exists
             at src-window.

             Like swap-pane, if -s is omitted and a marked pane is present
             (see select-pane -m), the window containing the marked pane is
             used rather than the current window.

     unlink-window [-k] [-t target-window]
                   (alias: unlinkw)
             Unlink target-window.  Unless -k is given, a window may be
             unlinked only if it is linked to multiple sessions - windows
             may not be linked to no sessions; if -k is specified and the
             window is linked to only one session, it is unlinked and
             destroyed.
