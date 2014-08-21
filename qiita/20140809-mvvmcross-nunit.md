MvvmCross: Xamarin Studio で NUnit

[TipCalc.Core](http://qiita.com/hidelafoglia/items/09452d50cb2cdfc4c91e)をテストする

# TipCalc.Unitの作成

![image](https://lh5.googleusercontent.com/-bOBDKS1kk48/U-W22wPcAVI/AAAAAAAAAuU/9UMEIllo1Js/w918-h555-no/Unit.1.png)

##  ターゲットフレームワーク変更(Mono/.NET4.5)

![image](https://lh5.googleusercontent.com/-LdGlMgSGnjs/U-W224KD69I/AAAAAAAAAuY/c9QWq_Vdvn8/w840-h556-no/Unit.2.png)

## MvvmCross Library追加

![image](https://lh6.googleusercontent.com/-oFkxEBoi8oo/U-W22-QwcmI/AAAAAAAAAuQ/nEUafST2EI8/w822-h545-no/Unit.3.png)


    TipCalc.Unit/
    ├── Test.cs
    ├── TipCalc.Unit.csproj
    └── packages.config
    
    0 directories, 3 files
    
# Cirrious.MvvmCross.Test.Core からコピる

- [ MvvmCross / Cirrious / Test / Cirrious.MvvmCross.Test.Core /](https://github.com/MvvmCross/MvvmCross/tree/v3/Cirrious/Test/Cirrious.MvvmCross.Test.Core)よりファイルをコピる

     - [MvxIoCSupportingTest.cs](https://github.com/MvvmCross/MvvmCross/blob/v3/Cirrious/Test/Cirrious.MvvmCross.Test.Core/MvxIoCSupportingTest.cs)
     - [TestTrace.cs](https://github.com/MvvmCross/MvvmCross/blob/v3/Cirrious/Test/Cirrious.MvvmCross.Test.Core/TestTrace.cs)
     

この時点でビルド確認:

    
    TipCalc.Unit/
    ├── MvvmCross
    │   ├── MvxIoCSupportingTest.cs
    │   └── TestTrace.cs
    ├── Test.cs
    ├── TipCalc.Unit.csproj
    ├── bin
    │   └── Debug
    │       ├── Cirrious.CrossCore.Wpf.dll
    │       ├── Cirrious.CrossCore.dll
    │       ├── Cirrious.MvvmCross.Localization.dll
    │       ├── Cirrious.MvvmCross.Wpf.dll
    │       ├── Cirrious.MvvmCross.dll
    │       ├── TipCalc.Unit.dll
    │       └── TipCalc.Unit.dll.mdb
    └── packages.config
   


# モックのディスパッチャーを用意する

メインスレッドの処理とビューモデルのナビゲーションを処理するためのモックのディスパッチャーを作る

```csharp

    // (c) Copyright Cirrious. http://www.cirrious.com
    // This source is subject to the Microsoft Public License (Ms-PL)
    // Please see license.txt on http://opensource.org/licenses/ms-pl.html
    // All other rights reserved.
    // </copyright>
    //  
    // Project Lead - Stuart Lodge, Cirrious. http://www.cirrious.com - Hire me - I'm worth it!
    
    using System;
    using System.Collections.Generic;
    using Cirrious.CrossCore.Core;
    using Cirrious.MvvmCross.ViewModels;
    using Cirrious.MvvmCross.Views;
    
    
    namespace TipCalc.Unit
    {
        // This Class is required for:
        // 1. MvvmCross UI thread marshalling  (IMvxMainThreadDispatcher)
        // 2. MvvmCross ViewModel navigation (IMvxViewDispatcher)
    
        public class MockMvxViewDispatcher : 
        MvxMainThreadDispatcher,        // IMvxMainThreadDispatcher 
        IMvxViewDispatcher
        {
            public List<IMvxViewModel> CloseRequests = new List<IMvxViewModel>();
            public List<MvxViewModelRequest> NavigateRequests = new List<MvxViewModelRequest>();
    
            // IMvxViewDispatcher#ShowViewModel
            public bool ShowViewModel(MvxViewModelRequest request)
            {
                NavigateRequests.Add(request);
                return true;
            }
    
            // IMvxViewDispatcher#ChangePresentation
            public bool ChangePresentation(MvxPresentationHint hint)
            {
                throw new NotImplementedException();
            }
    
            // IMvxMainThreadDispatcher#RequestMainThreadAction
            public bool RequestMainThreadAction(Action action)
            {
                action();
                return true;
            }
        }
    }
```


# テストのベースクラスを用意

- コピったCirrious.MvvmCross.Test.Core.MvxIoCSupportingTestをベースクラスにする
- CreateMockNavigationを実装

    - モックのディスパチャーを作成
    - メインスレッドとビューのディスパッチャインターフェースとして、つくったディスパッチャをシングルトン登録する


こんな
```csharp

    using System;
    using Cirrious.CrossCore.Core;
    using Cirrious.MvvmCross.Test.Core;
    using Cirrious.MvvmCross.Views;
    using NUnit.Framework;
   
   
    namespace TipCalc.Unit
    {  
        public class MvxTest : MvxIoCSupportingTest
        {  
            protected MockMvxViewDispatcher CreateMockNavigation()
            {  
                var dispatcher = new MockMvxViewDispatcher();  
                //XamarinMvx.Unit.MockMvxViewDispatcher
   
                Ioc.RegisterSingleton<IMvxMainThreadDispatcher>(dispatcher);
                Ioc.RegisterSingleton<IMvxViewDispatcher>(dispatcher);
   
                return dispatcher;
            }  
        }  
    }

プロジェクト

    TipCalc.Unit/
    ├── Mocs
    │   ├── MockMvxViewDispatcher.cs
    │   └── MvxTest.cs
    ├── MvvmCross
    │   ├── MvxIoCSupportingTest.cs
    │   └── TestTrace.cs
    ├── TipCalc.Unit.csproj
    ├── Test.cs
    ├── bin
    │   └── Debug
    │       ├── Cirrious.CrossCore.Wpf.dll
    │       ├── Cirrious.CrossCore.dll
    │       ├── Cirrious.MvvmCross.Localization.dll
    │       ├── Cirrious.MvvmCross.Wpf.dll
    │       ├── Cirrious.MvvmCross.dll
    │       ├── TipCalc.Unit.dll
    │       └── TipCalc.Unit.dll.mdb
    └── packages.config
    
    4 directories, 14 files

# TipCalc.CoreのUnitTestを作成
- Test.cs -> UnitTipViewModel.cs にリファクタ
- CreatAll()を読んでMvvmCrossの初期化
- CreateMockNavigationを読んで、モックのディスパッチャーを登録
- テスト対象のビューモデルを作る
- ビューモデルに対して、プロパティ変更通知を受け取るハンドラ登録
- テスト記述

こんな

```csharp

    using NUnit.Framework;
    using System;
    using Cirrious.MvvmCross.ViewModels;
    using Cirrious.CrossCore;
    
    namespace TipCalc.Unit
    {
        [TestFixture ()]
        public class UnitTipViewModel : MvxTest
    
        {
            [Test ()]
            public void TestCase ()
            {
                // 段取り
                ClearAll ();
                var mockNavigation = CreateMockNavigation ();
    
                // Calculation のタイプを登録                                
                Mvx.RegisterType<TipCalc.Core.ICalculation,TipCalc.Core.Calculation> (); 
                
                // テスト対象のビューモデル(TipViewModel)を生成   
                var vm = Mvx.IocConstruct<TipCalc.Core.ViewModels.TipViewModel> ();
                   
                int i = 0;
                
                // ハンドラ登録
                vm.PropertyChanged += (
                    object sender,
                    System.ComponentModel.PropertyChangedEventArgs e
                ) => {
                    var obj = sender as TipCalc.Core.ViewModels.TipViewModel;
    
                    var t = obj.Tip;
                    i = i + 1; 
    
                    if( e.PropertyName == "Tip" &&
                        vm.Generosity == 30 
                    )
                    {
                        Assert.AreEqual(obj.Tip, 300.0d );
                    }
                };
    
                vm.SubTotal = 1000.0;
                vm.Generosity = 30;
      
                Assert.AreEqual (i, 4);
    
            }
        }
    }
```
    
    

   

