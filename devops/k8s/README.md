# k8s / kubernetes

<<<<<<< HEAD
- [クーバネテス](https://www.howtopronounce.com/kubernetes/)
=======
- `クーバネテス`
>>>>>>> 876566e323a7818c5a1ecdaed354ef851fd0957e

## ポッド


ポッドの一覧:

~~~bash 
$ kubectl get pods
~~~

### ポッドを作る

- podは、Kubernetesの最も小さい基本的な構成単位で、podはクラスタ上のプロセスを代表しています。
- [Kubernetes の学習 (2) ～ Pod の作成 - Qiita](https://qiita.com/Arturias/items/62499b961b5d7375f608)
- [k8s pod 概要について自習ノート - Qiita](https://qiita.com/MahoTakara/items/f5130bb6e9e493c46c6b)
- [Pod Overview - Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/)

## プログラム実行

- [Kubernetes: アプリケーションのデバッグ方法 (kubectl exec など) - Qiita](https://qiita.com/tkusumi/items/a62c209972bd0d4913fc)

~~~bash
$ kubectl exec ポッド名 コマンドライン
~~~

## コマンド

- [kebuctl create](kubctl.create.md)
- [kebuctl explain](kubctl.explain.md)

## その他

- [Kubernetes のパッケージマネジャー helm の導入と使い方 - Qiita](https://qiita.com/quickguard/items/48ea2b69395afde3517b)
- [kubectl for Docker Users - Kubernetes](https://kubernetes.io/docs/reference/kubectl/docker-cli-to-kubectl/)
- [Kubernetes Python クライアントを使ってみる - Ian Lewis](https://www.ianlewis.org/jp/kubernetes-python)

## 記事

- [kubernetes初心者のための入門ハンズオン - Qiita](https://qiita.com/mihirat/items/ebb0833d50c882398b0f)