## Sphinxのドキュメントビルド

~~~yml
---
- hosts: staging
  tasks:
    - name: build docs
      command: /home/system/projects/mysite/bin/docbuild.bash
~~~      

- 実行されるスクリプト

~~~bash
#!/bin/bash
export PATH="/home/system/.anyenv/bin:$PATH"
eval "$(anyenv init -)"
pyenv activate myenv
cd /home/system/projects/mysite/web/docs
make html
~~~
