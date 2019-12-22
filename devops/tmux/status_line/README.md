# STATUS LINE

tmux includes an optional status line which is displayed in the bottom line of each terminal.

By default, 
the status line is enabled and one line in height (it may be disabled or made multiple lines with the status session option) 
and contains, from left-to-right: 
the name of the current session in square brackets; 
the window list; 
the title of the active pane in double quotes; 
and the time and date.

Each line of the status line is configured with the status-format option.  
The default is made of three parts: 
configurable left and right sections 
(which may contain dynamic content such as the time or output from a shell command, see the status-left, status-left-length, status-right, and status-right-length options below), 
and a central window list.  

By default, 
the window list shows the index, name and (if any) flag of the windows present in the current session in ascending numerical order.  
It may be customised with the window-status-format and window-status-current-format options.  
The flag is one of the following symbols appended to the window name:

    Symbol    Meaning
    *         Denotes the current window.
    -         Marks the last window (previously selected).
    #         Window activity is monitored and activity has been
                        detected.
    !         Window bells are monitored and a bell has occurred in
                        the window.
    ~         The window has been silent for the monitor-silence
                        interval.
    M         The window contains the marked pane.
    Z         The window's active pane is zoomed.

The `#` symbol relates to the monitor-activity window option.  
The window name is printed in inverted colours if an alert 
(bell, activity or silence) is present.

The colour and attributes of the status line may be configured, 
the entire status line using the status-style session option and individual windows using the window-status-style window option.

The status line is automatically refreshed at interval 
if it has changed, 
the interval may be controlled with the status-interval session option.

## コマンド

Commands related to the status line are as follows:

- command-prompt
- [confirm-before](confirm-before.md): 確認プロンプト
- display-menu
- display-message
