# volumes


- 過去に実行したコンテナがあればそのコンテナからvolumesを新しいコンテナにコピーする
- volumesに作成したデータは失われない
- コンテナ間で同じようなファイルを参照している場合 `volumes` に指定 (外部パッケージ, bundle, node_modules)


## 全削除

~~~zsh
% docker volume rm $(docker volume ls -qf dangling=true)
~~~

[volume prune](https://docs.docker.com/engine/reference/commandline/volume_prune/#parent-command):

~~~zsh
% docker volume prune
~~~



## docker-compose volumes

- [ボリューム設定リファレンス](https://matsuand.github.io/docs.docker.jp.onthefly/compose/compose-file/compose-file-v3/#volume-configuration-reference)

項目(v3.9):

- driver
- driver_opts
- attachable
- enable_ipv6
- ipam
- internal
- labels
- external
