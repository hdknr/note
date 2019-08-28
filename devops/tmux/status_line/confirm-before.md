# `confirm-before`: 確認プロンプト

    confirm-before [-p prompt] [-t target-client] command
    (alias: confirm)

Ask for confirmation before executing command.  If -p is given,
prompt is the prompt to display; otherwise a prompt is con‐
structed from command.  It may contain the special character
sequences supported by the status-left option.

This command works only from inside tmux.
