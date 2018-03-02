## インスタンス起動時にEBSをアタッチしてマウントする

オートスケールの設定などで使う:

事前:

- EC2インスタンスとEBSのボリュームの `ゾーンがおなじであること` を確認
- `$STORAGE` として、 EBSのボリュームに `Name` を指定しておく
- jq, awscli コマンドをイストールしておく

スクリプト内容:

- 起動中のインスタンス番号(`$INSTANCE_ID`) を特定する
- `Name` =  `$STORAGE` の EBSを探す
- これを強制デタッチする(念のため)
- EBSボリュームが利用可能になるのを待つ
- EBSボリュームをアタッチして、`$LOCALDEVICE` が利用可能になるのを待つ
- `$LOCALDEVICE` を `$MOUNTPOINT` にまうんとする
- `mysql`, `supervisor` などを再起動する

~~~bash
#!/bin/bash
# apt-get install jq awscli -y
export AWS_ACCESS_KEY_ID=XKIXI54S3WB4DRBQZZ3Q
expost AWS_SECRET_ACCESS_KEY=8FiHueLf+AotpzITOEyqLhI+CTSB6ybML0y2sRo
export AWS_DEFAULT_REGION=ap-northeast-1
STORAGE=PersitantStorage
#
AWSCLI=/usr/bin/aws
MOUNTPOINT=/data
LOCALDEVICE=/dev/xvdf1
DEVICE=/dev/sdf
#
export INSTANCE_ID=`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`
export VOLID=$($AWSCLI ec2 describe-volumes --filters Name=tag-key,Values="Name" Name=tag-value,Values="$STORAGE" | jq '.[][0].VolumeId' -r)
$AWSCLI ec2 detach-volume --volume-id $VOLID --force
$AWSCLI ec2 wait volume-available    --volume-ids $VOLID
$AWSCLI ec2 attach-volume --volume-id $VOLID --instance-id $INSTANCE_ID --device $DEVICE
while [ ! -e $LOCALDEVICE ]; do
  echo "Waiting for disk to appear.."
  sleep 30
done
#
mount $LOCALDEVICE $MOUNTPOINT      
sudo service mysql start
sudo supervisorctl reload
~~~


## アタッチできない

- インスタンスのゾーンとEBSのゾーンがことなる

オートスケールから起動:

- サブネット のゾーンは マウントする EBS と同じものを `１つだけ` チョイスする
