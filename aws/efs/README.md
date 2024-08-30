# EFS

## E2 からマウント

```bash
#!/bin/bash
EFS_ID="fs-0f90bd97a364a6e94"
#
PKG=amazon-efs-utils
RES=$(dpkg --get-selections | grep $PKG)
MOUNT_PATH="/storage"

if [ -z "${RES}" ]; then
    # https://github.com/aws/efs-utils?tab=readme-ov-file#on-other-linux-distributions
    apt update && apt upgrade -y && apt autoremove -y
    apt-get -y install git binutils rustc cargo pkg-config libssl-dev
    git clone https://github.com/aws/efs-utils
    cd efs-utils
    ./build-deb.sh
    apt-get install -y ./build/amazon-efs-utils*deb
fi
#
if [ ! -d $MOUNT_PATH ]; then
    mkdir $MOUNT_PATH
fi
#
mount -t efs $EFS_ID:/ $MOUNT_PATH
```

## fstab

マウントヘルパーをつかって /storageに EFS(DNS名をIDとして指定)をマウント:

```txt
fs-0f80bd87a364a6e84.efs.ap-northeast-1.amazonaws.com:/ /storage  efs _netdev 0 0
```

`mount` コマンドで確認:

```bash
$ sudo mount -fav
/                        : ignored
swap                     : ignored
/storage is already mounted, please run 'mount' command to verify
/storage                 : successfully mounted
```

## 資料

- [Amazon Elastic File System とは](https://docs.aws.amazon.com/ja_jp/efs/latest/ug/whatisefs.html)
- [EFS マウントヘルパーを使用した Amazon EC2 Linux インスタンスをマウントする](https://docs.aws.amazon.com/ja_jp/efs/latest/ug/mounting-fs-mount-helper-ec2-linux.html)
- [Amazon EFS を作成し EC2 からマウントしてみた](https://engineers.weddingpark.co.jp/amazon-efs/)
- [AWS の Ubuntu の EC2 で EFS のマウント(amazon-efs-utils)](https://qiita.com/momomo_rimoto/items/16c2fb959bc36eba1f11)
