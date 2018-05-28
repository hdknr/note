## データディレクトリの移動

[MySQLのデータディレクトリを移動する](https://qiita.com/ShuM/items/1a960b4ef53f8a08dd5a)

/etc/mysql.conf.d/mysqld.cnf:

~~~
# datadir               = /var/lib/mysql
datadir               = /data/mysql
~~~

ディスクを `/data` にマウント:

~~~bash 
$ df

Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/xvda1      30428648 4463568  25948696  15% /
...
/dev/xvdf1      30831592 2153284  27089116   8% /data
~~~


自動起動させない:

- マウントスクリプトのあとで手動起動

~~~bash
$ systemctl list-unit-files -t service  | grep sql
mysql.service                              disabled
~~~

EBSをマウントするスクリプト:

~~~bash 
#!/bin/bash
AWSCLI=/usr/bin/aws
STORAGE=MYEXTERNALDISK
MOUNTPOINT=/data
LOCALDEVICE=/dev/xvdf1
DEVICE=/dev/sdf
EIP=eipalloc-f9999a3cf
export AWS_ACCESS_KEY_ID=AKI99999999999999
export AWS_SECRET_ACCESS_KEY=4321dsafdsafdsafafsfdsafdsaf
export AWS_DEFAULT_REGION=ap-northeast-1

export INSTANCE_ID=`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`
export VOLID=$($AWSCLI ec2 describe-volumes --filters Name=tag-key,Values="Name" Name=tag-value,Values="$STORAGE" | jq '.[][0].VolumeId' -r)

$AWSCLI ec2 associate-address --allocation-id $EIP --instance-id $INSTANCE_ID
$AWSCLI ec2 detach-volume --volume-id $VOLID --force
$AWSCLI ec2 wait volume-available    --volume-ids $VOLID
$AWSCLI ec2 attach-volume --volume-id $VOLID --instance-id $INSTANCE_ID --device $DEVICE

while [ ! -e $LOCALDEVICE ]; do
  echo "Waiting for disk to appear.."
  sleep 30
done

mount $LOCALDEVICE $MOUNTPOINT
sudo service mysql start
sudo supervisorctl reload
sudo service nginx restart
sudo swapon /swapfile
~~~