## パスワードの保存

- [Git push: username, password, how to avoid?](http://stackoverflow.com/questions/8588768/git-push-username-password-how-to-avoid)

~~~
$ git config credential.helper store
$ git push https://github.com/repo.git

Username for 'https://github.com': <USERNAME>
Password for 'https://USERNAME@github.com': <PASSWORD>
~~~


## ユーザー指定

~~~bash
$ git config --global user.name hdknr
$ git config --global user.email gmail@hdknr.com
$ git remote set-url origin https://hdknr@github.com/hdknr/bin.git
~~~



## error: The requested URL returned error: 403 Forbidden while accessing

- エラー

~~~bash
$ git push
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/hdknr/bin.git/info/refs
fatal: HTTP request failed
~~~

~~~bash
$ export GIT_SSL_NO_VERIFY=true  
~~~
