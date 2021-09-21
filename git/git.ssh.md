# git ssh


## デプロイキーを指定する

~~~bash
$ export GIT_SSH_COMMAND='ssh -i /home/ubuntu/.ssh/yourkey.pem'
~~~

## config

~~~bash
$ git config core.sshCommand "ssh -i ~/.ssh/id_rsa -F /dev/null"
~~~