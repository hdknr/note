# COMMANDS

This section describes the commands supported by tmux.  

Most commands accept the optional `-t` (and sometimes `-s`) argument
with one of target-client, target-session, target-window, or target-pane.  
These specify the client, session, window or pane which a command should affect.

target-client should be the name of the client, 
typically the pty(4) file to which the client is connected, 
for example either of /dev/ttyp1 or ttyp1 for the client attached to /dev/ttyp1.  
If no client is specified, 
tmux attempts to work out the client currently in use; 
if that fails, an error is reported.  

Clients may be listed with the [list-clients](clinent_and_session/list-clients.md) command.

`target-session` is tried as, in order:

1. A session ID prefixed with a `$`.
2. An exact name of a session (as listed by the list-sessions command).
3. The start of a session name, for example `‘mysess’` would match a session named `‘mysession’`.
4. An fnmatch(3) pattern which is matched against the session name.

If the session name is prefixed with an `‘=’`, 
only an exact match is accepted 
(so `‘=mysess’` will only match exactly `‘mysess’`, not `‘mysession’`).

If a single session is found, it is used as the target session; multi‐
ple matches produce an error.  If a session is omitted, the current
session is used if available; if no current session is available, the
most recently used is chosen.

`target-window` (or `src-window` or `dst-window`) specifies a window in the form `session:window`.  
`session` follows the same rules as for `target-session`, 
and `window` is looked for in order as:

1. A special token, listed below.
2. A window index, for example `‘mysession:1’` is window 1 in session `‘mysession’`.
3. A window ID, such as `@1`.
4. An exact window name, such as `‘mysession:mywindow’`.
5. The start of a window name, such as `‘mysession:mywin’`.
6. As an fnmatch(3) pattern matched against the window name.

Like sessions, a `‘=’` prefix will do an exact match only.  

An empty window name specifies the next unused index if appropriate 
(for example the new-window and link-window commands) otherwise the current window in session is chosen.

The following special tokens are available to indicate particular windows.  
Each has a single-character alternative form.

     Token              Meaning
     {start}       ^    The lowest-numbered window
     {end}         $    The highest-numbered window
     {last}        !    The last (previously current) window
     {next}        +    The next window by number
     {previous}    -    The previous window by number

`target-pane` (or `src-pane` or `dst-pane`) may be a pane ID or takes a similar form to `target-window`
but with the optional addition of a period followed by a pane index or pane ID, for example: `‘mysession:mywindow.1’`.  

If the pane index is omitted,
the currently active pane in the specified window is used.  

The following special tokens are available for the pane index:

     Token                  Meaning
     {last}            !    The last (previously active) pane
     {next}            +    The next pane by number
     {previous}        -    The previous pane by number
     {top}                  The top pane
     {bottom}               The bottom pane
     {left}                 The leftmost pane
     {right}                The rightmost pane
     {top-left}             The top-left pane
     {top-right}            The top-right pane
     {bottom-left}          The bottom-left pane
     {bottom-right}         The bottom-right pane
     {up-of}                The pane above the active pane
     {down-of}              The pane below the active pane
     {left-of}              The pane to the left of the active pane
     {right-of}             The pane to the right of the active pane

The tokens `‘+’` and `‘-’` may be followed by an offset, 
for example:

           select-window -t:+2

In addition, 
`target-session`,`target-window` or `target-pane` may consist entirely of the token `‘{mouse}’` (alternative form `‘=’`)
to specify the session, window or pane where the most recent mouse event occurred 
(see the MOUSE SUPPORT section) or `‘{marked}’` (alternative form `‘~’`) to specify the marked pane (see select-pane -m).

Sessions, window and panes are each numbered with a unique ID; 
session IDs are prefixed with a ‘$’, windows with a ‘@’, and panes with a ‘%’.
These are unique and are unchanged for the life of the session, window or pane in the tmux server.  
The pane ID is passed to the child process of the pane in the TMUX_PANE environment variable.  
IDs may be displayed using the ‘session_id’, ‘window_id’, or ‘pane_id’ formats 
(see the FORMATS section) and the display-message, list-sessions, list-windows or list-panes commands.

shell-command arguments are sh(1) commands.  
This may be a single argu‐ ment passed to the shell, for example:

           new-window 'vi /etc/passwd'

Will run:

           /bin/sh -c 'vi /etc/passwd'

Additionally, 
the new-window, new-session, split-window, respawn-window and respawn-pane commands allow shell-command to be given 
as multiple arguments and executed directly (without ‘sh -c’).  
This can avoid issues with shell quoting.  

For example:

           $ tmux new-window vi /etc/passwd

Will run vi(1) directly without invoking the shell.

command [arguments] refers to a tmux command, either passed with the command and arguments separately, for example:

           bind-key F1 set-option status off

Or passed as a single string argument in .tmux.conf, for example:

        bind-key F1 { set-option status off }

Example tmux commands include:

           refresh-client -t/dev/ttyp2
           rename-session -tfirst newname
           set-option -wt:0 monitor-activity on
           new-window ; split-window -d
           bind-key R source-file ~/.tmux.conf \; \
                   display-message "source-file done"

Or from sh(1):

           $ tmux kill-window -t :1
           $ tmux new-window \; split-window -d
           $ tmux new-session -d 'vi /etc/passwd' \; split-window -d \; attach
