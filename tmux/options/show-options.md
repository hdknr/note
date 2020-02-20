# show-options (alias: show)

~~~bash
show-options [-gqsvw] [-t target-session | target-window] [option]
~~~

Show the window options (or a single window option if given) with -w (equivalent to show-window-options), the server options with -s, otherwise the session options for target session. Global session or window options are listed if -g is used. -v shows only the option value, not the name. If -q is set, no error will be returned if option is unset.