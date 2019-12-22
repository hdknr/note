# nvram - manipulate firmware NVRAM(不揮発性ランダムアクセスメモリ) variables

## nvram

- NVRAM (不揮発性ランダムアクセスメモリ) は、Mac がすばやくアクセスできるように所定の設定情報を記憶しておく小容量のメモリです。
- PRAM (パラメータ RAM) にも似たような情報が保存されていて、NVRAM と PRAM のリセット手順は同じです。

保存されている情報:

- 音量
- 画面解像度
- 選択されている起動ディスク
- 時間帯
- 最近起きたカーネルパニックの情報など

## 起動時にNVRAM をリセットする

- `option` + `⌘` + `p` + `r` を同時に `20 秒` ぐらい押す

## 起動音を消す

- [Mac で NVRAM または PRAM をリセットする - Apple サポート](https://support.apple.com/ja-jp/HT204063)
- [アプリを使わずにMacの起動音量を調整する - 涼の成長記録](http://ryo021021.hatenablog.com/entry/2014/04/05/020525)

~~~bash 
$ sudo nvram SystemAudioVolume=%80
~~~