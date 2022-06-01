# イメージ

## PROVISIONING が遅い

- AWSイメージはキャッシュされているので早い
- カスタムイメージもAWSイメージをベースにすると、Layerキャッシュが効く

## 資料

- [カスタムイメージを使ってCodebuildでbuildするまで。](https://qiita.com/fake-deli-ca/items/a5ed9b0ea34411273765)
- [Provisioning a custom Docker image on AWS CodeBuild takes a very long time](https://stackoverflow.com/questions/62025740/provisioning-a-custom-docker-image-on-aws-codebuild-takes-a-very-long-time)