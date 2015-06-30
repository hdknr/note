ssh: Djangoでパブリックキー管理してAuthorizedKeysCommandで呼び出す

- Debian Jessie でやってみた

# キーの確認をコマンドでやる

/etc/sshd/sshd_config:

```
PasswordAuthentication no

AuthorizedKeysCommand  /root/auth.bash
AuthorizedKeysCommandUser root
```

/root/auth.bash :

```
#!/bin/bash

LOG=/tmp/root.txt

date >> $LOG
echo $@ >> $LOG
cat `dirname $0`/auth.key
```

/root/auth.key にキーを登録するとログインできた:

```
vagrant@10:~$ ssh vagrant@localhost

You have new mail.
Last login: Thu Jan  8 06:16:50 2015 from ::1
```

vagrant にログイン要求が来てる:

```
root@10:/tmp# tail /tmp/root.txt 
Thu Jan  8 06:16:50 UTC 2015
vagrant
```

## ユーザを変えてみる

```
LogLevel ERROR

AuthorizedKeysCommand  /home/vagrant/projects/sshkey/auth.bash
AuthorizedKeysCommandUser vagrant

```

```
# tail -f /var/log/auth.log

Jan  8 06:32:39 10 sshd[20926]: 
error: Unsafe AuthorizedKeysCommand: 
bad ownership or modes for file /home/vagrant/projects/sshkey/auth.bash
```

```
vagrant@10:~/projects/sshkey$ ls -al
total 20
drwx------  3 vagrant vagrant 4096 Jan  8 06:27 .
drwxr-xr-x 10 vagrant vagrant 4096 Jan  8 04:54 ..
-rwx------  1 vagrant vagrant   90 Jan  8 06:22 auth.bash
-rw-------  1 vagrant vagrant  801 Jan  8 06:21 auth.key
```

- [ここ](https://lists.mindrot.org/pipermail/openssh-bugs/2013-April/012052.html)をみるとroot以外はエラーがでるっぽい。
- sshkey以下をroot所有に変えてAuthorizedKeysCommandUser=rootにすると、sshkeyの親ディレクトリで、`bad ownership` になる。
- おとなしくrootでやったほうがいいでしょう

# Djangoでキー管理

## keys アプリ

```
keys
├── admin.py
├── __init__.py
├── management
│   ├── commands
│   │   ├── __init__.py
│   │   └── sshkeys.py
│   └── __init__.py
├── migrations
│   ├── 0001_initial.py
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

##モデル

### Key

- ログインユーザーは自分の鍵のパブリックキーの管理をできるようにする

```py
from django.db import models
from django.contrib.auth.models import User

class Key(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    key = models.TextField()

    def __unicode__(self):
        return "{0} {1}".format(
            self.user and self.user.username or '',
            self.name or '',
        )

```

### Resource

- リソースの管理者(rootとか)はunix userでリソース登録
- 管理者はusersに許可するユーザーを登録
- keysにusersのキーが登録される
- デフォルトでUserのKeyを全て登録して、あとで、Userが自身のキーの登録削除をできるようにする

```py
class Resource(models.Model):
    name = models.CharField(max_length=100)
    unix_user = models.CharField(
        max_length=100,
        unique=True,
    )
    users = models.ManyToManyField(User, null=True, blank=True, default=None)
    keys = models.ManyToManyField(Key, null=True, blank=True, default=None)
```    

## コマンド: リソースのパブリックキーを返す

- sshkey authkeys $UNIX_USER に対応するパブリックキーを返す

```
from pycommand.command import Command as PyCommand, SubCommand
from django.core.management.base import BaseCommand

from keys.models import Key

class Command(BaseCommand, PyCommand):

    def run_from_argv(self, argv):
        return self.run(argv[1:])

    class AuthKeys(SubCommand):
        name = 'authkeys'
        args = [
            (('user', ), dict(nargs=1,)),
        ]

        def run(self, param, **options):
            for key in Key.objects.filter(resource__unix_user=param.user[0]):
                print key.key
```

## auth.bashからコマンドを呼ぶ

- openssh から呼ばれたら、djangoのコマンドで処理する

```
#!/bin/bash

PY=/home/vagrant/.pyenv/versions/wordpress/bin/python
DJ=/home/vagrant/projects/sshauth/web

$PY $DJ/manage.py sshkeys authkeys $1
```
