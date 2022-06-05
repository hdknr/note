# terraform cli

- [Basic CLI Features](https://www.terraform.io/cli/commands)

## グローバルオプション (サブコマンド前で指定する) 

| オプション | 意味                                                                           |
| ---------- | ------------------------------------------------------------------------------ |
| -chdir=DIR | Switch to a different working directory before executing the given subcommand. |
| -help      | Show this help output, or the help for a specified subcommand.                 |
| -version   | An alias for the "version" subcommand.                                         |

## コマンド

Initializing Working Directories:

- [init](init.md)
- [get](get.md)

Provisioning Infrastructure:

- [plan](plan.md)
- [apply](apply.md)
- [destroy](destroy.md)

Authenticating:

- [login](login.md)
- [logout](logout.md)


Writing and Modifying Code:

- [console](console.md)
- [fmt](fmt.md)


Inspecting Infrastructure:

- [graph](graph.md)
- [output](output.md)
- [show](show.md)
- [state list](state.md)
- [state show](state.md)

Importing Infrastructure:

- [import](import.md)

Manipulating State:

- [state](state.md)


Managing Workspaces:


- [workspace](workspace.md)


Managing Plugins:

- [providers](workspace.md)
- [version](version.md) 



## 資料

- [[翻訳]Terraform_Commands(CLI)大全](https://qiita.com/HirokiSakonju/items/79d4d950b0732f757eef)
