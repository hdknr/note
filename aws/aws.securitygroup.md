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
