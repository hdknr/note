Android Activity

## 終了

### Finish

- [Android.App.Activity.Finish ](https://developer.xamarin.com/api/member/Android.App.Activity.Finish/)
- [finishActivity](https://developer.android.com/reference/android/app/Activity.html#finish())
- アクティビティをアプリケーションから閉じる時に明示的に呼ぶ
- ActivityResult が起動元に送信される(onActivityResult)

~~~csharp

protected override void OnCreate (Bundle savedInstanceState)
{
	base.OnCreate (savedInstanceState);
	Window.RequestFeature (WindowFeatures.NoTitle);

	// Create your application here
	// 停止ボタンのハンドラ
	StopButton.Click += OnStopping;
}

public void OnStopping (object sender, EventArgs e)
{
  // アクティビティを終了します。これにより OnDestoryがコールバックされます。
  Finish ();
}

/// Activity解放
/// 端末のHistory Back ボタンが押されると、直接 OnDestroyされます
protected override void OnDestroy ()
{
  CloseActivityTask();      /// 業務処理の停止

  base.OnDestroy ();
  Dispose ();
}
~~~
