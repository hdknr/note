# ECS Fargate

## Elastic File System(EFS) マウント

- [FargateでElastic File System(EFS)が使えるようになりました](https://dev.classmethod.jp/articles/fargate_platform_1_4_update/)
- [【全世界待望】Fargateから共有ファイルストレージのEFSが使えるようになりました！](https://dev.classmethod.jp/articles/efs-fargate/)



## プラクティス

sshd:

- 入れておいた方が無難
- 公開鍵はSystem Managerのパラメータストアから環境変数に渡すのが良いのでは
- 必要な時のみ `サービス` で定義したセキュリティグループの TCP22 をIPアドレス指定で開ける


ロードバランサ:

- ALBのセキュリティグループと、`サービス`のセキュリティグループを分ける
- `サービス` セキュリティグループのTCP80は ALBのセキュリティグループからのみ許す
