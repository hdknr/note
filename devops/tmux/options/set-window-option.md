# set-window-option (alias: setw)

~~~bash
set-window-option [-aFgoqu] [-t target-window] option value
~~~

Set a window option. The -a, -F, -g, -o, -q and -u flags work similarly to the set-option command.
Supported window options are:

aggressive-resize [on | off]
Aggressively resize the chosen window. This means that tmux will resize the window to the size of the smallest session for which it is the current window, rather than the smallest session to which it is attached. The window may resize when the current window is changed on another sessions; this option is good for full-screen programs which support SIGWINCH and poor for interactive programs such as shells.
allow-rename [on | off]
Allow programs to change the window name using a terminal escape sequence (\ek...\e\\). The default is off.
alternate-screen [on | off]
This option configures whether programs running inside tmux may use the terminal alternate screen feature, which allows the smcup and rmcup terminfo(5) capabilities. The alternate screen feature preserves the contents of the window when an interactive application starts and restores it on exit, so that any output visible before the application starts reappears unchanged after it exits. The default is on.
automatic-rename [on | off]
Control automatic window renaming. When this setting is enabled, tmux will rename the window automatically using the format specified by automatic-rename-format. This flag is automatically disabled for an individual window when a name is specified at creation with new-window or new-session, or later with rename-window, or with a terminal escape sequence. It may be switched off globally with:
set-window-option -g automatic-rename off
        
automatic-rename-format format
The format (see FORMATS) used when the automatic-rename option is enabled.
clock-mode-colour colour
Set clock colour.
clock-mode-style [12 | 24]
Set clock hour format.
force-height height
 
force-width width
Prevent tmux from resizing a window to greater than width or height. A value of zero restores the default unlimited setting.
main-pane-height height
 
main-pane-width width
Set the width or height of the main (left or top) pane in the main-horizontal or main-vertical layouts.
mode-keys [vi | emacs]
Use vi or emacs-style key bindings in copy mode. The default is emacs, unless VISUAL or EDITOR contains ‘vi’.
mode-style style
Set window modes style. For how to specify style, see the message-command-style option.
monitor-activity [on | off]
Monitor for activity in the window. Windows with activity are highlighted in the status line.
monitor-bell [on | off]
Monitor for a bell in the window. Windows with a bell are highlighted in the status line.
monitor-silence [interval]
Monitor for silence (no activity) in the window within interval seconds. Windows that have been silent for the interval are highlighted in the status line. An interval of zero disables the monitoring.
other-pane-height height
Set the height of the other panes (not the main pane) in the main-horizontal layout. If this option is set to 0 (the default), it will have no effect. If both the main-pane-height and other-pane-height options are set, the main pane will grow taller to make the other panes the specified height, but will never shrink to do so.
other-pane-width width
Like other-pane-height, but set the width of other panes in the main-vertical layout.
pane-active-border-style style
Set the pane border style for the currently active pane. For how to specify style, see the message-command-style option. Attributes are ignored.
pane-base-index index
Like base-index, but set the starting index for pane numbers.
pane-border-format format
Set the text shown in pane border status lines.
pane-border-status [off | top | bottom]
Turn pane border status lines off or set their position.
pane-border-style style
Set the pane border style for panes aside from the active pane. For how to specify style, see the message-command-style option. Attributes are ignored.
remain-on-exit [on | off]
A window with this flag set is not destroyed when the program running in it exits. The window may be reactivated with the respawn-window command.
synchronize-panes [on | off]
Duplicate input to any pane to all other panes in the same window (only for panes that are not in any special mode).
window-active-style style
Set the style for the window's active pane. For how to specify style, see the message-command-style option.
window-status-activity-style style
Set status line style for windows with an activity alert. For how to specify style, see the message-command-style option.
window-status-bell-style style
Set status line style for windows with a bell alert. For how to specify style, see the message-command-style option.
window-status-current-format string
Like window-status-format, but is the format used when the window is the current window.
window-status-current-style style
Set status line style for the currently active window. For how to specify style, see the message-command-style option.
window-status-format string
Set the format in which the window is displayed in the status line window list. See the status-left option for details of special character sequences available. The default is ‘#I:#W#F’.
window-status-last-style style
Set status line style for the last active window. For how to specify style, see the message-command-style option.
window-status-separator string
Sets the separator drawn between windows in the status line. The default is a single space character.
window-status-style style
Set status line style for a single window. For how to specify style, see the message-command-style option.
window-style style
Set the default window style. For how to specify style, see the message-command-style option.
wrap-search [on | off]
If this option is set, searches will wrap around the end of the pane contents. The default is on.
xterm-keys [on | off]
If this option is set, tmux will generate xterm(1) -style function key sequences; these have a number included to indicate modifiers such as Shift, Alt or Ctrl.