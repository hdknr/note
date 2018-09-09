#  launchd

- a unified service-management framework, starts, stops and manages daemons, applications, processes, and scripts in macOS.
- [wikipedia](https://en.wikipedia.org/wiki/Launchd)/[jp](https://ja.wikipedia.org/wiki/Launchd)

## launchctl

- [コマンド/launchctl - MacWiki](http://macwiki.osdn.jp/wiki/index.php/%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89/launchctl)
- [Macのlaunchctlでサービスの自動起動をさせたくない時のためのメモ - Qiita](https://qiita.com/ono_matope/items/e437a35c3921ad35d109)

## launchd.plist

| 場所 | 用途 |
|:----|:-----|
| `~/Library/LaunchAgents/<Label>.plist`|ユーザーごと設定できる**エージェント**|
| `/Library/LaunchAgents/<Label>.plist`|管理者用の**エージェント**|
| `/Library/LaunchDaemons/<Label>.plist`|システム共通の**デーモン**（`root`がオーナー）|
| `/System/Library/LaunchAgents/<Label>.plist`  | OS提供(いじるな)  |
| `/System/Library/LaunchDaemons/<Label>.plist` | OS提供(いじるな) |



- [launchd.plistの書き方 | Drowsy Dog's Diary](http://ka-zoo.net/2013/04/launchd-plist/)
- [launchdで定期的にスクリプトを実行 - Qiita](https://qiita.com/rsahara/items/7d37a4cb6c73329d4683)

自動起動:

~~~xml
<key>KeepAlive</key>
    <true/>
~~~
