# EC2

- [AMI](ec2.ami.md)

## インスタンス情報 (ec2 describe-instances)

- [メタデータ](aws.instance.metadata.md)
- [Ubuntu](aws.ubuntu.md)
- [Ubuntu Boot](aws.ubuntu.boot.md)

awscli:

- [インスタンス](aws.instances.md)

## [インスタンスタイプ](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/instance-types.html)

汎用:

- t2: t2.nano | t2.micro | t2.small | t2.medium | t2.large | t2.xlarge | t2.2xlarge |
- t3: t3.nano | t3.micro | t3.small | t3.medium | t3.large | t3.xlarge | t3.2xlarge |
- m4: m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m4.16xlarge |
- m5: m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.12xlarge | m5.24xlarge |
- m5d: m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.12xlarge | m5d.24xlarge

コンピューティングの最適化:

- c4: c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge |
- c5: c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.18xlarge |
- c5d: c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.18xlarge

メモリ最適化

- r4: r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge |
- r5: r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.12xlarge | r5.24xlarge |
- r5d: r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.12xlarge | r5d.24xlarge | - x1: x1.16xlarge | x1.32xlarge |
- x1e: x1e.xlarge | x1e.2xlarge | x1e.4xlarge | x1e.8xlarge | x1e.16xlarge | x1e.32xlarge
- z1d: z1d.large | z1d.xlarge | z1d.2xlarge | z1d.3xlarge | z1d.6xlarge | z1d.12xlarge

ストレージの最適化

- d2: d2.xlarge | d2.2xlarge | d2.4xlarge | d2.8xlarge |
- h1: h1.2xlarge | h1.4xlarge | h1.8xlarge | h1.16xlarge |
- i3: i3.large | i3.xlarge | i3.2xlarge | i3.4xlarge | i3.8xlarge | i3.16xlarge

高速コンピューティング

- f1: f1.2xlarge | f1.4xlarge | f1.16xlarge
- g3: g3.4xlarge | g3.8xlarge | g3.16xlarge
- p2: p2.xlarge | p2.8xlarge | p2.16xlarge
- p3: p3.2xlarge | p3.8xlarge | p3.16xlarge

ベアメタル

- i3.metal | u-6tb1.metal | u-9tb1.metal
