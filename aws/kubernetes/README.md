## Pod

Podとは:

- いくつかのコンテナをグループ化したもの。
- Kubernets は Pod 単位で作成、開始、停止、削除といった操作を行う(コンテナ単位では操作しない)。 
- そのため、１つのコンテナを作成したいときも、「コンテナが１つ含まれるPod」を作成することになる。

特徴:

- Pod 内のコンテナは、同一ホスト上に配備される
- Pod 内のコンテナは、仮想NICやプロセステーブルを共有する
- つまり、同じIPを使えたり、互いのプロセスが見えたりする。



## 記事


### 概念

- [今さら人に聞けない Kubernetes とは？](https://qiita.com/MahoTakara/items/85096f8b2632c802ab22)
- [kubernetesを使った開発のベストプラクティスを求めて](https://qiita.com/mihirat/items/668a43a88547792cde7e)
- [Introduction to Kubernetes](https://qiita.com/ocadaruma/items/5a00f87f56e295d3553c)

### Minikube 


- Minikubeはローカルで簡単にKubernetesを実行できるツールです。
- Kubernetesの検証や開発者のために、ノートPC上のVM環境でシングルノードのKubernetesクラスタを実行します。
- 注意事項としては、シングルノードの環境になるので検証できない機能もあります。

- [Minikubeを使ってローカル環境にKubernetes環境を用意する](https://dev.classmethod.jp/cloud/minikube/)
- [ローカルでkubernetesを動かせるminikubeを試す](https://reiki4040.hatenablog.com/entry/2017/04/11/221122)

### 学習

- [Kubernetes の学習 (1) ～ AWS上でのクラスタ構築](https://qiita.com/Arturias/items/8f16194f164aeacbe67d)
- [Kubernetes の学習 (2) ～ Pod の作成](https://qiita.com/Arturias/items/62499b961b5d7375f608)

### kubectl

- [kubernetes : kubectlコマンド一覧](https://qiita.com/suzukihi724/items/241f7241d297a2d4a55c)

### Docker

- [Docker for Mac with Kubernetes](https://qiita.com/taishin/items/920d62a641c9cd58f289)
- [Docker for MacでKubernetes インストールからデプロイまで](https://qiita.com/uni-3/items/a4f2afa0973bfc35b498)
- [Docker for MacはKubernetes for Macだった！？　入門してみた。](https://qiita.com/flyhigh/items/668a21da483dbf1ab145)
- [Docker for Mac にKubernetesがやって来た！(ちょっと追記)](https://blue1st-tech.hateblo.jp/entry/2018/01/06/162306)

### Ubuntu

- [KubernetesでUbuntuのイメージをデプロイする](https://qiita.com/donsan/items/fe144895df91da6d6e1a)