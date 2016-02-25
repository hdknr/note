- [Linux インスタンスでの起動時のコマンドの実行](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/user-data.html)

## 概要

- Amazon EC2 でインスタンスを起動するとき、起動後にそのインスタンスに `ユーザーデータ`を渡すことができます。
- 一般的な自動設定タスクを実行したり、スクリプトを実行したりできます。

2 つのタイプのユーザーデータを Amazon EC2 に渡すことができます。

- シェルスクリプト
- cloud-init ディレクティブ

また、このデータは以下の形式で起動ウィザードに渡すこともできます。

- プレーンテキスト
- ファイル（コマンドラインツールでインスタンスを起動する場合に便利です）
-  base64 でエンコードされたテキスト（API 呼出の場合）


参考

- [What is AWS CloudFormation?](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [What is AWS OpsWorks?](http://docs.aws.amazon.com/opsworks/latest/userguide/welcome.html)
- [チュートリアル: Amazon Linux への LAMP ウェブサーバーのインストール](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/install-LAMP.html)


## シェルスクリプト

- シェルスクリプトに詳しい場合、シェルスクリプトが起動時に指示を送る最も簡単で完全な方法となります。
- cloud-init ログファイル（/var/log/cloud-init.log）にコンソール出力が記録されるので、インスタンスが意図したとおりに動作しない場合、起動後にスクリプトを簡単にデバッグできます。
- [IMPORTANT] ユーザーデータのスクリプトおよび cloud-init ディレクティブは、インスタンスを起動するときの初回の起動サイクルでのみ実行されます。
