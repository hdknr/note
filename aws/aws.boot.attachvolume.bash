#!/bin/bash
# sudo apt-get install jq -y
# pip install awscli
# aws configure   # (key, secret, and default region)
#
# Copy this and paste at User-Data to Instance wizard.
# https://raw.githubusercontent.com/hdknr/scriptogr.am/master/aws/aws.user-data.mount-volume.png

AWSCLI=/usr/local/bin/aws
STORAGE=ApplicationStorage
DEVICE=/dev/sdf
VOLUME=/dev/xvdf1
MOUNTPOINT=/vagrant

export INSTANCE_ID=`wget -q -O - http://169.254.169.254/latest/meta-data/instance-id`
export VOLID=$($AWSCLI ec2 describe-volumes --filters Name=tag-key,Values="Name" Name=tag-value,Values="$STORAGE" | jq '.[][0].VolumeId' -r)
$AWSCLI ec2 detach-volume --volume-id $VOLID --force
$AWSCLI ec2 wait volume-available	 --volume-ids $VOLID 
$AWSCLI ec2 attach-volume --volume-id $VOLID --instance-id $INSTANCE_ID --device $DEVICE
while [ ! -e $LOCALDEVICE ]; do
  echo "Waiting for disk to appear.."
  sleep 30
done
mount $VOLUME $MOUNTPOINT
#
