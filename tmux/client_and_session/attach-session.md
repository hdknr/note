# attach-session (alias: attach)

~~~
attach-session [-dEr] [-c working-directory] [-t target-session]
~~~

If run from outside tmux, create a new client in the current terminal and attach it to target-session.  

If used from inside, switch the current client.  

If no server is started, attach-session will attempt to start it; 
this will fail unless sessions are created in the configuration file.

The target-session rules for attach-session are slightly adjusted: 
if tmux needs to select the most recently used session,
it will prefer the most recently used unattached session.

## `-d`

If -d is specified, any other clients attached to the session are detached.  

- [tmuxへのアタッチで画面サイズが合わない時は-d - Qiita](https://qiita.com/maueki/items/dec71193560955f15e5f)


## `-r`

-r signifies the client is read-only 
(only keys bound to the detach-client or switch-client commands have any effect)

## `-c`

-c will set the session working directory 
(used for new win‐ dows) to working-directory.


## `-E`

If -E is used, the update-environment option will not be applied.