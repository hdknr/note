
- [Setting the Environment (and Working With Proxies)](http://docs.ansible.com/ansible/playbooks_environment.html)
- [Variable](http://docs.ansible.com/ansible/playbooks_variables.html)


## 環境変数

~~~yaml
user: "{{ lookup('env', 'USER') }}"
homedir: "{{ lookup('env', 'HOME') }}"
~~~
