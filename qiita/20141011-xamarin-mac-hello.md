Xamarin.Mac: HelloMac アプリケーション終了

# Xamarin Studio 5.5 

##  Xamarin.Mac Classic API 

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/qiita/20141011-xamarin-mac-hello/1.png)



![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/qiita/20141011-xamarin-mac-hello/2.png)



# XCode で Outlet作成

## ボタン

MainWindow.xib を開き、 "Push Button" をドラッグ&ドロップ

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/qiita/20141011-xamarin-mac-hello/3.png)

## ボタンのOutlet
- Assistant Editor を開く(MainWindowController.h)
- Closeボタンに Controlキー + マウスクリックで、エディタにドラッグ&ドロップ

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/qiita/20141011-xamarin-mac-hello/4.png)

~~~objc:MainWindowController.h

#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>


@interface MainWindowController : NSWindowController {
    NSButton *CloseButton;
}
@property (assign) IBOutlet NSButton *CloseButton;

@end
~~~

~~~ objc:MainWindowController.m

#import "MainWindowController.h"

@implementation MainWindowController
@synthesize CloseButton;

@end
~~~

- XCode閉じる

~~~
Peeko:HelloMac hide$ find . -name "*.m" -print
./obj/Xcode/0/AppDelegate.m
./obj/Xcode/0/MainWindow.m
./obj/Xcode/0/MainWindowController.m
./obj/Xcode/1/AppDelegate.m
./obj/Xcode/1/MainWindow.m
./obj/Xcode/1/MainWindowController.m
~~~

# MainWindow.designer.cs

- MainWindow.xibで編集したので、 MainWindow.designer.csファイルに自動的に作成される
- ただし、CloseButtonがOutletで定義されるクラスは MainWindowsController(MainWindowsController.h/.m にOutlet定義したので)

~~~csharp:MainWindow.designer.cs

using MonoMac.Foundation;
using System.CodeDom.Compiler;

namespace HelloMac
{
	[Register ("MainWindowController")]
	partial class MainWindowController
	{
		[Outlet]
		MonoMac.AppKit.NSButton CloseButton { get; set; }
		
		void ReleaseDesignerOutlets ()
		{
			if (CloseButton != null) {
				CloseButton.Dispose ();
				CloseButton = null;
			}
		}
	}

	[Register ("MainWindow")]
	partial class MainWindow
	{
		
		void ReleaseDesignerOutlets ()
		{
		}
	}
}
~~~

# MainWindowController.cs

##  メインWindow

- 自動生成 されてます

~~~csharp:MainWindowController.cs

		public new MainWindow Window {
			get { return (MainWindow)base.Window; }
		}
~~~
		
## 終了ボタン

- WindowDidLoad() をオーバーライド

~~~csharp:MainWindowController.cs

		public override void WindowDidLoad ()
		{
			this.CloseButton.Activated += (object sender, EventArgs e) => {
				Window.Close();
			};
		}
~~~
		
		
# AppDelegate.cs

- CloseButtonをクリックすると MainWindowインスタンスがClose()される
- がAppDelegateは行きているのでアプリケーションは終了しません
- AppDelegate管理のWindowが閉じた時にAppDelegateを終了するようにApplicationShouldTerminateAfterLastWindowClosedをオーバーライドしてtrueを返す

~~~csharp:AppDelegate.cs

public override bool ApplicationShouldTerminateAfterLastWindowClosed (NSApplication sender)
{
    return true;
}
~~~		
