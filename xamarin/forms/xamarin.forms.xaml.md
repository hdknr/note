- [Part 2. Essential XAML Syntax](https://developer.xamarin.com/guides/xamarin-forms/user-interface/xaml-basics/essential_xaml_syntax/)
- [Part 4. Data Binding Basics](https://developer.xamarin.com/guides/xamarin-forms/user-interface/xaml-basics/data_binding_basics/)
- [Xamarin で ReactiveUI を使ってみた](http://www.slideshare.net/amay077/xamarin-reactive-ui)
- [runceel/ReactiveProperty](https://github.com/runceel/ReactiveProperty)
- [ReactiveProperty オーバービュー](http://blog.okazuki.jp/entry/2014/05/07/014133)



## INotifyPropertyChanged

- [INotifyPropertyChangedを実装する](http://qiita.com/Temarin_PITA/items/2d2a86d14f15ba078570)
- [INotifyPropertyChangedを実装する(2)](http://qiita.com/Temarin_PITA/items/94163bf11d3b98ac21cc)
- [INotifyPropertyChanged実装のありえない面倒くささと、ReactivePropertyの信じられない素晴らしさ](http://qiita.com/ledsun/items/6f4ef754e5ae2507e531)
- [方法 : INotifyPropertyChanged インターフェイスを実装する](https://msdn.microsoft.com/ja-jp/library/ms229614(v=vs.110).aspx)
- [Xamarin.Forms と ReactiveProperty で快適MVVM生活](http://qiita.com/amay077/items/9ee28c18ff9fc519ae58)



## Binding

### 1. WebView にURLを渡す

- HomePage.xaml

~~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
	xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
	x:Class="XmWeb.HomePage">

	<ContentPage.Content>
		<StackLayout Orientation="Vertical">
            <WebView
            	Source="{Binding Url}"
            	x:Name="MainView" HeightRequest="800"/>
        </StackLayout>
	</ContentPage.Content>
</ContentPage>
~~~

- HomePage.xaml.cs

~~~csharp
using System;
using System.Collections.Generic;
using Xamarin.Forms;

namespace XmWeb
{
	public partial class HomePage : ContentPage
	{
		public HomePage ()
		{
			InitializeComponent ();

			this.BindingContext = new ViewModel {
				Url = "https://www.apple.com"
			};

		}


		public class ViewModel
		{
			public string Url { get; set; }
		}
	}
}
~~~

### 2. コメント入力を受け取る

- ビューモデルにCommentを拡張 (HomePage.xaml.cs )

~~~csharp
using System.Linq;
using Reactive.Bindings;
using System.Runtime;
~~~

~~~csharp
public class ViewModel
{
  public string Url { get; set; }

  public ReactiveProperty<string> Comment {get;private set; }
  = new ReactiveProperty<string>("");

  public ViewModel()
  {
    this.Comment.Value = "...";
    this.Comment.Subscribe( s =>{
      System.Diagnostics.Debug.WriteLine($"{Url}: Command: {s}");
    });
  }
}
~~~

- xamlにEdit を追加

~~~xml
<Editor Text="{Binding Comment.Value}" />
~~~
