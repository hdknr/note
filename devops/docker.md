- [debian9にdocker最新版をインストール](http://qiita.com/tukiyo3/items/bc909d08930d7f61b501)

- [Docker を本番環境で４ヶ月運用して分かった HARD THINGS](http://staycreative.jp/2015/12/docker-production-hard-things/)

- AMI の管理が不要になる(コンテナイメージがアプリケーションのマスターイメージとなるため、オートスケーリング時には DockerHub から最新のイメージを pull して run するだけで済む)

CIやデプロイに時間がかかる()

- CircleCI のキャッシュ機構と若干相性が悪いため比較的ビルドに時間がかる
- DockerHub への push もインターネット通信のため時間がかかる
- 障害時の切り戻しに時間がかかる(tag を付け替える機能は DockerHub の API に無いため、一度ローカルに pull して付け替え、再度 push)


# Mac

- [VirtualBoxはもういらない？Docker社が開発中のDockerForMacの紹介](http://qiita.com/sadayuki-matsuno/items/afce49a2ab017fd86117)
