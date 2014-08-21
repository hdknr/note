ZXing.Net.Mobile:iOS: QRコードを作成してみる

- Xamarin + Storyboard勉強中


# iPhone の Single View Application #

- 新規で QrCoderを作ってみる。

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/e878e32a-03cf-4c71-901d-7850762cb340/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.40.40.png?resizeSmall&width=600)

- Bundle Identifier を登録した物に変更

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/bfe00b41-1942-4d20-91f5-7028ab72caa0/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.41.29.png?resizeSmall&width=600)


# Navigation Controlerの Rootビューにする #
- ストーリーボード(MainStoryboard.storyboard)を開く

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/25f60ae3-4ad1-4663-ab0e-598cee433535/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.46.15.png?resizeSmall&width=500)

- Toolboxで Navigation Controler を選択


![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/32ed5dda-c7f4-433e-b407-eb66d41c8b5b/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.55.43.png?resizeSmall&width=300)

- Navigation Controllerをストーリーボードにドラッグ&ドロップ

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/8670507b-5c7c-46ab-95c3-182fa7466d52/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.57.23.png?resizeSmall&width=500)

- 最初に作られたビュー（QrCoderViewControllerクラス)からイニシャルビューのハンドルをドラッグして、Navigation Controllerにドロップする(Navigation ControllerがInitial View Controller)
- Navigation Controllerを Control + クリックして、そのままQrCoderViewControllerにドロップし、QrCoderViewControllerをRootとする


![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/3bde331f-0f78-45df-a677-9161f81cb8c3/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.57.51.png?resizeSmall&width=600)

- Navigation Controllerを追加した時に一緒について来たViewは削除

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/d4713a95-f99b-4ac2-af49-1c2b6b6c7759/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.58.10.png?resizeSmall&width=600)

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/00ee215d-a09d-4714-ae31-bc7a7aac467d/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.58.24.png?resizeSmall&width=400)


# QR コードを表示するビューを追加して遷移させる #

- ToolboxからView Controlerを選択して、ドロップ

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/44f7b70b-2bb5-4c65-81bc-94eddfb1f8d6/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.59.29.png?resizeSmall&width=300)

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/81acfaeb-555a-4078-b345-dbf2f40f31f4/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2010.59.43.png?resizeSmall&width=600)


- ToolboxからButtonを選択して、 Rootビューにドロップ
- Create QR Codeというラベルに変える

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/e39f23cc-61fe-41e3-b94f-2125deccfb65/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.00.13.png?resizeSmall&width=600)

- Buttonを Control+クリックして、そのまま追加したViewにドラッグする

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/4e169a72-a8e9-4178-832b-e9c53996dc34/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.00.23.png?resizeSmall&width=600)

- これでボタンをクリックするとビューに移るようになる
- このビューをCreateQrCodeContollerという名前にする

# QRコード表示画面 #

- ToolboxからImage View を選択して、追加したビューに落とす
- 同じく TookboxからButtonを選択して、Image Viewの下の方に落とす


![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/611e5bde-87a9-4b4a-9fc6-a21f6c8479ac/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.01.43.png?resizeSmall&width=300)

- Image Viewの名前をQrCodeImageに変える

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/79527de9-8263-40be-ba8e-f13147709c7a/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.10.16.png?resizeSmall&width=600)

- ButtonのラベルをCreate にし、名前を CreateButtonにする

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/11c9ee83-1abf-42db-af63-b9cb5ab62dfe/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.04.52.png?resizeSmall&width=600)




# ZXing.Net.Mobile 追加 #

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/ccf07ecf-57ea-4d86-963c-63b8031205d3/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.06.25.png?resizeSmall&width=600)

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/a7adf2d5-8e2d-4f76-8b7a-ded1b656c247/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.06.35.png?resizeSmall&width=300)


# QRコード作成ハンドラ作成 #

- CreateQrCodeControllerビューに追加した"Create"ボタンをダブルクリックする
- ハンドラコードを追加する場所を移動する

![image](https://www.evernote.com/shard/s302/sh/f5da988e-1c9c-412a-889d-33dbede9b194/65254e001dc1f39bfe18c444eaf66643/res/eaea50ba-6962-4d83-9a73-49193475e16f/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202014-06-29%2011.05.00.png?resizeSmall&width=600)

- Enterキーで確定

```csharp

    using System;
    using MonoTouch.Foundation;
    using MonoTouch.UIKit;
    using System.CodeDom.Compiler;
   
    namespace QrCoder
    {
        partial class CreateQrCodeController : UIViewController
        {
            public CreateQrCodeController (IntPtr handle) : base (handle)
            {
            }
   
   
            partial void CreateButton_TouchUpInside (UIButton sender)
            {
                throw new NotImplementedException (); 
            }
   
        }
    }

```

- ちなみにコードビハインド(CreateQrCodeController.designer.cs)は自動的に以下のように編集されている

```csharp

    using System;
    using MonoTouch.Foundation;
    using MonoTouch.UIKit;
    using System.CodeDom.Compiler;

    namespace QrCoder
    {
        [Register ("CreateQrCodeController")]
        partial class CreateQrCodeController
        {
            [Outlet]
            [GeneratedCode ("iOS Designer", "1.0")]
            UIButton CreateButton { get; set; }
   
            [Outlet]
            [GeneratedCode ("iOS Designer", "1.0")]
            UIImageView QrCodeImage { get; set; }
   
            [Action ("CreateButton_TouchUpInside:")]
            [GeneratedCode ("iOS Designer", "1.0")]
            partial void CreateButton_TouchUpInside (UIButton sender);
   
            void ReleaseDesignerOutlets ()
            {
                if (CreateButton != null) {
                    CreateButton.Dispose ();
                    CreateButton = null;
                }
                if (QrCodeImage != null) {
                    QrCodeImage.Dispose ();
                    QrCodeImage = null;
                }
            }
        }
    }

```

- QRコード生成

```csharp

            partial void CreateButton_TouchUpInside (UIButton sender)
            {
   
                var writer = new ZXing.BarcodeWriter{
                    Format= ZXing.BarcodeFormat.QR_CODE,
                };
                var qrcode = writer.Write("Hello");
                QrCodeImage.Image = qrcode;
            }

```


