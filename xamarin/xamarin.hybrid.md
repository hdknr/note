[HybridWebViewの実装](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/hybridwebview/)

  プラットフォームごとにビューをレンダリングする

- Xamarin.Forms カスタムUIコントロールはViewクラスを継承する。
- 画面上にレイアウトやコントロールを配置します
- ここでは、 HybridWebViewカスタムコントロール用のカスタムレンダラのくり方をデモします。
- プラットフォームごとのWebコントロールを改良してC#コードがJavaScriptから呼び出されることをデモします


- すべてのXamarin.Formsビューにはレンダラが付属していて、各プラットフォームでネィティブコントロールのインスタンスを作成することができます。
- Viewが iOS のXamarin.Formsアプリでレンダーされる時には、 ViewRendererクラスが生成され、ネイティブの [UIView](https://developer.xamarin.com/api/type/MonoTouch.UIKit.UIView/)コントロールをそこで生成します。
- Androidでは ViewRendererクラスが [View](https://developer.xamarin.com/api/type/Android.Views.View/)コントロールを生成します。
- Windows Phoneと Universal Windows Platform(UWP) では ViewRendererクラスは ネイティブの FrameworkElementコントロールを生成します。
- xamarin.Fromsコントロールがマッピングする レンダラと ネィティブコントロールに関しては、  [Renderer Base Classes and Native Controls](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/renderers/) を参照。


- 以下の図では、 Viewとその実装に対応するネイティブコントロール間の関連を示しています

![](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/hybridwebview/Images/view-classes.png)


レンダリングプロセスによりプラットフォームごとのカスタマイズを実装します。
かくプラットフォームでのViewに対するカスタムレンダラを実装するのです。
このプロセスは以下のようになります。


1. HybridWebView カスタムコントロールを作成
2. Xamarin.Formsより HybridWebViewを利用
3. 各プラットフォームでの HybridWebViewのカスタムレンダラを作成

- それぞれ HybridWebViewレンダラを実装するために順番に説明します。
- JavascriptからC#コードを呼べるようにするのです。
- HybridWebViewインスタンスはHTMLページを表示してユーザーに自分の名前の入力を促します。
- ユーザーがHTMLボタンをクリックすると、 Javascript関数は C# Actionをコールし、ユーザー名を含んだポップアップを表示します。

- C#をJavascriptから呼ぶ手順に関しては、[こちら](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/hybridwebview/#Invoking_C#_from_JavaScript)
- HTMLページの作成に関しては[こちら](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/hybridwebview/#Creating_the_Web_Page)


## HybridWebViewの作成

HybridWebView カスタムコントロールは、 [Xamarin.Forms.View](https://developer.xamarin.com/api/type/Xamarin.Forms.View/) クラスをサブクラスします。

~~~csharp

public class HybridWebView : View
{
  Action<string> action;
  public static readonly BindableProperty UriProperty = BindableProperty.Create (
    propertyName: "Uri",
    returnType: typeof(string),
    declaringType: typeof(HybridWebView),
    defaultValue: default(string));

  public string Uri {
    get { return (string)GetValue (UriProperty); }
    set { SetValue (UriProperty, value); }
  }

  public void RegisterAction (Action<string> callback)
  {
    action = callback;
  }

  public void Cleanup ()
  {
    action = null;
  }

  public void InvokeAction (string data)
  {
    if (action == null || data == null) {
      return;
    }
    action.Invoke (data);
  }
}
~~~

PCLに作成して、以下のAPIを定義します：

- `Uri` プロパティ: ロードするウェブページのアドレス
- `RegisterAction` メソッド : コントロールの `Action` を登録します. 登録されたアクションが`Uri`プロパティでレンダリングされたHTMLに含まれるJavaScriptから呼ばれます。
- `CleanUp`メソッド: 登録された `Action` を捨てます
- `InvokeAction` メソッド: `Action` をコールします。 このメソッドは各プラットフォームのカスタムレンダラから呼ばれます。

## HybridWebView の利用

- HybridWebViewカスタムコントロールは PCLプロジェクトのXAMLで参照することができます。
-  `namespace` プレフィックスを使うことができます。

以下のようにXamlで参照します:

~~~xml
<ContentPage ...
    xmlns:local="clr-namespace:CustomRenderer;assembly=CustomRenderer"
    x:Class="CustomRenderer.HybridWebViewPage"
    Padding="0,20,0,0">

    <ContentPage.Content>
        <local:HybridWebView
          x:Name="hybridWebView"
          Uri="index.html"
          HorizontalOptions="FillAndExpand"
          VerticalOptions="FillAndExpand" />
    </ContentPage.Content>

</ContentPage>
~~~

- `local` ネームスペースプレフィックスは何にでも使えます。
- が、 `clr-namespace` と `assembly`値はカスタムコントロールの詳細に一致する必要があります。
- `namespace` が定義されると、 プレフィックスをつかってカスタムコントロールを参照することができます。

また、以下のようにして HybridWebViewカスタムコントロールをC#ページで利用できるようにします:

~~~csharp
public class HybridWebViewPageCS : ContentPage
{
  public HybridWebViewPageCS ()
  {
    var hybridWebView = new HybridWebView {
      Uri = "index.html",
      HorizontalOptions = LayoutOptions.FillAndExpand,
      VerticalOptions = LayoutOptions.FillAndExpand
    };
    ...
    Padding = new Thickness (0, 20, 0, 0);
    Content = hybridWebView;
  }
}
~~~

- HybridWebViewインスタンスをつかって ネイティブウェブコントロールを各プラットフォームで表示することができます。
- `Uri` プロパティで HTMLファイルを指定します。これは、各プラットフォームプロジェクトに保存され、ネイティブのウェブコントロールで表示されます。
- レンダされたHTMLがユーザーに名前の入力をうながして、  JavaScript関数が HTMLボタンクリックに対応する C# Action を呼びます。

HybridWebViewPage　は 以下のようなアクションを登録してJavascriptから呼び出されるようにします。

~~~csharp

public partial class HybridWebViewPage : ContentPage
{
  public HybridWebViewPage ()
  {
    ...
    hybridWebView.RegisterAction (
      data => DisplayAlert ("Alert", "Hello " + data, "OK"));
  }
}
~~~

このアクションは [Xamarin.Forms.Page.DisplayAlert](https://developer.xamarin.com/api/member/Xamarin.Forms.Page.DisplayAlert/p/System.String/System.String/System.String/) メソッドをコールして、 モーダルのポップアップを表示し、HTMLページに入力された名前を表示します。

カスタムレンダラがかくアプリケーションプロジェクトで、プラットフォームごとのWebコントロールを改良して、 C#コードが Javascriptから呼ばれるようにします。

## カスタムレンダラの作成

手順:

1. `ViewRenderer<T1,T2>` クラスのサブクラスを作成。 これがカスタムコントロールをレンダします。 `T1` が HybridWebViewになります。 `T2` が、 ネイティブコントロールでカスタムビューを実装します。

2. `OnElementChanged` メソッドをオーバーライドします。これはカスタムコントロールをレンダして、 カスタマイズするロジックを実装します。 このメソッドが、 対応するXamarin.Formsカスタムコントロールが生成されたときに呼ばれます。


3. `ExportRenderer` 属性を追加します。 これは Xamarin.Formsカスタムコントロールをレンダするために使います。 Xamarin.Formsにカスタムレンダラを登録する時に使われます。

:

  ほとんどのXamarin.Formsエレメントでは、 カスタムレンダラを用意するのはオプションです。
  カスタムレンダラが登録されないならば、デフォルトのレンダラが使われます。
  ただし、 [Xamarin.Forms.View ](https://developer.xamarin.com/api/type/Xamarin.Forms.View/)をレンダリングするには必須です。


以下の図で、 サンプルでの責任範囲を説明しています。


![](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/hybridwebview/Images/solution-structure.png)


The HybridWebView custom control is rendered by platform-specific renderer classes, which all derive from the ViewRenderer class for each platform. This results in each HybridWebView custom control being rendered with platform-specific web controls, as shown in the following screenshots:



![](https://developer.xamarin.com/guides/xamarin-forms/custom-renderer/hybridwebview/Images/screenshots.png)


The ViewRenderer class exposes the OnElementChanged method, which is called when the Xamarin.Forms custom control is created in order to render the corresponding native web control. This method takes an ElementChangedEventArgs parameter that contains OldElement and NewElement properties. These properties represent the Xamarin.Forms element that the renderer was attached to, and the Xamarin.Forms element that the renderer is attached to, respectively. In the sample application the OldElement property will be null and the NewElement property will contain a reference to the HybridWebView instance.

An overridden version of the OnElementChanged method, in each platform-specific renderer class, is the place to perform the native web control instantiation and customization. The SetNativeControl method should be used to instantiate the native web control, and this method will also assign the control reference to the Control property. In addition, a reference to the Xamarin.Forms control that's being rendered can be obtained through the Element property.


In some circumstances the OnElementChanged method can be called multiple times, and so care must be taken when instantiating a new native control in order to prevent memory leaks. The approach to use when instantiating a new native control in a custom renderer is shown in the following code example:


~~~csharp
protected override void OnElementChanged (ElementChangedEventArgs<NativeListView> e)
{
  base.OnElementChanged (e);

  if (Control == null) {
    // Instantiate the native control and assign it to the Control property with
    // the SetNativeControl method
  }

  if (e.OldElement != null) {
    // Unsubscribe from event handlers and cleanup any resources
  }

  if (e.NewElement != null) {
    // Configure the control and subscribe to event handlers
  }
}
~~~

A new native control should only be instantiated once, when the Control property is null. The control should only be configured and event handlers subscribed to when the custom renderer is attached to a new Xamarin.Forms element. Similarly, any event handlers that were subscribed to should only be unsubscribed from when the element the renderer is attached to changes. Adopting this approach will help to create a performant custom renderer that doesn't suffer from memory leaks.


Each custom renderer class is decorated with an ExportRenderer attribute that registers the renderer with Xamarin.Forms. The attribute takes two parameters – the type name of the Xamarin.Forms custom control being rendered, and the type name of the custom renderer. The assembly prefix to the attribute specifies that the attribute applies to the entire assembly.

The following sections discuss the structure of the web page loaded by each native web control, the process for invoking C# from JavaScript, and the implementation of this in each platform-specific custom renderer class.


## Webページ作成

The following code example shows the web page that will be displayed by the HybridWebView custom control:

~~~html
<html>
  <body>
  <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>

  <h1>HybridWebView Test</h1>

  <br/> Enter name: <input type="text" id="name"> <br/> <br/>

  <button type="button" onclick="javascript:invokeCSCode($('#name').val());">Invoke C# Code</button> <br/>

  <p id="result">Result:</p>

  <script type="text/javascript">
  function log(str)
  {
      $('#result').text($('#result').text() + " " + str);
  }

  function invokeCSCode(data) {
      try {
          log("Sending Data:" + data);
          invokeCSharpAction(data);
      }
      catch (err){
          log(err);
      }
  }
  </script>
  </body>
</html>
~~~

The web page allows a user to enter their name in an input element, and provides a button element that will invoke C# code when clicked. The process for achieving this is as follows:


- When the user clicks on the button element, the invokeCSCode JavaScript function is called, with the value of the input element being passed to the function.

- The invokeCSCode function calls the log function in order to display the data it is sending to the C# Action. It then calls the invokeCSharpAction method to invoke the C# Action, passing the parameter received from the input element.

The invokeCSharpAction JavaScript function is not defined in the web page, and will be injected into it by each custom renderer.

## JavascriptからC#コードを呼び出す

The process for invoking C# from JavaScript is identical on each platform:


- The custom renderer creates a native web control and loads the HTML file specified by the HybridWebView.Uri property.
- Once the web page is loaded, the custom renderer injects the invokeCSharpAction JavaScript function into the web page.
- When the user enters their name and clicks on the HTML button element, the invokeCSCode function is invoked, which in turn invokes the invokeCSharpAction function.
- The invokeCSharpAction function invokes a method in the custom renderer, which in turn invokes the HybridWebView.InvokeAction method.
- The HybridWebView.InvokeAction method invokes the registered Action.

The following sections will discuss how this process is implemented on each platform.


## iOSでのカスタムレンダラ

The following code example shows the custom renderer for the iOS platform:


~~~csharp

[assembly: ExportRenderer (typeof(HybridWebView), typeof(HybridWebViewRenderer))]
namespace CustomRenderer.iOS
{
    public class HybridWebViewRenderer : ViewRenderer<HybridWebView, WKWebView>, IWKScriptMessageHandler
    {
        const string JavaScriptFunction = "function invokeCSharpAction(data){window.webkit.messageHandlers.invokeAction.postMessage(data);}";
        WKUserContentController userController;

        protected override void OnElementChanged (ElementChangedEventArgs<HybridWebView> e)
        {
            base.OnElementChanged (e);

            if (Control == null) {
                userController = new WKUserContentController ();
                var script = new WKUserScript (new NSString (JavaScriptFunction), WKUserScriptInjectionTime.AtDocumentEnd, false);
                userController.AddUserScript (script);
                userController.AddScriptMessageHandler (this, "invokeAction");

                var config = new WKWebViewConfiguration { UserContentController = userController };
                var webView = new WKWebView (Frame, config);
                SetNativeControl (webView);
            }
            if (e.OldElement != null) {
                userController.RemoveAllUserScripts ();
                userController.RemoveScriptMessageHandler ("invokeAction");
                var hybridWebView = e.OldElement as HybridWebView;
                hybridWebView.Cleanup ();
            }
            if (e.NewElement != null) {
                string fileName = Path.Combine (NSBundle.MainBundle.BundlePath, string.Format ("Content/{0}", Element.Uri));
                Control.LoadRequest (new NSUrlRequest (new NSUrl (fileName, false)));
            }
        }

        public void DidReceiveScriptMessage (WKUserContentController userContentController, WKScriptMessage message)
        {
            Element.InvokeAction (message.Body.ToString ());
        }
    }
}

~~~

The HybridWebViewRenderer class loads the web page specified in the HybridWebView.Uri property into a native WKWebView control, and the invokeCSharpAction JavaScript function is injected into the web page. Once the user enters their name and clicks the HTML button element, the invokeCSharpAction JavaScript function is executed, with the DidReceiveScriptMessage method being called after a message is received from the web page. In turn, this method invokes the HybridWebView.InvokeAction method, which will invoke the registered action in order to display the pop-up.

This functionality is achieved as follows:


Provided that the Control property is null, the following operations are carried out:

- A WKUserContentController instance is created, which allows posting messages and injecting user scripts into a web page.
- A WKUserScript instance is created in order to inject the invokeCSharpAction JavaScript function into the web page after the web page is loaded.
- The WKUserContentController.AddScript method adds the WKUserScript instance to the content controller.
- The WKUserContentController.AddScriptMessageHandler method adds a script message handler named invokeAction to the WKUserContentController instance, which will cause the JavaScript function window.webkit.messageHandlers.invokeAction.postMessage(data) to be defined in all frames in all web views that will use the WKUserContentController instance.
- A WKWebViewConfiguration instance is created, with the WKUserContentController instance being set as the content controller.
- A WKWebView control is instantiated, and the SetNativeControl method is called to assign a reference to the WKWebView control to the Control property.


Provided that the custom renderer is attached to a new Xamarin.Forms element:

- The WKWebView.LoadRequest method loads the HTML file that's specified by the HybridWebView.Uri property. The code specifies that the file is stored in the Content folder of the project. Once the web page is displayed, the invokeCSharpAction JavaScript function will be injected into the web page.


When the element the renderer is attached to changes:

- Resources are released.

::

  The WKWebView class is only supported in iOS 8 and later.


## Android のカスタムレンダラ

The following code example shows the custom renderer for the Android platform:


~~~csharp

[assembly: ExportRenderer (typeof(HybridWebView), typeof(HybridWebViewRenderer))]
namespace CustomRenderer.Droid
{
    public class HybridWebViewRenderer : ViewRenderer<HybridWebView, Android.Webkit.WebView>
    {
        const string JavaScriptFunction = "function invokeCSharpAction(data){jsBridge.invokeAction(data);}";

        protected override void OnElementChanged (ElementChangedEventArgs<HybridWebView> e)
        {
            base.OnElementChanged (e);

            if (Control == null) {
                var webView = new Android.Webkit.WebView (Forms.Context);
                webView.Settings.JavaScriptEnabled = true;
                SetNativeControl (webView);
            }
            if (e.OldElement != null) {
                Control.RemoveJavascriptInterface ("jsBridge");
                var hybridWebView = e.OldElement as HybridWebView;
                hybridWebView.Cleanup ();
            }
            if (e.NewElement != null) {
                Control.AddJavascriptInterface (new JSBridge (this), "jsBridge");
                Control.LoadUrl (string.Format ("file:///android_asset/Content/{0}", Element.Uri));
                InjectJS (JavaScriptFunction);
            }
        }

        void InjectJS (string script)
        {
            if (Control != null) {
                Control.LoadUrl (string.Format ("javascript: {0}", script));
            }
        }
    }
}
~~~

The HybridWebViewRenderer class loads the web page specified in the HybridWebView.Uri property into a native WebView control, and the invokeCSharpAction JavaScript function is injected into the web page, after the web page has loaded, with the InjectJS method. Once the user enters their name and clicks the HTML button element, the invokeCSharpAction JavaScript function is executed. This functionality is achieved as follows:



Provided that the Control property is null, the following operations are carried out:

- A native WebView instance is created, and JavaScript is enabled in the control.
- The SetNativeControl method is called to assign a reference to the native WebView control to the Control property.


Provided that the custom renderer is attached to a new Xamarin.Forms element:

- The WebView.AddJavascriptInterface method injects a new JSBridge instance into the main frame of the WebView's JavaScript context, naming it jsBridge. This allows methods in the JSBridge class to be accessed from JavaScript.
- The WebView.LoadUrl method loads the HTML file that's specified by the HybridWebView.Uri property. The code specifies that the file is stored in the Content folder of the project.
- The InjectJS method is invoked in order to inject the invokeCSharpAction JavaScript function into the web page.

When the element the renderer is attached to changes:

- Resources are released.


When the invokeCSharpAction JavaScript function is executed, it in turn invokes the JSBridge.InvokeAction method, which is shown in the following code example:


~~~csharp
public class JSBridge : Java.Lang.Object
{
  readonly WeakReference<HybridWebViewRenderer> hybridWebViewRenderer;

  public JSBridge (HybridWebViewRenderer hybridRenderer)
  {
    hybridWebViewRenderer = new WeakReference <HybridWebViewRenderer> (hybridRenderer);
  }

  [JavascriptInterface]
  [Export ("invokeAction")]
  public void InvokeAction (string data)
  {
    HybridWebViewRenderer hybridRenderer;

    if (hybridWebViewRenderer != null && hybridWebViewRenderer.TryGetTarget (out hybridRenderer)) {
      hybridRenderer.Element.InvokeAction (data);
    }
  }
}

~~~

The class must derive from Java.Lang.Object, and methods that are exposed to JavaScript must be decorated with the [JavascriptInterface] and [Export] attributes. Therefore, when the invokeCSharpAction JavaScript function is injected into the web page and is executed, it will call the JSBridge.InvokeAction method due to being decorated with the [JavascriptInterface] and [Export("invokeAction")] attributes. In turn, the InvokeAction method invokes the HybridWebView.InvokeAction method, which will invoked the registered action in order to display the pop-up.

::

  Projects that use the [Export] attribute must include a reference to Mono.Android.Export, or a compiler error will result.

## Summary

This article has demonstrated how to create a custom renderer for a HybridWebView custom control, that demonstrates how to enhance the platform-specific web controls to allow C# code to be invoked from JavaScript.
