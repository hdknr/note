# ECS(Elastic Container Service)

- ECS(Elastic Container Service)
- ECR(Elastic Container Registry)
- EKS(Elastic Kubernetes Service)

## トピック

- [定期](aws.ecs.cron.md)

## ECS

３要素:

- タスク
- サービス
- クラスター

### タスク

| ECS        | Docker         | 補足                        |
| ---------- | -------------- | --------------------------- |
| タスク     | コンテナ       |                             |
| タスク定義 | ンテナ起動設定 | docker-compose.yml 的なもの |

### サービス

ECS での概念:

- サービス = デーモンプロセス = タスク + ALB + AutoScale
- タスクの起動管理をするタスク

### クラスター

タスクを動かすインフラ概念:

- EC2
- Farget

Kubernetes クラスタよりも単純なクラスタ(=Docker のホスティング環境)

## [ECR](ECR.md)

- レポジトリ(private/public)

## 記事

- [決めろ最強の ECS! 〜起動タイプ × 負荷分散 × デプロイ方法で自分だけのアーキテクチャ〜](https://qiita.com/hiroga/items/4229d5d6f20f33ab7435)

EventBridge:

- [【AWS】EventBridge で FargateECS を自動停止/起動する](https://k9s.hatenablog.jp/entry/2022/09/28/161359)
