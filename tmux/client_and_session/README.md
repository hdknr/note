# CLIENT AND SESSIONS

The tmux server manages clients, sessions, windows and panes. Clients
are attached to sessions to interact with them, either when they are
created with the new-session command, or later with the attach-session
command. Each session has one or more windows linked into it. Windows
may be linked to multiple sessions and are made up of one or more
panes, each of which contains a pseudo terminal. Commands for creat‐
ing, linking and otherwise manipulating windows are covered in the
WINDOWS AND PANES section.

The following commands are available to manage clients and sessions:

- [attach-session](attach-session.md) (`attach`)
- [detach-client](detach-client.md)(`detach`)
- has-session
- kill-server
- list-commands
- list-sessions
- lock-client
- lock-session
- new-session
- refresh-client
- [rename-session](rename-session.md)
- show-messages
- source-file
- start-server
- suspend-client
- switch-client
