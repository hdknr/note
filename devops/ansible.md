## Ansible Install

~~~
(sandbox)Peeko:js1 hide$ pip install -U ansible
~~~

~~~
Requirement already up-to-date: ansible in /Users/hide/ve/sandbox/lib/python2.7/site-packages
Requirement already up-to-date: paramiko in /Users/hide/ve/sandbox/lib/python2.7/site-packages (from ansible)
Downloading/unpacking jinja2 from https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.7.3.tar.gz#md5=b9dffd2f3b43d673802fe857c8445b1a (from ansible)
  Running setup.py egg_info for package jinja2

    warning: no files found matching '*' under directory 'custom_fixers'
    warning: no previously-included files matching '*' found under directory 'docs/_build'
    warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
Requirement already up-to-date: PyYAML in /Users/hide/ve/sandbox/lib/python2.7/site-packages (from ansible)
Downloading/unpacking setuptools from https://pypi.python.org/packages/source/s/setuptools/setuptools-7.0.tar.gz#md5=6245d6752e2ef803c365f560f7f2f940 (from ansible)
  Running setup.py egg_info for package setuptools

Requirement already up-to-date: pycrypto>=2.6 in /Users/hide/ve/sandbox/lib/python2.7/site-packages (from ansible)
Requirement already up-to-date: ecdsa>=0.11 in /Users/hide/ve/sandbox/lib/python2.7/site-packages (from paramiko->ansible)
Downloading/unpacking markupsafe (from jinja2->ansible)
  Downloading MarkupSafe-0.23.tar.gz
  Running setup.py egg_info for package markupsafe

Installing collected packages: jinja2, setuptools, markupsafe
  Found existing installation: Jinja2 2.6
    Uninstalling Jinja2:
      Successfully uninstalled Jinja2
  Running setup.py install for jinja2

    warning: no files found matching '*' under directory 'custom_fixers'
    warning: no previously-included files matching '*' found under directory 'docs/_build'
    warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyc' found under directory 'docs'
    warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
    warning: no previously-included files matching '*.pyo' found under directory 'docs'
  Found existing installation: setuptools 0.6c11
    Uninstalling setuptools:
      Successfully uninstalled setuptools
  Running setup.py install for setuptools

    Installing easy_install script to /Users/hide/ve/sandbox/bin
    Installing easy_install-2.7 script to /Users/hide/ve/sandbox/bin
  Running setup.py install for markupsafe

    building 'markupsafe._speedups' extension
    cc -fno-strict-aliasing -fno-common -dynamic -arch x86_64 -arch i386 -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -fwrapv -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch x86_64 -arch i386 -pipe -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c markupsafe/_speedups.c -o build/temp.macosx-10.9-intel-2.7/markupsafe/_speedups.o
    cc -bundle -undefined dynamic_lookup -arch x86_64 -arch i386 -Wl,-F. build/temp.macosx-10.9-intel-2.7/markupsafe/_speedups.o -o build/lib.macosx-10.9-intel-2.7/markupsafe/_speedups.so
Successfully installed jinja2 setuptools markupsafe
Cleaning up...
~~~

~~~
(sandbox)Peeko:js1 hide$ ansible --version
ansible 1.7.2
~~~


## config

### ~/.ssh/config

~~~
Peeko:devops hide$ vi ~/.ssh/config
~~~

~~~
Host 192.168.56.*
IdentityFile ~/.vagrant.d/insecure_private_key
User vagrant
~~~

### host

- [インベントリーファイル](http://docs.ansible.com/intro_inventory.html)に指定

~~~
(sandbox)Peeko:js1 hide$ vi hosts
~~~
~~~
[servers]
192.168.56.50
~~~

### test

- "-i" でインベントリファイルを指定"

~~~
  -i INVENTORY, --inventory-file=INVENTORY
                        specify inventory host file
                        (default=/etc/ansible/hosts)
~~~                         

- "-m" でモジュールを指定

~~~
  -m MODULE_NAME, --module-name=MODULE_NAME
                        module name to execute (default=command)
~~~

- "-vvv" verbose

~~~
  -v, --verbose         verbose mode (-vvv for more, -vvvv to enable
                        connection debugging)
~~~

### ping モジュール ( -m ping)
~~~
(sandbox)Peeko:js1 hide$ ansible -i hosts servers -m ping -vvvv
~~~

~~~
<192.168.56.50> ESTABLISH CONNECTION FOR USER: hide
<192.168.56.50> REMOTE_MODULE ping
<192.168.56.50> EXEC ['ssh',
    '-C', '-tt', '-vvv',
    '-o', 'ControlMaster=auto',
    '-o', 'ControlPersist=60s',
    '-o', 'ControlPath=/Users/hide/.ansible/cp/ansible-ssh-%h-%p-%r',
    '-o', 'KbdInteractiveAuthentication=no',
    '-o', 'PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey',
    '-o', 'PasswordAuthentication=no',
    '-o', 'ConnectTimeout=10',
    '192.168.56.50',
    "/bin/sh -c 'mkdir -p $HOME/.ansible/tmp/ansible-tmp-1414379666.02-135744012751990 && chmod a+rx $HOME/.ansible/tmp/ansible-tmp-1414379666.02-135744012751990 && echo $HOME/.ansible/tmp/ansible-tmp-1414379666.02-135744012751990'"]

<192.168.56.50> PUT /var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/tmpVp04VR TO /home/vagrant/.ansible/tmp/ansible-tmp-1414379666.02-135744012751990/ping

<192.168.56.50> EXEC ['ssh',
    '-C', '-tt', '-vvv',
    '-o', 'ControlMaster=auto',
    '-o', 'ControlPersist=60s',
    '-o', 'ControlPath=/Users/hide/.ansible/cp/ansible-ssh-%h-%p-%r',
    '-o', 'KbdInteractiveAuthentication=no',
    '-o', 'PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey',
    '-o', 'PasswordAuthentication=no',
    '-o', 'ConnectTimeout=10',
    '192.168.56.50',
    u"/bin/sh -c 'LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8 /usr/bin/python /home/vagrant/.ansible/tmp/ansible-tmp-1414379666.02-135744012751990/ping; rm -rf /home/vagrant/.ansible/tmp/ansible-tmp-1414379666.02-135744012751990/ >/dev/null 2>&1'"]
~~~
~~~    
192.168.56.50 | success >> {
    "changed": false,
    "ping": "pong"
}
~~~

### 任意のコマンド(-m command)

- "-m command" : -m を指定しないとデフォルトで "command" と見なされます
- "-a" : コマンドの引数

~~~
  -a MODULE_ARGS, --args=MODULE_ARGS
                        module arguments
~~~

~~~
(sandbox)Peeko:js1 hide$ ansible -i hosts servers -a 'uname -a' -vvvv
~~~

~~~
<192.168.56.50> ESTABLISH CONNECTION FOR USER: hide
<192.168.56.50> REMOTE_MODULE command uname -a
~~~
~~~
<192.168.56.50> EXEC ['ssh', '-C',     '-tt',     '-vvv',
    '-o', 'ControlMaster=auto',
    '-o', 'ControlPersist=60s',
    '-o', 'ControlPath=/Users/hide/.ansible/cp/ansible-ssh-%h-%p-%r',
    '-o', 'KbdInteractiveAuthentication=no',
    '-o', 'PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey',
    '-o', 'PasswordAuthentication=no',
    '-o', 'ConnectTimeout=10',
    '192.168.56.50',
    "/bin/sh -c
        'mkdir -p $HOME/.ansible/tmp/ansible-tmp-1414380394.67-216295138135478 &&
        chmod a+rx $HOME/.ansible/tmp/ansible-tmp-1414380394.67-216295138135478 &&
        echo $HOME/.ansible/tmp/ansible-tmp-1414380394.67-216295138135478'"]
~~~
~~~        
<192.168.56.50> PUT
    /var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/tmpNRuSIM TO
    /home/vagrant/.ansible/tmp/ansible-tmp-1414380394.67-216295138135478/command
~~~
~~~    
<192.168.56.50> EXEC ['ssh', '-C', '-tt', '-vvv',
    '-o', 'ControlMaster=auto',
    '-o', 'ControlPersist=60s',
    '-o', 'ControlPath=/Users/hide/.ansible/cp/ansible-ssh-%h-%p-%r',
    '-o', 'KbdInteractiveAuthentication=no',
    '-o', 'PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey',
    '-o', 'PasswordAuthentication=no',
    '-o', 'ConnectTimeout=10',
    '192.168.56.50',
    u"/bin/sh -c 'LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8
        /usr/bin/python /home/vagrant/.ansible/tmp/ansible-tmp-1414380394.67-216295138135478/command;
        rm -rf /home/vagrant/.ansible/tmp/ansible-tmp-1414380394.67-216295138135478/ >/dev/null 2>&1'"]
~~~
~~~        
192.168.56.50 | success | rc=0 >>
Linux js1 3.14-2-amd64 #1 SMP Debian 3.14.13-2 (2014-07-24) x86_64 GNU/Linux
~~~

## playbook

### apt

- [apt - Manages apt-packages](http://docs.ansible.com/apt_module.html#examples)

~~~
(sandbox)Peeko:js1 hide$ vi apt.yml
~~~

~~~
- hosts: servers
  sudo: true
  user: vagrant
  tasks:
    - apt: update_cache=yes state=latest
~~~

~~~
(sandbox)Peeko:js1 hide$ ansible-playbook apt.yml  -i hosts
~~~

~~~
PLAY [servers] ****************************************************************

GATHERING FACTS ***************************************************************
ok: [192.168.56.50]

TASK: [apt update_cache=yes state=latest] *************************************
ok: [192.168.56.50]

PLAY RECAP ********************************************************************
192.168.56.50              : ok=2    changed=0    unreachable=0    failed=0   
~~~

- 確認

~~~
root@js1:~# apt-get update
Hit http://security.debian.org jessie/updates InRelease                 
Hit http://security.debian.org jessie/updates/main Sources              
Hit http://security.debian.org jessie/updates/contrib Sources
Hit http://security.debian.org jessie/updates/non-free Sources              
Hit http://security.debian.org jessie/updates/main amd64 Packages           
Hit http://ftp.uk.debian.org jessie InRelease  
Hit http://security.debian.org jessie/updates/contrib amd64 Packages   
Hit http://security.debian.org jessie/updates/non-free amd64 Packages  
Hit http://ftp.uk.debian.org jessie-updates InRelease
Hit http://security.debian.org jessie/updates/contrib Translation-en   
Hit http://security.debian.org jessie/updates/main Translation-en
Hit http://ftp.uk.debian.org jessie-backports InRelease
Hit http://security.debian.org jessie/updates/non-free Translation-en  
Hit http://ftp.uk.debian.org jessie/main Sources/DiffIndex
Hit http://ftp.uk.debian.org jessie/contrib Sources/DiffIndex
Hit http://ftp.uk.debian.org jessie/non-free Sources/DiffIndex
Hit http://ftp.uk.debian.org jessie/main amd64 Packages/DiffIndex
Hit http://ftp.uk.debian.org jessie/contrib amd64 Packages/DiffIndex
Hit http://ftp.uk.debian.org jessie/non-free amd64 Packages/DiffIndex
Hit http://ftp.uk.debian.org jessie/contrib Translation-en/DiffIndex
Hit http://ftp.uk.debian.org jessie/main Translation-en/DiffIndex
Hit http://ftp.uk.debian.org jessie/non-free Translation-en/DiffIndex
Hit http://ftp.uk.debian.org jessie-updates/main Sources
Hit http://ftp.uk.debian.org jessie-updates/contrib Sources
Hit http://ftp.uk.debian.org jessie-updates/non-free Sources
Hit http://ftp.uk.debian.org jessie-updates/main amd64 Packages
Hit http://ftp.uk.debian.org jessie-updates/contrib amd64 Packages
Hit http://ftp.uk.debian.org jessie-updates/non-free amd64 Packages
Hit http://ftp.uk.debian.org jessie-updates/contrib Translation-en
Hit http://ftp.uk.debian.org jessie-updates/main Translation-en
Hit http://ftp.uk.debian.org jessie-updates/non-free Translation-en
Hit http://ftp.uk.debian.org jessie-backports/main Sources
Hit http://ftp.uk.debian.org jessie-backports/contrib Sources
Hit http://ftp.uk.debian.org jessie-backports/non-free Sources
Hit http://ftp.uk.debian.org jessie-backports/main amd64 Packages
Hit http://ftp.uk.debian.org jessie-backports/contrib amd64 Packages
Hit http://ftp.uk.debian.org jessie-backports/non-free amd64 Packages
Hit http://ftp.uk.debian.org jessie-backports/contrib Translation-en
Hit http://ftp.uk.debian.org jessie-backports/main Translation-en
Hit http://ftp.uk.debian.org jessie-backports/non-free Translation-en
Reading package lists... Done
~~~

- upgradeまでやってみた

~~~
- hosts: servers
  sudo: true
  user: vagrant
  tasks:
    - apt: update_cache=yes state=latest
    - apt: upgrade=yes state=latest

~~~

- ログ (/var/log/apt/term.log , /var/log/apt/history.log)

~~~
root@js1:/var/log# tail /var/log/apt/term.log

Log started: 2014-10-27  03:59:11
Log ended: 2014-10-27  04:01:25
~~~

## プラクティス

- 対象作業ごとにフォルダーを作る(Vagrantと同様)
- ansible.cfg を用意する
- ssh_connectionで、 ssh.configファイルを参照するようにする
- インベントリファイル(hostfile)には、ssh.configのHost名を指定する

### 例

#### ansible.cfg

- ssh.confファイルに接続情報を書く

~~~
[ssh_connection]
ssh_args = -F ssh.conf

[defaults]
hostfile = hosts
~~~

#### hosts

- サーバー名は ssh.conf のHostエントリ

~~~
[server]
default
~~~


#### ssh.conf

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

#### 実行

~~~
$ ansible default -a "uptime"
default | success | rc=0 >>
 00:31:13 up 10 days, 22:50,  4 users,  load average: 0.03, 0.03, 0.05
~~~

~~~
$ ssh -F ssh.conf default uptime
 00:32:06 up 10 days, 22:51,  3 users,  load average: 0.01, 0.02, 0.05
~~~

- リモートログイン

~~~
$ ssh -F ssh.conf default

Linux wzy 3.2.0-4-amd64 #1 SMP Debian 3.2.63-2+deb7u2 x86_64
....
Last login: Sun Feb  1 00:31:51 2015 from mac
hdknr@wzy:~$
~~~

## メモ
- [Ansible Tutorial](https://yteraoka.github.io/ansible-tutorial/#simple-playbook)
- [入門Ansible(未発表箇所)](http://www.slideshare.net/takushimizu/ansible-28951674)
- [DevOps Technologies: Fabric or Ansible](https://insights.sei.cmu.edu/devops/2015/03/devops-technologies-fabric-or-ansible.html)
