# ユーザー

## ユーザー追加

- [adduser](../../command/a/adduser.md) コマンドでユーザーを追加します。


## groupadd + useradd

~~~bash
USER=emailuser
ID=2000
PASSWORD=Ieth6cah
#
sudo groupadd -g $ID $USER
sudo useradd -g $USER -d /home/$USER -u $ID -m $USER -p $PASSWORD
~~~ 