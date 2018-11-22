# モーダルウィンドウ

~~~js
const subWindow = new BrowserWindow({
    parent: mainWindow,                 //親ウィンドウのBrowserWindowオブジェクト
    modal: true,
});
subWindow.loadURL(`file://${__dirname}/subwindow_content.html`);
~~~

~~~js 
"use strict";

const { remote } = require('electron');

function openModal() {
  let win = new remote.BrowserWindow({
    parent: remote.getCurrentWindow(),
    modal: true
  })

  var theUrl = 'file://' + __dirname + '/modal.html'
  console.log('url', theUrl);

  win.loadURL(theUrl);
}
~~~

## 記事

- [Electron を試す 6 – 複数ウィンドウの管理 – アカベコマイリ](http://akabeko.me/blog/2015/12/electron-6/)
- [TamkeenLMS/electron-window-manager: A NodeJs module that handles window management for Electron (Atom Shell, previously).](https://github.com/TamkeenLMS/electron-window-manager)
- [BrowserWindow | Electron](https://electronjs.org/docs/api/browser-window)

