# git ssh


## デプロイキーを指定する

~~~bash
$ export GIT_SSH_COMMAND='ssh -i /home/ubuntu/.ssh/yourkey.pem'
~~~

## config

~~~bash
$ git config core.sshCommand "ssh -i ~/.ssh/id_rsa -F /dev/null"
~~~


設定スクリプト:


~~~bash
#!/bin/bash

KEY=$1
FILE=$(basename $1)
DIR=.secrets
#
mkdir -p $DIR
cp $KEY $DIR/$FINE
#
cat > $DIR/ssh.conf << EOS
Host github.com
    HostName github.com
    Port 22
    User git
    IdentityFile .secrets/$FILE
EOS
#
git config core.sshCommand "ssh -F .secrets/ssh.conf"
~~~