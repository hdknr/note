# Dockerfile

## Bashスクリプト実行

- [DockerfileのRUNやCMDをBashのログインシェルで実行させる](https://qiita.com/clomie/items/235192bd62c60b0d0806)
- [DockerfileのCMDとENTRYPOINTを改めて解説する](https://qiita.com/uehaj/items/e6dd013e28593c26372d)
- [How to run a shell script in Dockerfile](https://www.diskinternals.com/linux-reader/dockerfile-run-shell-script/)

## 分割可能？

Dockerfile そのものには直接 `include` 機能はありませんが、いくつかの方法で条件に応じて異なる Dockerfile を使用することができます。

1. **マルチステージビルド**: Dockerfile 内で複数のステージを定義し、ビルド時に特定のステージを選択する方法です。

    ```Dockerfile
    # Stage 1
    FROM node:14 AS build
    WORKDIR /app
    COPY package*.json ./
    RUN npm install
    COPY . .
    RUN npm run build

    # Stage 2
    FROM nginx:alpine
    COPY --from=build /app/build /usr/share/nginx/html
    ```

2. **環境変数を使用**: ビルド時に環境変数を設定し、それに応じて異なる Dockerfile を使用する方法です。

    ```sh
    docker build -f Dockerfile.dev -t myapp:dev .
    docker build -f Dockerfile.prod -t myapp:prod .
    ```

3. **外部スクリプトを使用**: シェルスクリプトや Makefile を使って、条件に応じて異なる Dockerfile を選択する方法です。

    ```Makefile
    ifeq ($(ENV),dev)
        DOCKERFILE := Dockerfile.dev
    else
        DOCKERFILE := Dockerfile.prod
    endif

    build:
        docker build -f $(DOCKERFILE) -t myapp:$(ENV) .
    ```

これらの方法を使えば、条件に応じて異なる Dockerfile を使用することができます。どの方法が最適かは、プロジェクトの構成や要件によります。どれか試してみたい方法はありますか？

ソース: Copilot との会話、 2024/9/6
(1) Dockerfile を書くベスト・プラクティス — Docker-docs-ja 17.06 .... <https://docs.docker.jp/engine/userguide/eng-image/dockerfile_best-practice.html>.
(2) Dockerfileを書くためのベストプラクティス【参考訳】v18.09 - Qiita. <https://qiita.com/zembutsu/items/a96b68277d699f79418d>.
(3) 使用 include 选项拆分 Docker Compose 文件 - OriLight的自留地. <https://blog.amarea.cn/archives/docker-compose-include.html>.
(4) Dockerfileを複数に分けてdocker-compose.ymlからまとめて .... <https://zenn.dev/kotopasi/articles/9dcb3beda38b25>.
(5) Dockerfileでincludeを使う #Makefile - Qiita. <https://qiita.com/d6rkaiz/items/f71032c1f7dfdd44e939>.
(6) Getty Images. <https://www.gettyimages.com/detail/news-photo/in-this-photo-illustration-the-docker-logo-seen-displayed-news-photo/1247853892>.
