#!/bin/bash
# sudo apt-get install jq python-pip tree -y
# sudo pip install awscli

JQ_COMMAND=jq
EBS_NAME=AppDisk

attach_volume_and_wait() {
    local  volumeid="$1" instanceid="$2" device="$3"

    aws ec2 attach-volume  --volume-id $volumeid --instance-id $instanceid --device $device

    while true; do
        status=$(aws ec2 describe-volumes --volume-ids ${volumeid}  | \
            ${JQ_COMMAND} '.Volumes[].Attachments[].State' )

        echo ${volumeid}:${status}
        case "$status" in
            *attached* ) break;;
        esac
        sleep 10
    done
    echo ${volumeid}:"attached"
}

mount_device(){
    local device="$1"  point="$2"
    mkdir -p $1

    # fstab
    if grep -q $1 /etc/fstab; then
       echo already found
    else
        cat >>/etc/fstab <<EOF
$device $point ext4 defaults 1 1
EOF
    fi
    mount -a
    echo "mounted"
}

wait_instance(){
    # Booting Insntace ID
    export INSTANCE_ID=$(wget -q -O - http://169.254.169.254/latest/meta-data/instance-id)

    # Wait 
    aws ec2 wait instance-running --instance-ids $INSTANCE_ID
}

find_volume(){
    local volume_name="$1"
    export VOLUME_ID=$(aws ec2 describe-volumes --filters \
        Name=tag-key,Values="Name" \
        Name=tag-value,Values="$volume_name" \
        Name=status,Values="available"  | jq ".Volumes[].VolumeId")

    export VOLUME_ID=$(eval "echo $VOLUME_ID")
}

######

# Zoneinfo
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

wait_instance
find_volume $EBS_NAME

if [ "$VOLUME_ID" == "" ]; then
    echo "No Available Volume"
    exit
fi

attach_volume_and_wait $VOLUME_ID $INSTANCE_ID /dev/sdf
mount_device /vagrant /dev/xvdf1
