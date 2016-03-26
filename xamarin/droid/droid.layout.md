## ２カラムレイアウト

- [Layout with 2 columns](http://stackoverflow.com/questions/10302604/layout-with-2-columns)

~~~xml
<LinearLayout android:orientation="horizontal">
  <LinearLayout />
  <LinearLayout />
</LinearLayout>
~~~

## テーブルレイアウト

- ２行のテーブル
- カラム数は cols

### 1. 行のレイアウト

2行なので、 Weight = 0.5f で TableRow のレイアウトパラメータを用意する
~~~csharp
var rowlayouts = new TableLayout.LayoutParams (
  TableLayout.LayoutParams.WrapContent,
  TableLayout.LayoutParams.WrapContent)
{ Weight = 0.5f };
~~~

### 2. カラムのレイアウト

- テーブル幅は画面と同じとして、幅を colsで割ったものとする。
- 高さは行に合わせる(MatchParent)
~~~csharp
Android.Graphics.Point size = new Android.Graphics.Point ();
			WindowManager.DefaultDisplay.GetSize ( size);
var collayout = new TableRow.LayoutParams(
  size.X / cols, TableRow.LayoutParams.MatchParent);
~~~

### 3. ボタンをはめていく

~~~csharp
TableRow row = null;

for (int i = 0; i < buttons.Count (); i++) {
  var button = buttons[i];

  if (i % cols == 0) {  // 改行
    row = null;
  }

  if (row == null) {
    // 行を追加する
    row = new TableRow (this);
    ButtonTable.AddView (row, rowlayouts);
  }

  var button = new Button (this);
  button.SetText (button.name_en, TextView.BufferType.Normal);
  row.AddView (button, collayout);
}
~~~

# サンプル

- https://github.com/hdknr/DroidLayout/blob/master/DroidLayout/ButtonTable.cs
