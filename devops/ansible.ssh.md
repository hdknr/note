OSX: Terminalを新規に開いてssh_config のサーバーにssh接続する

Ansibleというよりoascriptコマンドの話

# Ansible 設定
wzyというVirtualBoxにhkdnrで接続する環境。
Ansibleにssh_configを参照するように設定。
ssh_configは vagrant ssh-configで作って編集するとか。

- ansible.cfg

~~~
[ssh_connection]
ssh_args = -F ssh.conf

[defaults]
hostfile = hosts
~~~

- ssh.conf

~~~
Host default 
  HostName wzy
  User hdknr
  Port 22
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile ~/.ssh/id_rsa 
  IdentitiesOnly yes
  LogLevel FATAL
~~~

- hosts

~~~
[server]
default
~~~

# Termnalを開いてssh

-  oascript で AppleScript 経由でTerminalを開くbashの関数

~~~
function ANSIBLE_OPEN_SSH()
{
  PARAMS="$@"; [ -n "$PARAMS" ] || PARAMS="default";
  if [ -f ssh.conf ]; then
    SCRIPT="cd $PWD;ssh -F ssh.conf $PARAMS"; 
    AS="osascript -e 'tell application \"Terminal\" to do script \"$SCRIPT\"'";
    eval $AS;
  fi
}
~~~
