
# 変数

- [Setting the Environment (and Working With Proxies)](http://docs.ansible.com/ansible/playbooks_environment.html)
- [Variable](http://docs.ansible.com/ansible/playbooks_variables.html)
- [Ansibleのグローバルスコープの変数をどこに定義するか - Qiita](https://qiita.com/tentom/items/9816a5c07f013b84a6ce)
- [Ansible2 変数の優先度 - Qiita](https://qiita.com/KeijiYONEDA/items/721407cbe418b3d532ed)


## 環境変数

~~~yaml
user: "{{ lookup('env', 'USER') }}"
homedir: "{{ lookup('env', 'HOME') }}"
~~~
