# VS COde

- [#84](https://github.com/hdknr/scriptogr.am/issues/84)

## extensions

- コマンドパレット(`⌘ + shirt + P`)
- `ext install`

- [vscode-restructuredtext/vscode-restructuredtext](https://github.com/vscode-restructuredtext/vscode-restructuredtext)

## コマンドライン

- コマンドパレットで `Shell` で検索し、インストール

~~~bash
$ which code
/usr/local/bin/code

$ code --help
Visual Studio Code v1.2.1

Usage: code [arguments] [paths...]

Options:
  -d, --diff
      Open a diff editor. Requires to pass two file paths as arguments.
  --disable-extensions
      Disable all installed extensions.
  -g, --goto
      Open the file at path at the line and column (add :line[:column] to path).
  --locale <locale>
      The locale to use (e.g. en-US or zh-TW).
  -n, --new-window
      Force a new instance of Code.
  -r, --reuse-window
      Force opening a file or folder in the last active window.
  --user-data-dir <dir>
      Specifies the directory that user data is kept in, useful when running as root.
  --verbose
      Print verbose output (implies --wait).
  -w, --wait
      Wait for the window to be closed before returning.
  --list-extensions
      List the installed extensions.
  --install-extension <extension>
      Installs an extension.
  --uninstall-extension <extension>
      Uninstalls an extension.
  -v, --version
      Print version.
  -h, --help
      Print usage.

~~~

## vim

- [VSCodeVim/Vim](https://github.com/VSCodeVim/Vim)
- [割と突き詰めてやったvim->vscode移行](https://qiita.com/y-mattun/items/45776b7e1942edb2f727)

## Python

- [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [WindowsのVisual Studio CodeでPython!! その３](http://tohnaman.hatenablog.jp/entry/2018/03/25/094607)
- [Visual Studio CodeでPython + Djangoを書いて、py.testを実行してみた](http://thinkami.hatenablog.com/entry/2016/07/05/224416)

## タブ

HTMLだけ2タブにする:

- CTRL + ⌘  + P
- `Preferences: Configure language specific settings`
- 言語選択(django-html とか)
- 右ペインで `ユーザー設定`

~~~json
// Place your settings in this file to overwrite the default settings
{

    // Migrated from previous "File | Auto Save" setting:
    "files.autoSave": "afterDelay",

    // http://tohnaman.hatenablog.jp/entry/2018/03/25/094607
    // "python.formatting.provider": "yapf",
    "[html]": {
        "editor.tabSize": 2,
        "editor.detectIndentation": false
    },
    "[django-html]": {
    },
}
~~~

## 記事

- [Mac版 Visual Studio Codeを使ってみます](http://qiita.com/akiko-pusu/items/185f4fd8484ecd3b3243)
- [ターミナルからVisual Studio Codeを起動する方法【公式の方法】](http://qiita.com/naru0504/items/c2ed8869ffbf7682cf5c)
