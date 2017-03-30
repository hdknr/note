- [ec2-create-image](http://docs.aws.amazon.com/AWSEC2/latest/CommandLineReference/ApiReference-cmd-CreateImage.html)


## 現在のインスタンス取得

~~~bash
$ export INSTANCE_ID=`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`
~~~

- `ec2metadata` コマンド

~~~bash
$ ec2metadata --instance-id
~~~

- `boto`

~~~py
from boto import utils
iid = utils.get_instance_metadata()['instance-id']
~~~
