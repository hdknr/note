# EFS

## 接続条件と NFSのインバウンド設定

同一 VPCにする:

-  Amazon EFS ファイルシステム
-  Amazon ECS クラスター
-  Fargate タスク


EFSのセキュリティグループ:

- EFSのネットワークインターフェースに割り当てられているセキュリティグループを見つける
- TCP2049(NFS)のインバウンドを許可


Amazon ECS サービスのセキュリティグループ:

- TCP2049(NFS)のインバウンドを許可


## 記事


- [Fargate で実行されている Amazon ECS コンテナまたはタスクに Amazon EFS ファイルシステムをマウントする方法を教えてください。](https://aws.amazon.com/jp/premiumsupport/knowledge-center/ecs-fargate-mount-efs-containers-tasks/)
- [Adding, removing, and updating rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#AddRemoveRules)
