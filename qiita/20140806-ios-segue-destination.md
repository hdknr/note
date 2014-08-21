Storyboard: Segueの遷移先のウィンドウに値を渡したりする

[Unwindサンプルの写経](https://www.evernote.com/shard/s302/sh/b31731b5-dafb-453e-883b-25d1437697aa/0899b4062121d1a527bb5238f0c24d7c)のカスタマイズ

YellowViewControllerがRootで、“Go To Pink”ボタンをタッチすると、PinkViewControllerに遷移するので、その間になんかしたい。

# Destination(Pink)の修正

- プロパティを作成して、値を渡せるようにする
- ViewDidLoad()をオーバーライドして、画面表示する際に値をUIに反映


こんな:

```csharp

	partial class PinkViewController : UIViewController
	{

		public DateTime CurrentTime {
			get;
			set;
		}

		public override void ViewDidLoad ()
		{
			base.ViewDidLoad ();

			this.CurrentTimeLabel.Text =
				CurrentTime.ToLongDateString()+ " " + CurrentTime.ToLongTimeString ();
		}
	}
```

# Source(Yellow)の修正

- PrepareForSegueをオーバーライド
- セグエのDestinationViewControllerを目的のコントローラにリゾルブ(ここでは単純にキャスト)
- コントローラに値を渡す


GoToLinkボタンのタッチハンドラもいれてます。

```csharp

	partial class YellowViewController : UIViewController
	{

		partial void GoToPink_TouchUpInside (UIButton sender)
		{
			Console.WriteLine("**** going to Pink from Yellow");
		}

		public override void PrepareForSegue (UIStoryboardSegue segue, NSObject sender)
		{
			base.PrepareForSegue (segue, sender);

			var pink = (PinkViewController)segue.DestinationViewController;
			pink.CurrentTime = DateTime.Now;
		}
	}
```

呼ばれ順は
    
1. GoToPink_TouchUpInside  : ボタンをタッチした処理を実装する
2. PrepareForSegue : 画面遷移が用意できたときに、遷移先の画面をごにょる (この時点では遷移先のUIがウィンドウシステムに作成されていないので注意)
3. PerformSegue : Storyboardで紐づけた先の画面に遷移する (勝手によばれる)
