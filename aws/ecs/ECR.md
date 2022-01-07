# ECR

## Dockerイメージのプッシュ

- `{アカウントID}.dkr.ecr.ap-northeast-1.amazonaws.com` が URLプレフィックス
- `{アカウントID}.dkr.ecr.ap-northeast-1.amazonaws.com/{レポジトリ名}` が レポジトリURI (`ECS`の`タスク`の`コンテナ`の`イメージ`としてこのURIを設定する)

Dockerに認証情報でログイン:

~~~bash
aws ecr get-login-password --profile spindd --region ap-northeast-1 | docker login --username AWS --password-stdin 699120128753.dkr.ecr.ap-northeast-1.amazonaws.com
~~~

~~~
Login Succeeded
~~~

タグ付け:

~~~bash
docker tag hdknr/djdocker:latest 699120128753.dkr.ecr.ap-northeast-1.amazonaws.com/djdocker:latest
~~~


プッシュ:

~~~bash
docker push 699120128753.dkr.ecr.ap-northeast-1.amazonaws.com/djdocker:latest
~~~

~~~
The push refers to repository [699120128753.dkr.ecr.ap-northeast-1.amazonaws.com/djdocker]
465669d43986: Pushed 
fae040b29ff0: Pushed 
a0c1b5a971a6: Pushed 
c11164d977ad: Pushed 
8c1b2caae754: Pushed 
ccbefb30278f: Pushed 
7a8a38bf5538: Pushed 
0d77d4546954: Pushed 
98d95bdfa037: Pushed 
da9418a2e1b1: Pushed 
2e5b4ca91984: Pushed 
527ade4639e0: Pushed 
c2c789d2d3c5: Pushed 
8803ef42039d: Pushed 
latest: digest: sha256:b410dc2bcfe41cedc9d6a0a770731ff1279c29f6238b352d144bf336627e77b2 size: 3264
~~~

### bash

~~~bash
#!/bin/bash
REPO=djdocker
PROFILE=spindd
AWS_ID=123456789012
#
REGION=ap-northeast-1
ECR=$AWS_ID.dkr.ecr.$REGION.amazonaws.com
#
aws ecr get-login-password --profile $PROFILE --region $REGION  | docker login --username AWS --password-stdin $ECR
docker build -t $REPO . 
docker tag $REPO:latest $ECR/$REPO:latest
docker push $ECR/$REPO:latest
~~~

## lastest の確認


~~~bash
% aws ecr list-images --profile cloud --registry-id 726533500155 --repository-name ffs-prod | jq '.imageIds[] | select(.imageTag == "latest")'
~~~

~~~json
{
  "imageDigest": "sha256:d3a16b0c20248f4b57677bebe22170e5ee5460a1b06a56c7f4084fbca1ab624c",
  "imageTag": "latest"
}
~~~ 
