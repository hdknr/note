Swift: HelloSwift with XCode 6.0.1

# Project作成

- XCode起動
- File->New->Project... 

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/1.png)

- iOS->Application->Single View Application

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/2.png)

- Language: Swift (Bundle Identifier "jp.lafoglia.HelloSwift" )

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/3.png)

- Save this project

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/4.png)

## ファイル一覧

~~~
Peeko:Projects hide$ tree HelloSwift/
HelloSwift/
├── HelloSwift
│   ├── AppDelegate.swift
│   ├── Base.lproj
│   │   ├── LaunchScreen.xib
│   │   └── Main.storyboard
│   ├── Images.xcassets
│   │   └── AppIcon.appiconset
│   │       └── Contents.json
│   ├── Info.plist
│   └── ViewController.swift
├── HelloSwift.xcodeproj
│   ├── project.pbxproj
│   ├── project.xcworkspace
│   │   ├── contents.xcworkspacedata
│   │   └── xcuserdata
│   │       └── hide.xcuserdatad
│   │           └── UserInterfaceState.xcuserstate
│   └── xcuserdata
│       └── hide.xcuserdatad
│           └── xcschemes
│               ├── HelloSwift.xcscheme
│               └── xcschememanagement.plist
└── HelloSwiftTests
    ├── HelloSwiftTests.swift
    └── Info.plist

12 directories, 13 files

~~~


# Main.storyboard

## ボタン追加

- Buttonの追加 (ダブクリしてラベル変更)

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/5.png)

## ラベル追加

- Labelの追加

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/6.png)


# Outlet & Action

## アシスタントエディタでVewiController.swiftを開く

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/7.png)


## ラベルのOutlet

- StoryboardのラベルからControlキー + マウスドラッグで、ViewController.swiftにドロップ
- "TimeLabel"というOutlet名にして、"Connect"

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/8.png)

## ボタンのAction
- 同じくボタンからControlキー + マウスドラッグで、ViewController.swiftにドロップ
- Connectionを"Action"にする
- "OnNowTouchUpInside"というAction名で"Connect"

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/9.png)

# アクションがおきたら時間をセットする

~~~
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var TimeLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


    @IBAction func OnNowTouchUpInside(sender: AnyObject) {
        
        TimeLabel.text = NSDate().description
    }
}
~~~

# 実行

- シュミレータ変更

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/10.png)

- 実行ボタン


![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/11.png)

# 実機
- https://developer.apple.com

## App ID


![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/12.png)

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/13.png)

## Provisioning Profile

- 開発モード

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/14.png)

- アプリケーション選択

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/15.png)

- 証明書選択(証明書を作っておく事)

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/16.png)

- デバイス選択(デバイス登録しておく事)

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/17.png)

- 名前を指定して作成

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/18.png)

- DownloadしてダブクリするとXCodeで認識されます

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/19.png)


## iPhoneを接続して、切り替え

- "iPhone4h"という名前の iPhone5Sに切り替え

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/swift/HelloSwift/20.png)

- 実行

実行ボタンをおすとデプロイされて起動


