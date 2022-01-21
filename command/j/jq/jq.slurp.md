# `--slurp` / `-s`: JSONに戻す

入力内の各JSONオブジェクトに対してフィルターを実行する代わりに、 入力ストリーム全体を大きな配列に読み取り、フィルターを1回だけ実行する



## 例

- $DEPKEYの名前で設定したタグに配置名$ENV(`prod`, `stage`, `devel`など)がはいっていいる
- 上記の条件の AWS AMI を一覧する
- `deploy-server｀タグにサーバー名がはいっているので、 `サーバー名` : `ami id` のJSONを作る 


~~~bash
ENV=$1
DEPKEY=taiheicloud-deploy
aws --profile taiheicloud ec2 describe-images \
    --filters  Name=tag-key,Values=$DEPKEY \
    --query 'Images[].{Tags:Tags[?Value != `$1`],ImageId:ImageId}' | jq  \
    '.[] | (.Tags | from_entries) as $tags | {server: $tags["deploy-server"], ami: .ImageId}'  | jq \
    --slurp '. | reduce .[] as $o ({}; .[$o["server"]] = $o["ami"])' | tee -a /tmp/hoge.json
~~~bash

~~~json
{
    "server1",  "ami-0115a3169dcb1d138",
    "server2",  "ami-0225a3269dcb2d238",
    "server3",  "ami-0335a3369dcb3d338",
    "server4",  "ami-0445a4469dcb4d448"
}
~~~

## 資料

- [jqの出力をパイプでつなげた時の挙動(slurpとunbuffered)について](https://pod.hatenablog.com/entry/2017/08/29/215253)