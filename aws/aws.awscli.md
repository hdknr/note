# awscli

## インストール

### 公式

- [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


#### Linux

~~~bash
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
~~~

#### macOS

- GUIインストーラでよい

~~~bash
% tree  /usr/local/aws-cli -L 1 -I "*.so|*egg*|*dylib|*.zip"
~~~

~~~
/usr/local/aws-cli
├── Python
├── _struct
├── aws
├── aws_completer
├── awscli
├── cryptography
├── docutils
├── include
├── lib
└── zlib
~~~

~~~bash
% /usr/local/aws-cli/aws --help
~~~ 

~~~ 
usage: aws [-h] [--profile PROFILE] [--debug]

optional arguments:
  -h, --help         show this help message and exit
  --profile PROFILE
  --debug
~~~ 

~~~bash
% ls -l /usr/local/bin/aws
lrwxr-xr-x  1 root  admin  22  1  7 12:07 /usr/local/bin/aws -> /usr/local/aws-cli/aws
~~~

~~~bash
% aws --version
aws-cli/2.4.9 Python/3.8.8 Darwin/21.2.0 exe/x86_64 prompt/off
~~~



- 設定

~~~bash

$ aws configure
AWS Access Key ID [None]: XKIXIQXL35DTBNISJZGQ
AWS Secret Access Key [None]: yG9tmKOT85ACdFYHTA/mO/Y1OAksurhsGIl6U0yh
Default region name [None]: ap-northeast-1
Default output format [None]:
~~~

~~~bash
$ tree ~/.aws
/Users/hide/.aws
├── config
└── credentials

0 directories, 2 files
~~~

~~~bash
$ more ~/.aws/config
[default]
region = ap-northeast-1
~~~

~~~bash
$ more ~/.aws/credentials
[default]
aws_access_key_id = XKIXIQXL35DTBNISJZGQ
aws_secret_access_key = yG9tmKOT85ACdFYHTA/mO/Y1OAksurhsGIl6U0yh
~~~

## プロファイル


プロファイルを追加:

~~~bash
$ aws configure --profile ictact

$ aws configure --profile unitedly
AWS Access Key ID [None]: AAAAAAAAAAATZAZDZR4Q
AWS Secret Access Key [None]: SbbbbbbbbbbbbbbbS32OBRMoqjkpNPHaj9d6C5HJ
Default region name [None]: ap-northeast-1
Default output format [None]: json
~~~

~~~bash
$ cat ~/.aws/config

[default]
region = ap-northeast-1

[profile ictact]
output = json
region = ap-northeast-1
~~~

~~~bash
$ cat ~/.aws/credentials

[default]
aws_access_key_id = XKIXIQXL35DTBNISJZGQ
aws_secret_access_key = yi2tmKOT95WCdFYHTWfdafdsafdapaOWksurhsiIl6Ugyh

[profile ictact]
aws_access_key_id = XKIXI26V7E6YDWGJY32Q
aws_secret_access_key = TgJdgadNIZyaUg5akGGSGOjTHFAw9SfdsakkelNURoUvfC
~~~

## プロファイルを固定

~~~bash 
$ export AWS_PROFILE=user2
~~~

## 記事

- [AWS-CLIの初期設定のメモ - Qiita](https://qiita.com/reflet/items/e4225435fe692663b705)
- [AWS CLIで複数アカウントのアクセスキーを管理して扱う設定](http://qiita.com/kwsmkn/items/ce72d8e4cc35f1fc01b5)
- [AWS CLIを使ってEC2インスタンスの情報を取得する](http://qiita.com/toshiro3/items/37821bdcc50c8b6d06dc)
- [【AWS】CLIの初期設定について（認証情報とコマンド補完）](http://www.task-notes.com/entry/20141026/1414322858)
- [名前付きプロファイル](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-multiple-profiles.html)
