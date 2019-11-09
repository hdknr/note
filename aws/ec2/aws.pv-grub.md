- [UserProvidedKernels](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/UserProvidedKernels.html)


## PV-GRUB

- 準仮想化（PV）を使用する Amazon マシンイメージ では、起動プロセスで PV-GRUB と呼ばれるシステムが利用されます。
- [準仮想化](https://ja.wikipedia.org/wiki/%E6%BA%96%E4%BB%AE%E6%83%B3%E5%8C%96)
- PV-GRUB は、パッチが適用されたバージョンの GNU GRUB 0.97 を実行する準仮想化ブートローダーです。
- インスタンスを起動すると、PV-GRUB では起動プロセスが開始され、お客様のイメージの menu.lst ファイルが指定するカーネルがチェーンロードされます。


- PV-GRUB は標準の grub.conf または menu.lst コマンドを認識します。
- これにより、現在サポートされているすべての Linux ディストリビューションとともに利用できます。
- Ubuntu 10.04 LTS、Oracle Enterprise Linux、CentOS 5.x など、古いディストリビューションでは特別な「ec2」や「xen」カーネルパッケージが必要です。
- 新しいディストリビューションでは、デフォルトのカーネルパッケージに必要なドライバが含まれています。

- 最新の準仮想 AMI では、デフォルトで PV-GRUB AKI を使用します（Amazon EC2 Launch Wizard Quick Start メニューで利用できるすべての準仮想 Linux AMI が含まれています）。
- そのため、使用するカーネルにディストリビューションとの互換性がある場合、インスタンスで別のカーネルを使用するために必要な追加の手順はありません。
- インスタンスでカスタムカーネルを実行するには、必要としているものに近い AMI でインスタンスを起動する方法が最適です。
- この方法では、カスタムカーネルをインスタンス上でコンパイルして、「GRUB の設定」で説明されているように、そのカーネルで起動するように menu.lst ファイルを変更します。

- AMI のカーネルイメージが PV-GRUB AKI であることを Amazon EC2 コマンドラインツール (チェックするカーネルイメージ ID を代用します) で次の describe-images コマンドを実行して検証できます。


~~~bash
# aws ec2 describe-images --owners self  | jq ".[][0]"
{
  "Description": "Live Image",
  "ImageType": "machine",
  "Public": false,
  "CreationDate": "2016-02-24T02:06:45.000Z",
  "RootDeviceName": "/dev/sda1",
  "OwnerId": "757103751050",
  "KernelId": "aki-176bf516",
  "ImageLocation": "757103751050/ImageLive",
  "VirtualizationType": "paravirtual",
  "Name": "ImageLive",
  "Hypervisor": "xen",
  "ImageId": "ami-983231f6",
  "RootDeviceType": "ebs",
  "State": "available",
  "BlockDeviceMappings": [
    {
      "Ebs": {
        "Encrypted": false,
        "VolumeType": "standard",
        "VolumeSize": 120,
        "SnapshotId": "snap-bf0d23ac",
        "DeleteOnTermination": true
      },
      "DeviceName": "/dev/sda1"
    },
    {
      "Ebs": {
        "Encrypted": false,
        "VolumeType": "gp2",
        "VolumeSize": 100,
        "SnapshotId": "snap-6996c955",
        "DeleteOnTermination": false
      },
      "DeviceName": "/dev/sdf"
    },
    {
      "VirtualName": "ephemeral0",
      "DeviceName": "/dev/sdb"
    }
  ],
  "Architecture": "x86_64"
}
~~~

- Name フィールドが pv-grub で始まるかどうかを確認します。 (？？？)


## PV-GRUB の制約事項

PV-GRUB には次の制約事項があります。

- PV-GRUB の 64 ビットバージョンを使用して 32 ビットカーネルを起動したり、PV-GRUB の 32 ビットバージョンを使用して 64 ビットカーネルを起動したりすることはできません。
- PV-GRUB AKI の使用時には、Amazon ラムディスクイメージ（ARI）を指定できません。
- AWS は、PV-GRUB が EXT2、EXT3、EXT4、JFS、XFS、ReiserFS のファイルシステム形式で動作することをテストし、確認しています。その他のファイルシステム形式では動作しない場合があります。
- PV-GRUB は、gzip、bzip2、lzo、xz 圧縮形式を利用して圧縮されたカーネルを起動できます。
- Cluster AMI は PV-GRUB をサポートせず、また、必要としません。完全ハードウェア仮想化（HVM）が使用されるためです。準仮想インスタンスは PV-GRUB を使用して起動トします。
- 一方、HVM インスタンスボリュームは実際のディスクのように扱われ、その起動プロセスはパーティション分割ディスクとブートローダーを備えるベアメタルオペレーティングシステムの起動プロセスに似ています。
- PV-GRUB バージョン 1.03 以前では、GPT パーティショニングをサポートしません。MBR パーティショニングがサポートされています。
- Amazon EBS で Logical Volume Manager（LVM）を使用する場合、LVM の外側に別の起動パーティションが必要です。その場合、LVM で論理ボリュームを作成できます。


## GRUB の設定

PV-GRUB を起動するには、GRUB menu.lst ファイルがイメージに含まれている必要があります。このファイルの最も一般的な場所は /boot/grub/menu.lst です。

- 次の例は、PV-GRUB AKI を使用して AMI を起動する menu.lst 設定ファイルです。
- この例では、Amazon Linux2015.09 (この AMI の元々のカーネル) と Vanilla Linux4.3 (https://www.kernel.org/ の新しいバージョンの Vanilla Linux カーネル) の 2 つのカーネルエントリを選択できます。
- Vanilla エントリは、この AMI の元々のエントリからコピーされました。
- kernel と initrd パスは新しい場所に更新されました。
- [default 0] パラメータは、ブートローダをそれが検出した最初のエントリ（この場合、Vanilla エントリ）にポイントします。
- [fallback 1] パラメータは、最初のエントリの起動に問題が発生した場合、次のエントリにブートローダをポイントします。

~~~
default 0
fallback 1
timeout 0
hiddenmenu

title Vanilla Linux 4.3
root (hd0)
kernel /boot/vmlinuz-4.3 root=LABEL=/ console=hvc0
initrd /boot/initrd.img-4.3

title Amazon Linux 2015.09 (4.1.10-17.31.amzn1.x86_64)
root (hd0)
kernel /boot/vmlinuz-4.1.10-17.31.amzn1.x86_64 root=LABEL=/ console=hvc0
initrd /boot/initramfs-4.1.10-17.31.amzn1.x86_64.img
~~~

- Ubuntu

~~~
# cat /boot/grub/menu.lst | grep -v "^#" | grep -v "^$"
default         0
timeout         0
hiddenmenu
title           Ubuntu 14.04.2 LTS, kernel 3.13.0-48-generic
root            (hd0)
kernel          /boot/vmlinuz-3.13.0-48-generic root=LABEL=cloudimg-rootfs ro console=hvc0
initrd          /boot/initrd.img-3.13.0-48-generic
title           Ubuntu 14.04.2 LTS, kernel 3.13.0-48-generic (recovery mode)
root            (hd0)
kernel          /boot/vmlinuz-3.13.0-48-generic root=LABEL=cloudimg-rootfs ro  single
initrd          /boot/initrd.img-3.13.0-48-generic
~~~


## Amazon PV-GRUB カーネルイメージ ID

PV-GRUB AKI はすべての Amazon EC2 リージョンで利用できます。32 ビットと 64 ビットの両方のアーキテクチャタイプに AKI があります。最新の AMI では、デフォルトで PV-GRUB AKI が使用されます。

すべてのバージョンの PV-GRUB AKI がすべてのインスタンスタイプと互換性があるとは限らないため、常に最新バージョンの PV-GRUB AKI を使用することをお勧めします。次の describe-images コマンドを使用し、現在のリージョンの PV-GRUB AKI のリストを取得します。

~~~bash
# aws ec2 describe-images --owners amazon --filters Name=name,Values=pv-grub-*.gz | jq '.[][] | .ImageId + " " + .Name'
"aki-136bf512 pv-grub-hd0_1.04-i386.gz"
"aki-176bf516 pv-grub-hd0_1.04-x86_64.gz"
"aki-196bf518 pv-grub-hd00_1.04-i386.gz"
"aki-1f6bf51e pv-grub-hd00_1.04-x86_64.gz"
"aki-3e99283f pv-grub-hd00_1.03-i386.gz"
"aki-40992841 pv-grub-hd00_1.03-x86_64.gz"
"aki-42992843 pv-grub-hd0_1.03-i386.gz"
"aki-44992845 pv-grub-hd0_1.03-x86_64.gz"
~~~


## PV-GRUB のバージョンを更新するには

- インスタンスが古いバージョンの PV-GRUB を使用している場合は、最新バージョンに更新する必要があります。

1. Amazon PV-GRUB カーネルイメージ ID で、使用するリージョンとプロセッサアーキテクチャーの最新の PV-GRUB AKI を特定します。

2 .インスタンスを停止します。使用されるカーネルイメージを変更するには、インスタンスを停止する必要があります。

~~~
$ ec2-stop-instances instance_id --region region
INSTANCE	instance_id	stopped	stopped
~~~

3. インスタンスに使用するカーネルイメージを変更します。

~~~
$ ec2-modify-instance-attribute --kernel kernel_id --region region instance_id
~~~

4 .インスタンスを再起動します。

~~~
$ ec2-start-instances --region region instance_id
~~~
