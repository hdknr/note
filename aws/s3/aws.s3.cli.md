# AWS CLI コマンドでの操作 
## s3

- デフォルトでは `同期` なので、変更がないファイルは更新されません！！！
- [sync](http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)

~~~bash
$ aws s3 sync s3://bucket-name/uploads s3://bucket-name-dev/uploads
~~~


## リスト

- [ls](http://docs.aws.amazon.com/cli/latest/reference/s3/ls.html)
