# 設定関連

- [Configuring Ansible — Ansible Documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html#roles-path)
- [Ansible Configuration Settings — Ansible Documentation](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)
- [ansible.cfgの項目をリスト化してみた - Qiita](https://qiita.com/croissant1028/items/33f06298d7d05bf1e295)

## ansible.cfg

例:

~~~ini
[ssh_connection]
ssh_args = -F ssh.conf

[defaults]
hostfile = hosts.conf
~~~


## hosts.conf

### リモートサーバーのPythonのパスを指定(virtualenvなど)

~~~ini
[localhost]
127.0.0.1   ansible_python_interpreter=/Users/hide/.anyenv/envs/pyenv/versions/ansibleenv/bin/python

[aws]
test   ansible_python_interpreter=/home/system/.anyenv/envs/pyenv/versions/awsenv/bin/python
~~~
