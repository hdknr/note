# AMI


## EC2: 指定したタグ = AMI-ID のJSONを吐き出す

- [jq - convert a list of objects into a summarized object](https://stackoverflow.com/questions/47551333/jq-convert-a-list-of-objects-into-a-summarized-object)
- [jqの出力をパイプでつなげた時の挙動(slurpとunbuffered)について](https://pod.hatenablog.com/entry/2017/08/29/215253)

例:

- EC2のAMI一覧
- server-name というタグのキーにサーバー名が入っている
- 最終的に `サーバー名: ami-di` のJSONを作る

~~~bash
$ cat ~/Downloads/ami-prod.json | \
  jq  '.[] | (.Tags | from_entries) as $tags | {server: $tags["server-name"], ami: .ImageId}' | \
  jq --slurp '. | reduce .[] as $o ({}; .[$o["server"]] = $o["ami"])'
~~~


~~~json
{
  "tress": "ami-923211916836ff79e",
  "masters": "ami-93b6d7dfdfe9e8b67",
  "servifes": "ami-947ab1e7214178b6f",
  "epm": "ami-9496367a2376b71b4",
  "users": "ami-9f33e6216fddfebb1"
}
~~~