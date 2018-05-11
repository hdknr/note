## awsコマンドプロファイル

~~~bash
$ aws configure --profile tact

AWS Access Key ID [None]: *********
AWS Secret Access Key [None]: **********
Default region name [None]: ap-northeast-1
Default output format [None]: json
~~~

## sshが許可されたネットワークの確認(`describe-security-groups`)

- `--group-ids` にセキュリティグループIDを指定する

~~~bash
$ aws --profile tact ec2 describe-security-groups --group-ids sg-4c841a3d | jq ".[][0].IpPermissions" | jq "map(select(.FromPort == 22))" | jq ".[].IpRanges[].CidrIp"

"110.233.95.31/32"
....
~~~

### スクリプト([aws.bash](https://github.com/hdknr/bin/blob/osx/env/aws.bash))

セキュリティグループは`Main` と言う名前のタグのセキュリティグループ:

~~~bash 
$ AWS_PROFILE=tact EC2_SECGROUP_ID Main
sg-4c841a5d
~~~

許可してssh.conf の `staging` サーバーへssh:

~~~bash 
$ source ~/bin/env/aws.bash
$ source ~/bin/env/ansible.bash
$ AWS_PROFILE=tact EC2_SSHIP_ALLOW sg-4c841a5d
$ ANSIBLE_OPEN_SSH staging
~~~

終わったら却下:

~~~bash
$ AWS_PROFILE=tact EC2_SSHIP_REVOKE sg-4c841a5d
~~~






## 記事

- [TravisCIなどでEC2のSSH元IPを動的に指定する方法](https://qiita.com/maru_cc/items/33f11b142a686e4b377a)
- [[AWS][CLI] EC2にSSHするときだけ、security groupに自分のアドレスを追加する](https://dev.classmethod.jp/etc/ssh_with_adding_ingress_rule/)