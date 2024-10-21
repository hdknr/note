# output

1. terraform applyを実行後にCLIにプリントされる
2. 子モジュールの属性を親モジュールに公開できる
3. terraform_remote_stateを使うことで他の構w成からアクセスできる

```bash
% terraform output -json
```

## 出力JSONを .ini 形式に変更

```bash
jq -r 'to_entries  | map(\"\(.key)=\(.value.value)\") | .[]'
```

## 記事

- [Terraformのoutputとは何か](https://qiita.com/kyntk/items/2cdd38c2438ac257ac4e)
- [Output Data from Terraform](https://developer.hashicorp.com/terraform/tutorials/configuration-language/outputs)
- [Command: output](https://developer.hashicorp.com/terraform/cli/commands/output#use-in-automation)
