# destroy

- [Provisioning Infrastructure: destroy](https://www.terraform.io/cli/commands/destroy)
- 実際は `apply -destroy` コマンドのこと

モジュール指定:

~~~zsh
% terraform -chdir=admin destroy -target module.config
~~~

## オプション

- [-target](options.target.md)

## 指定したリソース以外の削除

- 除外オプションはない
- 削除したいリソースを全て `-target` で複数回指定して削除する ([terraform state list](state.md) などで一覧を作る)
