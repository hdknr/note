## メタデータ

- [インスタンスメタデータとユーザーデータ](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

- 取得

~~~bash
$ curl http://instance-data/latest/meta-data/
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
instance-action
instance-id
instance-type
kernel-id
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
~~~

- インスタンスID

~~~bash
$ export INSTANCE_ID=`wget -q -O - http://instance-data/latest/meta-data/instance-id`

$ echo $INSTANCE_ID
i-2510c1aa
~~~

~~~bash
$ export INSTANCE_ID=`curl -s http://instance-data/latest/meta-data/instance-id`
.
~~~
