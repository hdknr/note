# vagrant-aws

- https://github.com/mitchellh/vagrant-aws


- https://blog.logentries.com/2014/03/devops-vagrant-with-aws-ec2-digital-ocean/

- [Vagrant + Ansibleで複数のEC2インスタンスの起動、プロビジョニング](http://qiita.com/numa08/items/9946308ac0425c3ac270)
- [Vagrant + AWS + Ansible をやってみる](http://qiita.com/kiarina/items/052e977439c5a3693a67)

## 事前準備

- AWS IAM でグループ作成(vagrant)
- AWS IAM でユーザー作成(vagrant) + vagrantグループ追加 + キー&シークレット保存
- AWS ECS でセキュリティグループ(vagrant) + SSH/HTTP/HTTPS  (any)
- AWS Keypair でキーペア(vagrant) 作成   + ~/.ssh/vagrant.pem

## インストール

~~~bash
$ vagrant plugin install vagrant-aws

Installing the 'vagrant-aws' plugin. This can take a few minutes...
Installed the plugin 'vagrant-aws (0.6.0)'!
~~~

~~~bash
$ vagrant plugin install aws-sdk

Installing the 'aws-sdk' plugin. This can take a few minutes...
Installed the plugin 'aws-sdk (2.2.5)'!
~~~

~~~bash
$ vagrant plugin install dotenv
Installing the 'dotenv' plugin. This can take a few minutes...
Installed the plugin 'dotenv (2.0.2)'!
~~~
