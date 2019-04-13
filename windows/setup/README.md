# 設定

## エクスプローラで拡張子を表示

- `設定` > `更新とセキュリティ`

![](windows-explorer-options.png)

## UTF8

- `コントロールパネル` > `時計と地域`
- `地域` > `場所の変更` : `管理` タブ
- `システムロケールの変更` > `ベータ: ワールドワイド言語サポートで Unicode UTF-8を使用`

![](windows-utf8.png)

## ネットワーク共有

- [Windows10とMac OS Xの共有ファイル設定方法 | 端末ごとに解説 - その他ビジネス | ボクシルマガジン](https://boxil.jp/mag/a43/)

## RDP

- [Windows 10 homeにリモートデスクトップ接続できるようにする | 無停電電源装置(UPS) | イートン](https://www.eaton-daitron.jp/techblog/5726.html)
- [リモートデスクトップの接続を許可する方法 ( Windows 10 ) | ドスパラ サポートFAQ よくあるご質問｜お客様の｢困った｣や｢知りたい｣にお応えします。](http://faq3.dospara.co.jp/faq/show/06300?site_domain=default)

## パスを通す

PowerShell で Python のパスを通す:

~~~ps1
PS C:> $env:path += ";C:\Users\hdknr\.windows-build-tools\python27"
~~~

## 管理者権限コンソール

~~~ps1
PS C:>  Start-Process powershell.exe -Verb runas
~~~

- [Windowsでsudoしたい - Qiita](https://qiita.com/AinoMegumi/items/fd56711fe1fd2a0e1bbf)

## クリップボード

- [WSLからWindowsのクリップボードを入出力したい - tmytのらくがき](https://blog.tmyt.jp/entry/2018/02/02/171311)
- `clip.exe` は WSLからも普通に呼べます

## CAPSキー

- [Windows10 CapsLockキーをCtrlキーに割りあててしまおう！ - NOP](http://www.shin-tan.com/swapKey)
