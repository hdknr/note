# インベントリ

- [Working with Inventory — Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#how-variables-are-merged)
- [初めてのAnsible（3章：インベントリ:サーバーの記述） - Qiita](https://qiita.com/c0tt0n-candy/items/1b109c53d8709717a1bb)

## inventories ディレクトリ

~~~bash
.
├── hosts
│   ├── debug
│   │   ├── group_vars
│   │   │   └── main.yml
│   │   ├── host_vars
│   │   │   └── main.yml
│   │   └── inventory.conf
│   └── live
│       ├── group_vars
│       │   └── main.yml
│       ├── host_vars
│       │   └── main.yml
│       └── inventory.conf
~~~

~~~bash
$ ansible-playbook -i inventoreis/debug book1.yml
.
~~~

hosts/debug/inventory.conf:

~~~conf
[targets]
debug01
debug02
~~~

book1.yml:

~~~yml
---
- hosts: targets
  roles:
    - apps
~~~