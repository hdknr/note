# tr (translate characters)

## `-d` 文字削除

~~~bash
$ cat ec2-instance.json | jq -r ".[] |[.InstanceId, .Tags[0].Value, .NetworkInterfaces[0].Association.PublicIp, .ImageId] | @csv" | tr -d '\"'       
~~~

[sed](../s/sed/README.md):

~~~bash
... | sed s/\"//g 
~~~


## 関連

- [cut](../c/cut.md)