## 変数(vars)

- 変数の参照

~~~
$var
${var}
{{ var }}
~~~

## git モジュール

- [git - Deploy software (or files) from git checkouts](http://docs.ansible.com/git_module.html)


## いろいろ

- ホストを絞る [Safely limiting Ansible playbooks to a single machine?](https://stackoverflow.com/questions/18195142/safely-limiting-ansible-playbooks-to-a-single-machine)

	- `--limit servers[0]` を使う
	- `--extra-vars "target=server1"` を使う
	- ` -i "imac1-local,"` をつかう(カンマ注意)