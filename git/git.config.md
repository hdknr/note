## パスワードの保存

- [Git push: username, password, how to avoid?](http://stackoverflow.com/questions/8588768/git-push-username-password-how-to-avoid)

~~~
$ git config credential.helper store
$ git push https://github.com/repo.git

Username for 'https://github.com': <USERNAME>
Password for 'https://USERNAME@github.com': <PASSWORD>
~~~
