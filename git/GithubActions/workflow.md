# Workflow

- https://docs.github.com/en/actions/using-workflows/about-workflows

## 手動実行の有効化(`workflow_dispatch`)

```yml
on:
  push:
    branches:
      - master
    paths:
      - "docs/**"
  workflow_dispatch:
```

## 自動実行(`repository_dispatch`)

```yml
on:
  push:
    branches:
      - master
    paths:
      - "docs/**"
  repository_dispatch:
```

## `working-directory`

defaults: run のディレクトリをデフォルトで指定:

```yml
defaults:
  run:
    working-directory: python
```

- [GitHub Actions で作業ディレクトリを変更したい](https://blog.takuchalle.dev/post/2020/02/20/github_actions_change_directory/)
- [Github Actions の paths で、特定ディレクトリ下で変更があったときだけ何かする](https://intothelambda.com/blog/github-actions-with-paths/)

## ストレージ節約

- [【GitHub Actions】ストレージの使用容量を削減する](https://qiita.com/probabilityhill/items/d6e0b1ba0588bd4099a6)
