# Razor with Xamarin

- [Building HTML views using Razor Templates](https://docs.xamarin.com/guides/cross-platform/advanced/razor_html_templates/)
- [xamarin/PortableRazor](https://github.com/xamarin/PortableRazor)

## データタイプ

~~~~csharp

public class TimetableViewData {
  public string Color {get;set; }
  public string FirstTrain {get;set; }
  public string LastTrain {get;set; }
  public string Timetable {get;set; }
};
~~~~

## テンプレート

- "追加 > 新しいファイル > Preprocessed Razor Template" で作成
- 編集保存するとコードビハインド(*.cs)が作成されます
- "@model タイプ" でコンテキストデータクラスをネゴシーエトします
- @{ WriteLiteral( ...);}  でRaw HTML を書き込みます

~~~html
@model TimetableViewData

<html>
<head>
  <meta charset="utf-8">
  <style>
    // style....
  </style>
</head>

<body>

<table><tr>
<td style="color:white; background-color: @Model.Color;">始発</td><td>@Model.FirstTrain</td>
<td style="color:white; background-color: @Model.Color;">最終</td><td>@Model.LastTrain</td>
</tr></table>
<table>
 <thead>
   <tr>
     <th >時</th>
     <th colspan='9'>分</th>
 	</tr>
 </thead>

 <tbody class="tt">
 @{WriteLiteral(Model.Timetable);}
 </tbody>

</table>
</body>
</html>
~~~


## レンダリング

~~~
void RenderHtml(
    string color, string
    first_train,
    string last_train,
    string timetable_html)
{
  var data = new TimetableViewData {
    Color = color,
    FirstTrain= first_train,
    LastTrain= last_train,
    Timetable = timetable_html
  };

  // TimetableTemplate.cshtml
  var template = new TimetableTemplate {Model =data};

  string contentDirectoryPath =
    System.IO.Path.Combine (NSBundle.MainBundle.BundlePath, "");

  //WebView
  TimeTable.LoadHtmlString(
    template.GenerateString()
    ,new NSUrl(contentDirectoryPath, true));

}
~~~
