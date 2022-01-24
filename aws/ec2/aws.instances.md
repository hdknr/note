# awscli


## インスタンスのIPアドレス取得

~~~bash
aws describe-instances --filters Name=tag:site-deploy,Values=prod \
    | jq ".Reservations[].Instances[]|[.PublicIpAddress, ((.Tags | from_entries) | .Name)]"
~~~ 


## インスタンスID一覧

ID:

~~~bash
$ aws ec2 describe-instances --profile ictact | jq '.Reservations[].Instances[].InstanceId'
.
~~~

名称(`KeyName`):`

~~~bash
$ aws ec2 describe-instances --profile spindd | jq -r ".Reservations[].Instances[] | [.KeyName, .State.Name] | @tsv"
.
~~~


~~~bash
$ aws ec2 describe-instances --profile ictact | jq ".Reservations[].Instances[]|[.InstanceId, .InstanceType, .VpcId, .ImageId, .PublicDnsName]" -c
["i-535b8adc","t1.micro","vpc-fbf6709e","ami-e54e648b","ec2-53-64-4-1.ap-northeast-1.compute.amazonaws.com"]
["i-60561cef","m3.xlarge","vpc-fbf6709e","ami-36d1dc58","ec2-54-64-244-35.ap-northeast-1.compute.amazonaws.com"]
~~~