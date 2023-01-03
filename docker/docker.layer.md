# レイヤー

レイヤー:

- 変更差分: ルートファイルシステムに対する差分のtarファイル
- RUN, COPY, ADD でレイヤーが作られる
- レイヤーが多すぎると `max depth exceeded`



## 記事

- [docker ビルド時のレイヤー上限は 125](https://www.kimullaa.com/entry/2021/05/11/082647)
- [【Docker】「max depth exceeded」エラーについて考える](https://blog.websandbag.com/entry/2018/05/15/235514)
- [Reduce docker image size by minimizing the number of layers](https://gist.github.com/shinsenter/4f1f4f16a1f5b9a02ef9ba4faf19233d)
- [Minimize the number of layers](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#minimize-the-number-of-layers)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/): 前ステージのアーチファクトをコピーすることで、必要なレイヤーを減らせる
- [Dockerイメージのレイヤの考え方とイメージの軽量化について](https://www.itbook.info/network/docker02.html)
- [Dockerコンテナのレイヤ構造とは？](https://qiita.com/okmtz/items/f8231c83134a6363647b)
- [知らないと損する Docker イメージのレイヤ構造とは](https://www.techscore.com/blog/2018/12/10/docker-images-and-layers/)
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

