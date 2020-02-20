# set-option (alias: set)

~~~bash
set-option [-aFgoqsuw] [-t target-session | target-window] option value
~~~~

Set a window option with -w (equivalent to the set-window-option command),
a server option with -s, otherwise a session option.

If `-g` is given, the global session or window option is set.

`-F` expands formats in the option value.

The -u flag unsets an option, so a session inherits the option from the global options
(or with -g, restores a global option to the default).

The -o flag prevents setting an option that is already set 
and the -q flag suppresses errors about unknown or ambiguous options.

With -a, and if the option expects a string or a style, 
value is appended to the existing setting. For example:

~~~bash
set -g status-left "foo"
set -ag status-left "bar"
~~~

Will result in ‘foobar’. And:

~~~bash
set -g status-style "bg=red"
set -ag status-style "fg=blue"
~~~

Will result in a red background and blue foreground. Without -a, 
the result would be the default background and a blue foreground.

Available window options are listed under set-window-option.

value depends on the option and may be a number, a string, or a flag (on, off, or omitted to toggle).

## Server Options

Available server options are:

### `buffer-limit` *number*

Set the number of buffers; as new buffers are added to the top of the stack, old ones are removed from the bottom if necessary to maintain this maximum length.

### `command-alias[]` *name=value*

This is an array of custom aliases for commands. If an unknown command matches name, it is replaced with value. For example, after:

~~~
set -s command-alias[100] zoom='resize-pane -Z'
~~~

Using:

~~~
zoom -t:.1
~~~

Is equivalent to:

~~~
resize-pane -Z -t:.1
~~~

Note that aliases are expanded when a command is parsed rather than when it is executed, so binding an alias with bind-key will bind the expanded form.

### `default-terminal` *terminal*

Set the default terminal for new windows created in this session - the default value of the TERM environment variable. For tmux to work correctly, this must be set to ‘screen’, ‘tmux’ or a derivative of them.

### `escape-time` *time*

Set the time in milliseconds for which tmux waits after an escape is input to determine if it is part of a function or meta key sequences. The default is 500 milliseconds.

### exit-empty [on | off]

If enabled (the default), the server will exit when there are no active sessions.

### exit-unattached [on | off]

If enabled, the server will exit when there are no attached clients.

### focus-events [on | off]

When enabled, focus events are requested from the terminal if supported and passed through to applications running in tmux. Attached clients should be detached and attached again after changing this option.

### history-file path

If not empty, a file to which tmux will write command prompt history on exit and load it from on start.

### message-limit number

Set the number of error or information messages to save in the message log for each client. The default is 100.

### set-clipboard [on | external | off]

Attempt to set the terminal clipboard content using the xterm(1) escape sequence, if there is an Ms entry in the terminfo(5) description (see the TERMINFO EXTENSIONS section).

If set to on, tmux will both accept the escape sequence to create a buffer and attempt to set the terminal clipboard. If set to external, tmux will attempt to set the terminal clipboard but ignore attempts by applications to set tmux buffers. If off, tmux will neither accept the clipboard escape sequence nor attempt to set the clipboard.

Note that this feature needs to be enabled in xterm(1) by setting the resource:

~~~
disallowedWindowOps: 20,21,SetXprop
~~~
        
Or changing this property from the xterm(1) interactive menu when required.

### terminal-overrides[] string

Allow terminal descriptions read using terminfo(5) to be overridden. Each entry is a colon-separated string made up of a terminal type pattern (matched using fnmatch(3)) and a set of name=value entries.
For example, to set the ‘clear’ terminfo(5) entry to ‘\e[H\e[2J’ for all terminal types matching ‘rxvt*’:

~~~
rxvt*:clear=\e[H\e[2J
~~~

The terminal entry value is passed through strunvis(3) before interpretation.

## Session Options

Available session options are:

### activity-action [any | none | current | other]

Set action on window activity when monitor-activity is on. any means activity in any window linked to a session causes a bell or message (depending on visual-activity) in the current window of that session, none means all activity is ignored (equivalent to monitor-activity being off), current means only activity in windows other than the current window are ignored and other means activity in the current window is ignored but not those in other windows.

### assume-paste-time milliseconds

If keys are entered faster than one in milliseconds, they are assumed to have been pasted rather than typed and tmux key bindings are not processed. The default is one millisecond and zero disables.

### base-index index

Set the base index from which an unused index should be searched when a new window is created. The default is zero.

### bell-action [any | none | current | other]

Set action on a bell in a window when monitor-bell is on. The values are the same as those for activity-action.

### default-command shell-command

Set the command used for new windows (if not specified when the window is created) to shell-command, which may be any sh(1) command. The default is an empty string, which instructs tmux to create a login shell using the value of the default-shell option.

### default-shell path

Specify the default shell. This is used as the login shell for new windows when the default-command option is set to empty, and must be the full path of the executable. When started tmux tries to set a default value from the first suitable of the SHELL environment variable, the shell returned by getpwuid(3), or /bin/sh. This option should be configured when tmux is used as a login shell.

### destroy-unattached [on | off]

If enabled and the session is no longer attached to any clients, it is destroyed.

### detach-on-destroy [on | off]

If on (the default), the client is detached when the session it is attached to is destroyed. If off, the client is switched to the most recently active of the remaining sessions.

### display-panes-active-colour colour

Set the colour used by the display-panes command to show the indicator for the active pane.

### display-panes-colour colour

Set the colour used by the display-panes command to show the indicators for inactive panes.

### display-panes-time time

Set the time in milliseconds for which the indicators shown by the display-panes command appear.

### display-time time

Set the amount of time for which status line messages and other on-screen indicators are displayed. If set to 0, messages and indicators are displayed until a key is pressed. time is in milliseconds.

### history-limit lines

Set the maximum number of lines held in window history. This setting applies only to new windows - existing window histories are not resized and retain the limit at the point they were created.

### key-table key-table

Set the default key table to key-table instead of root.

### lock-after-time number

Lock the session (like the lock-session command) after number seconds of inactivity. The default is not to lock (set to 0).

### lock-command shell-command

Command to run when locking each client. The default is to run lock(1) with -np.

### message-command-style style

Set status line message command style, where style is a comma-separated list of characteristics to be specified.
The style format is shared by many options and may be: ‘bg=colour’ to set the background colour, ‘fg=colour’ to set the foreground colour, and a list of attributes as specified below.

The colour is one of: black, red, green, yellow, blue, magenta, cyan, white, aixterm bright variants (if supported: brightred, brightgreen, and so on), colour0 to colour255 from the 256-colour set, default for the default colour (inherited from another option in the case of some options, for example window-status-style inherits from status-style), terminal for the terminal default colour, or a hexadecimal RGB string such as ‘#ffffff’.

The attributes is either none or a comma-delimited list of one or more of: bright (or bold), dim, underscore, blink, reverse, hidden, italics, strikethrough, double-underscore curly-underscore dotted-underscore or dashed-underscore to turn an attribute on, or an attribute prefixed with ‘no’ to turn one off.

Examples are:

~~~
fg=yellow,bold,underscore,blink
bg=black,fg=default,noreverse
~~~
        
With the -a flag to the set-option command the new style is added otherwise the existing style is replaced.

### message-style style

Set status line message style. For how to specify style, see the message-command-style option.

### mouse [on | off]

If on, tmux captures the mouse and allows mouse events to be bound as key bindings. See the MOUSE SUPPORT section for details.

### `prefix` *key*

Set the key accepted as a prefix key.
In addition to the standard keys described under KEY BINDINGS,
prefix can be set to the special key ‘None’ to set no prefix.

### `prefix2` *key*

Set a secondary key accepted as a prefix key. Like prefix, prefix2 can be set to ‘None’.

### `renumber-windows` [`on` | `off`]

If on, when a window is closed in a session, automatically renumber the other windows in numerical order. This respects the base-index option if it has been set. If off, do not renumber the windows.

### repeat-time time

Allow multiple commands to be entered without pressing the prefix-key again in the specified time milliseconds (the default is 500). Whether a key repeats may be set when it is bound using the -r flag to bind-key. Repeat is enabled for the default keys bound to the resize-pane command.

### set-titles [on | off]

Attempt to set the client terminal title using the tsl and fsl terminfo(5) entries if they exist. tmux automatically sets these to the \e]0;...\007 sequence if the terminal appears to be xterm(1). This option is off by default.

### set-titles-string string

String used to set the window title if set-titles is on. Formats are expanded, see the FORMATS section.

### silence-action [any | none | current | other]

Set action on window silence when monitor-silence is on. The values are the same as those for activity-action.

### status [on | off]

Show or hide the status line.

### status-interval interval

Update the status line every interval seconds. By default, updates will occur every 15 seconds. A setting of zero disables redrawing at interval.

### status-justify [left | centre | right]

Set the position of the window list component of the status line: left, centre or right justified.

### status-keys [vi | emacs]

Use vi or emacs-style key bindings in the status line, for example at the command prompt. The default is emacs, unless the VISUAL or EDITOR environment variables are set and contain the string ‘vi’.

### status-left string

Display string (by default the session name) to the left of the status line. string will be passed through strftime(3) and formats (see FORMATS) will be expanded. It may also contain the special character sequence #[] to change the colour or attributes, for example ‘#[fg=red,bright]’ to set a bright red foreground. See the message-command-style option for a description of colours and attributes.
For details on how the names and titles can be set see the NAMES AND TITLES section.

Examples are:

~~~bash
#(sysctl vm.loadavg)
#[fg=yellow,bold]#(apm -l)%%#[default] [#S]
~~~

The default is ‘[#S] ’.

### status-left-length length

Set the maximum length of the left component of the status line. The default is 10.

### status-left-style style

Set the style of the left part of the status line. For how to specify style, see the message-command-style option.

### status-position [top | bottom]

Set the position of the status line.

### status-right string

Display string to the right of the status line. By default, the current pane title in double quotes, the date and the time are shown. As with status-left, string will be passed to strftime(3) and character pairs are replaced.
status-right-length length
Set the maximum length of the right component of the status line. The default is 40.

### status-right-style style

Set the style of the right part of the status line. For how to specify style, see the message-command-style option.

### status-style style

Set status line style. For how to specify style, see the message-command-style option.

### update-environment[] variable

Set list of environment variables to be copied into the session environment when a new session is created or an existing session is attached. Any variables that do not exist in the source environment are set to be removed from the session environment (as if -r was given to the set-environment command).

### user-keys[] key

Set list of user-defined key escape sequences. Each item is associated with a key named ‘User0’, ‘User1’, and so on.
For example:

~~~bash
set -s user-keys[0] "\e[5;30012~"
bind User0 resize-pane -L 3
~~~

### visual-activity [on | off | both]

If on, display a message instead of sending a bell when activity occurs in a window for which the monitor-activity window option is enabled. If set to both, a bell and a message are produced.

### visual-bell [on | off | both]

If on, a message is shown on a bell in a window for which the monitor-bell window option is enabled instead of it being passed through to the terminal (which normally makes a sound). If set to both, a bell and a message are produced. Also see the bell-action option.

### visual-silence [on | off | both]

If monitor-silence is enabled, prints a message after the interval has expired on a given window instead of sending a bell. If set to both, a bell and a message are produced.

### word-separators string

Sets the session's conception of what characters are considered word separators, for the purposes of the next and previous word commands in copy mode. The default is ‘ -_@’.