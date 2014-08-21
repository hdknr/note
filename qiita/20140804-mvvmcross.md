MvvmCross: 簡単な例

[MvvmCross TipCalc](http://www.codeproject.com/Articles/566270/MvvmCross-TipCalc-Step-Creati) を Xamarin 5.1.4 で動かしてみる


# TipCalc.Core の作成


## 空のソリューションに PCLプロジェクト追加

![image](https://lh6.googleusercontent.com/-xwqly0xRVAU/U97kyt9obKI/AAAAAAAAAoI/_lW8P5irK8Y/w818-h494-no/3.png)

## MvvmCross Hot Tuna Starter Pack

追加前

```bash

    TipCalc.Core/
    ├── MyClass.cs
    ├── Properties
    │   └── AssemblyInfo.cs
    ├── TipCalc.Core.csproj
    ├── bin
    │   └── Debug
    └── obj
        └── Debug
```
    

![image](https://lh6.googleusercontent.com/-rXAnXupNYDY/U97kzNNxJ6I/AAAAAAAAAn0/z_nDTE1Eczk/w817-h542-no/5.png)

追加後

```bash

    TipCalc.Core/
    ├── App.cs
    ├── MyClass.cs
    ├── Properties
    │   └── AssemblyInfo.cs
    ├── TipCalc.Core.csproj
    ├── ToDo-MvvmCross
    │   └── _\ Core.txt
    ├── ViewModels
    │   └── FirstViewModel.cs
    ├── bin
    │   └── Debug
    ├── obj
    │   └── Debug
    └── packages.config
    
```


## Service(Model)インターフェースとクラス実装

* Serviceフォルダを追加
 
### ICalculationインターフェース定義

```csharp

    using System;
    
    namespace TipCalc.Core
    {
    	public interface ICalculation
    	{
    		double TipAmount(double subTotal, int generosity);
    	}
    }
    
```


### Caluculationクラス定義

```csharp

    using System;
    
    namespace TipCalc.Core
    {
    	public class Calculation : ICalculation
    	{
    		public double TipAmount(double subTotal, int generosity)
    		{
    			return subTotal * ((double)generosity)/100.0;
    		}
    	}
    }
```
    

## ViewModelの実装

* ViewModel == UI機能がないアプリケーション
* ViewModels/FirstViewModel.cs が追加されているのでこれをリファクタリング
* Start()で開始
* 変数はPropertyでアクセス可能
* 変更通知が必要が変数は、setの中でRecalcuate（）でUIに通知する

こんな

```csharp

    using Cirrious.MvvmCross.ViewModels;
    
    namespace TipCalc.Core.ViewModels
    {
        public class TipViewModel 
    		: MvxViewModel
        {
    		/// <summary>
    		/// ICalculation Container
    		/// </summary>
    		private readonly ICalculation _calculation;
    
    		public TipViewModel(ICalculation calculation)
    		{
    			_calculation = calculation;
    		}
    
    
    		/// <summary>
    		/// Start this instance with some initial values.
    		/// </summary>
    		public override void Start()
    		{
    			_subTotal = 100;
    			_generosity = 10;
    			Recalcuate();
    			base.Start();
    		}
    
    		/// <summary>
    		/// Recalcuate the Tip
    		/// </summary>
    		private void Recalcuate()
    		{
    			Tip = _calculation.TipAmount(SubTotal, Generosity);
    		}    
    
    
    		// Values are exposed thru "Property"
    		// If a Property value was changed, 
    		// a event is fired thru "RaisePropertyChange".
    
    
    		private double _subTotal;
    		public double SubTotal
    		{
    			get { return _subTotal; }
    			set { 
    				_subTotal = value; 
    				RaisePropertyChanged(() => SubTotal); 
    				Recalcuate(); 
    			}
    		}
    
    		private int _generosity;
    		public int Generosity
    		{
    			get { return _generosity; }
    			set { 
    				_generosity = value; 
    				RaisePropertyChanged(() => Generosity); 
    				Recalcuate(); 
    			}
    		}
    
    		private double _tip;
    		public double Tip
    		{
    			get { return _tip; }
    			set { 
    				_tip = value; 
    				RaisePropertyChanged(() => Tip);
    			}
    		}
    	}
    }
    
```


## App の実装

* App.csが追加されているので、これを編集

こんな

```csharp

    using Cirrious.CrossCore.IoC;
    using Cirrious.CrossCore;
    
    namespace TipCalc.Core
    {
        public class App : Cirrious.MvvmCross.ViewModels.MvxApplication
        {
            public override void Initialize()
            {	
                CreatableTypes()
                    .EndingWith("Service")
                    .AsInterfaces()
                    .RegisterAsLazySingleton();
    				
    			RegisterAppStart<ViewModels.TipViewModel>();
    
    			// ICaliculationのクラスを登録
    			// TipViewModelのコンストラクタに必要なクラスを登録することで
    			// 自動的にクラスを見つけてコンストラクタに渡してくれる
    			Mvx.RegisterType<TipCalc.Core.ICalculation,TipCalc.Core.Calculation> ();					
    
            }
        }
    }

```

# TipCalc.iOS の作成


## iPhone Single View Application プロジェクト作成

![image](https://lh3.googleusercontent.com/-4WL_pA7LWMY/U97kwx-L5AI/AAAAAAAAAnM/0ia5FFt1nt0/w818-h497-no/11.png)


## MvvmCross Hot Tuna Starter Pack

* TipCalc.Coreと同様

追加前

```bash
    TipCalc.iOS/
    ├── AppDelegate.cs
    ├── Entitlements.plist
    ├── Info.plist
    ├── Main.cs
    ├── MainStoryboard.storyboard
    ├── Resources
    │   └── Default-568h@2x.png
    ├── TipCalc.iOS.csproj
    ├── TipCalc.iOSViewController.cs
    └── TipCalc.iOSViewController.designer.cs
```    


![image](https://lh3.googleusercontent.com/-81I332SzStM/U97kxuQIJNI/AAAAAAAAAoQ/hwpGZCO3VGQ/w818-h541-no/13.png)


ファイルが追加

```bash

    TipCalc.iOS/
    ├── AppDelegate.cs
    ├── AppDelegate.cs.txt
    ├── DebugTrace.cs
    ├── Entitlements.plist
    ├── Info.plist
    ├── LinkerPleaseInclude.cs
    ├── Main.cs
    ├── MainStoryboard.storyboard
    ├── Resources
    │   └── Default-568h@2x.png
    ├── Setup.cs
    ├── TipCalc.iOS.csproj
    ├── TipCalc.iOSViewController.cs
    ├── TipCalc.iOSViewController.designer.cs
    ├── ToDo-MvvmCross
    │   └── _\ Touch\ UI.txt
    ├── Views
    │   └── FirstView.cs
    └── packages.config
    
```


## StoryboardでUIを設定(Outlet生成)

![image](https://lh3.googleusercontent.com/-eIIap_Gw_n0/U97kxbXYEMI/AAAAAAAAAoY/DIRN0Vi18jo/w381-h440-no/12.png)

保存するとOutletがUIViewControllerのコードビハインドに生成されます。


```csharp
 
    namespace TipCalc.iOS
    {
    	[Register ("TipCalc_iOSViewController")]
    	partial class TipCalc_iOSViewController
    	{
    		[Outlet]
    		[GeneratedCode ("iOS Designer", "1.0")]
    		UISlider Generosity { get; set; }
    
    		[Outlet]
    		[GeneratedCode ("iOS Designer", "1.0")]
    		UITextField SubTotal { get; set; }
    
    		[Outlet]
    		[GeneratedCode ("iOS Designer", "1.0")]
    		UILabel Tip { get; set; }
    }
    

## UIViewControllerを修正してViewModelの通知を受け取る


* ベースクラスを UIViewController -> MvxViewController
* ViewDidLoadでOutletにViewModelの通知を反映させるように紐づける


```csharp

    using System;
    using System.Drawing;
    
    using MonoTouch.Foundation;
    using MonoTouch.UIKit;
    
    using TipCalc.Core.ViewModels;
    
    using Cirrious.MvvmCross.Binding.BindingContext;
    using Cirrious.MvvmCross.Touch.Views;
    using Cirrious.MvvmCross.ViewModels;
    
    namespace TipCalc.iOS
    {
    	public partial class TipCalc_iOSViewController : MvxViewController
    	{
    		public TipCalc_iOSViewController (IntPtr handle) : base (handle)
    		{
    		}
    
    		public override void ViewDidLoad ()
    		{
    			this.Request = new MvxViewModelRequest<TipViewModel>(
    				null, null, new MvxRequestedBy());
    				
    			base.ViewDidLoad();
                
                // ViewModelのデータ変更通知を受け取るので表示が変わる
    			this.CreateBinding(this.Generosity).To<TipViewModel>(vm => vm.Generosity).Apply();
    			this.CreateBinding(this.Tip).To<TipViewModel>(vm => vm.Tip).Apply();
    			this.CreateBinding(this.SubTotal).To<TipViewModel>(vm => vm.SubTotal).Apply();
    
    			// Perform any additional setup after loading the view, typically from a nib.
    		}
    	}
    }
```
    


## Setup クラスを追加して、ViewModelの設定を行う

* Tot Tunaが生成してくれる

```csharp

    using MonoTouch.UIKit;
    using Cirrious.CrossCore;
    using Cirrious.CrossCore.Platform;
    using Cirrious.MvvmCross.ViewModels;
    using Cirrious.MvvmCross.Touch.Platform;
    
    namespace TipCalc.iOS
    {
    	public class Setup : MvxTouchSetup
    	{
    		public Setup(MvxApplicationDelegate applicationDelegate, UIWindow window)
                : base(applicationDelegate, window)
    		{
    		}
    
    		protected override IMvxApplication CreateApp ()
    		{
    			return new Core.App();
    		}
    		
            protected override IMvxTrace CreateDebugTrace()
            {
                return new DebugTrace();
            }
    	}
    }
```

## AppDelegateを修正してSetupの実行

*　ベースクラスを UIApplicationDelegate -> MvxApplicationDelegate
* FinishedLaunchingをオーバーライドしてSetup実行


```csharp

    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    using MonoTouch.Foundation;
    using MonoTouch.UIKit;
    
    using TipCalc.Core.ViewModels;
    
    using Cirrious.CrossCore;
    using Cirrious.MvvmCross.Binding.BindingContext;
    using Cirrious.MvvmCross.Touch.Views;
    using Cirrious.MvvmCross.Touch.Platform;
    using Cirrious.MvvmCross.ViewModels;
    
    namespace TipCalc.iOS
    {
    	// The UIApplicationDelegate for the application. This class is responsible for launching the
    	// User Interface of the application, as well as listening (and optionally responding) to
    	// application events from iOS.
    
    	[Register ("AppDelegate")]
    	public partial class AppDelegate :	MvxApplicationDelegate
    	{
  
    		public override bool FinishedLaunching (UIApplication app, NSDictionary options)
    		{
    			//base.FinishedLaunching を呼び出してはいけない。
    			var setup = new Setup(this, this.Window);
    			setup.Initialize();
    
    			return true;
    		}
    
    	}
    }
```

# モデル/サービスを外部から与える

* 例えば、ICalculationの実装が別のPCLに定義されているとか
* iOS UIアプリ側から与えたい場合は、Setupを修正

InitializeFirstChanceでコンストラクタに使われるタイプを登録する:

```csharp

    using MonoTouch.UIKit;
    using Cirrious.CrossCore;
    using Cirrious.CrossCore.Platform;
    using Cirrious.MvvmCross.ViewModels;
    using Cirrious.MvvmCross.Touch.Platform;
    
    namespace TipCalc.iOS
    {
    	public class Setup : MvxTouchSetup
    	{
    		public Setup(MvxApplicationDelegate applicationDelegate, UIWindow window)
                : base(applicationDelegate, window)
    		{
    		}
    		protected override void InitializeFirstChance ()
    		{
    			base.InitializeFirstChance ();
                Mvx.RegisterType<TipCalc.Core.ICalculation,TipCalc.Core.Calculation> ();
    		}
    	}
    }
 
```
