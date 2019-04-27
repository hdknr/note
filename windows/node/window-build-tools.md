# Windows Build Tools

管理コンソール

~~~bash
PS> npm -g i windows-build-tools
~~~

##　パス

~~~ps1
PS C:> $env:path += ";C:\Users\hdknr\.windows-build-tools\python27"
PS C:> python --version
Python 2.7.15
~~~

## v140 ビルドツール

エラー:

    error MSB8020: v140 (プラットフォーム ツールセット = 'v140') のビルド ツールが見つかりません。

    v140 ビルド ツールを 使用してビルドするには、v140 ビルド ツールをインストールしてください。
    または、[プロジェクト] メニューを選択するかソリューションを右クリックし [ソリューションの再ターゲット] を選択して、現在の Visual Studio Tools にアップグレードすることもできます

手動インストール。 UIでインストール内容を変更する:

~~~ps1
PS C:> C:\Users\hdknr\.windows-build-tools\vs_BuildTools.exe
~~~

## 記事

- [WindowsでElectronからNative Moduleを使えるようにする - Qiita](https://qiita.com/maron8676/items/4457b4d70be6db260eee)
- [Windowsでnode-gpyのエラーが止まらない - Qiita](https://qiita.com/kujirahand/items/75af925c558dff4304c4)
- [Can't find Python executable "python" after installing · Issue #56 · felixrieseberg/windows-build-tools](https://github.com/felixrieseberg/windows-build-tools/issues/56)
- [コマンドプロンプトで一時的にパス path を通します。 – oki2a24](https://oki2a24.com/2012/08/11/set-path-temporary-in-command-prompt/)
