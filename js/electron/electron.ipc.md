# IPC

## [プロセス](https://electronjs.org/docs/tutorial/application-architecture#main-and-renderer-processes)

### メインプロセス

- package.json で `main` で定義されているファイルを実行するプロセス
- メインプロセスが終了＝アプリケーションの終了
- アプリに１つだけ

### レンダラープロセス

- 画面ごとに作成されるプロセス ([BrowserWindow](https://electronjs.org/docs/api/browser-window)で作られるインスタンス)
- メインプロセスからxxxx.htmlを読み込んで画面を表示したら、その画面自体が一つのプロセスで動作しているということ
- メインプロセスからいくらでも作ることが可能

## 通信

### 1. レンダラ -> メイン

- [送信]([ipcRenderer](https://electronjs.org/docs/api/ipc-renderer))
- [受信]([ipcMain](https://electronjs.org/docs/api/ipc-main))

### 2. メイン -> レンダラ

- 送信先のレンダラの `webContents` に対してメッセージを送信する
- [webContents.send](https://electronjs.org/docs/api/web-contents#contentssendchannel-arg1-arg2-)

### 3. レンダラA -> レンダラB

- 1 と 2 を組み合わせる
- 間に メインプロセスを仲介させる

### 4. 同期/非同期

- [send](https://electronjs.org/docs/api/ipc-renderer#ipcrenderersendchannel-arg1-arg2-)
- [sendSync](https://electronjs.org/docs/api/ipc-renderer#ipcrenderersendsyncchannel-arg1-arg2-)

## HTTP リクエストがきたらランダラに通知する

メインプロセス(main/index.js):

~~~js
let mainWindow              // BrowserWindow

require('http').createServer((request, response) => {
  request.addListener('end', () => {
    // HTTP 応答
    response.writeHead(200, {'Content-Type': 'text/plain'})
    response.end('Hello Electron Vue!\n')

    // ランダラへの通知
    mainWindow.webContents.send('network-message', request.headers)
  }).resume()
}).listen(9900, '0.0.0.0')
~~~

レンダラプロセス(renderer/App.vue):

~~~html
<template>
  <div id="app">
    <span v-html="message"></span> <!-- ここにメッセージを表示 --->
    <router-view></router-view>
  </div>
</template>
~~~

~~~js
import { ipcRenderer } from 'electron'

export default {
  created () {
    // IPCイベント受付
    ipcRenderer.on('network-message', (event, arg) => {
      console.log(arg)
      this.message = arg
    })
  },
  data () {
    return {
      message: ''
    }
  },
  name: 'hellovue'
}
~~~

## 記事

- [ElectronのIPCをまとめる - Qiita](https://qiita.com/maecho/items/cb6eb18be2f4ffae60b5)
- [IPC send from main process to renderer - electron - Atom Discussion](https://discuss.atom.io/t/ipc-send-from-main-process-to-renderer/16046)
- [Electronでipcを使ってプロセス間通信を行う - Qiita](https://qiita.com/Misumi_Rize/items/dde76dbf89abee13991c)
- [javascript - How to access DOM elements in electron? - Stack Overflow](https://stackoverflow.com/questions/32780726/how-to-access-dom-elements-in-electron)
- [【Electron連載】第４回 基本編－メイン／レンダラープロセスの話 - Qiita](https://qiita.com/nullpointer_t/items/83cc14225b677f0d72fa)
- [Electronで最初に躓くメインプロセスとレンダラープロセスについて - Electron｜ONE-RUN](https://st40.xyz/one-run/article/502/)
- [Electronでファイルやフォルダの選択 - Qiita](https://qiita.com/_takwat/items/6544342fd4141345bb19)
