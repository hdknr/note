# 依存関係

- https://12factor.net/dependencies
- `Explicitly declare and isolate dependencies`

依存関係:

- Docker: `FROM` , マルチステージビルド
- k8s: イメージ -> Pod -> ReplicaSet -> Deployment -> Service
- Helm: 親チャート -> 子チャート (requirements.yml, charts/)

