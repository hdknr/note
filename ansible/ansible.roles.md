## Role構造

~~~
site.yml
roles/
   myrole/
     tasks/
     defaults/
     vars/
     files/
     templates/
     meta/
     handlers/
~~~

### main.yml

- 書くディレクトリのmain.ymlが読み込まれます
- その他のファイルは main.yml から `include` される

### 1. tasks

- roleで実行されるtaskを定義します。 

main.yml例:

~~~yml
---
- name: git clone
  git: repo={{ repository }} dest={{ approot }} version={{ version }} accept_hostkey=yes
  become: false
  tags:
    - update

- name: collectstatic
  django_manage: command=collectstatic app_path={{ apppath }} virtualenv={{ venv }}
  tags:
    - update

- name: restart gunicorn app service
  become: true
  supervisorctl: name={{ appservice}} state=started
  tags:
    - restart
~~~

###  2. defaults 

- roleで利用される変数のデフォルト値を定義します。 
- varsとの違いは、group_varsなどで変数を上書きできる点です。


main.yml例:

~~~yml
---
repository: git@bitbucket.org:yourprofile/goodapp.git
appname: goodapp
approot: "/data/projects/{{ appname }}"
apppath: "{{ approot }}/web"
version: master
ve: gootdapp
venv: "{{ ansible_env.HOME }}/.anyenv/envs/pyenv/versions/{{ ve }}"
appservice: goodapp
~~~

### 3. vars

- rooleで利用される変数を定義します。 
- 基本的に環境毎に変わる固定値などを記述し、group_varsなどで変数を上書きできません（厳密にはできるが、優先順位的にvarsはかなり強いため、扱い難い）。


### 4. files

- copyモジュールでセットアップされるファイルを配置します。 
- テキストファイルでもバイナリファイルでも構いません。 
- シェルスクリプトのようなテキストファイルは後述のtemplatesに配置する方がよい


### 5. templates

- templateモジュールでセットアップされるJinja2形式のテキストファイルを配置します。 
- Jinja2形式のテキストファイルは、変数を埋め込むことができる点がfilesの下のファイルとの違いです。 



### 6. meta

- Roleのメタ情報を配置します。 Roleの依存関係を記述することになります。 
- このRoleを実行するには依存するミドルウェアをインストールする別のRoleが必要、といったイメージです。



### 7. handlers

- `notify` で発火されたイベントに対してタスクを実行します

例:

~~~yaml
---
- hosts: all
  connection: local
  sudo: True
  tasks:
    - name: install httpd
      yum: name=httpd
      notify: restart httpd

  handlers:
    - name: restart httpd
      service: name=httpd state=restarted
~~~