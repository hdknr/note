設定関連

# ansible.cfg

例:

~~~ini
[ssh_connection]
ssh_args = -F ssh.conf

[defaults]
hostfile = hosts.conf
~~~


# hosts.conf

## リモートサーバーのPythonのパスを指定(virtualenvなど)

~~~ini
[localhost]
127.0.0.1   ansible_python_interpreter=/Users/hide/.anyenv/envs/pyenv/versions/ansibleenv/bin/python

[aws]
test   ansible_python_interpreter=/home/system/.anyenv/envs/pyenv/versions/awsenv/bin/python
~~~
