Xamarin: Button.Tagにオブジェクトをセットして１つのClickハンドラで処理する

## JavaObjectWrapper

- [How to convert a type to Java.lang.object](https://forums.xamarin.com/discussion/7894/how-to-convert-a-type-to-java-lang-object)

~~~csharp
public class JavaObjectWrapper<T> : Java.Lang.Object
{
  public T Obj { get; set; }
}
~~~

### GetTag<T>/SetTag<T> 拡張メソッド

~~~csharp
public static T GetTag<T>(this Android.Widget.Button button){
  return (button.Tag as JavaObjectWrapper<T>).Obj;
}
public static void SetTag<T>(this Android.Widget.Button button, T obj)
{
  button.Tag = new JavaObjectWrapper<T>{ Obj = obj };
}
~~~

## TableViewにテーブル ボタン

- Line オブジェクトをTagとしてセットする

~~~csharp

  // LineTable: cols列のTableView
  TableRow row = null;

  for (int i = 0; i < lines.Count (); i++) {
    var line = lines [i];

    if (i % cols == 0) {
      row = new TableRow (this){LayoutParameters =rowlayouts};
      LineTable.AddView (row);
    }

    var button = new Button (this);
    button.SetText (line.name, TextView.BufferType.Normal);
    button.SetTag<Line> (line);
    button.Click += OnLineButtonClicked;
    row.AddView (button, buttonlayout);
  }
}
~~~


## Clickハンドラ

- LineオブジェクトをTagから復元する

~~~csharp
void OnLineButtonClicked(object sender, EventArgs e) {
  var line = (sender as Button).GetTag<Line>();
  Console.WriteLine ("...... {0}", line.name);
}
~~~
