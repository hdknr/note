Xamarin: i18n Resource in PCL DLL

## PCL DLLに Properties/LibResource.res を作成

- ビルドアクション:  `EmbeddedResource` にする
- カスタムツール: `Public` を加えて `PublicResXFileCodeGenerator`にする


## Resource ID を修正

- 自動生成された .cs ファイルと .resx でリソースIDが異なるので合わせる
- Properties/LibResources.Designer.cs

~~~csharp
public static System.Resources.ResourceManager ResourceManager {
    get {
        if (object.Equals(null, resourceMan)) {
            System.Resources.ResourceManager temp = new System.Resources.ResourceManager(
              //"CoolLib.LibResources",    
              "CoolLib.Properties.LibResources",
              typeof(LibResources).GetTypeInfo().Assembly);

            resourceMan = temp;
        }
        return resourceMan;
    }
}
~~~

## 文字列リソースを追加

- Properties/LibResource.res

~~~xml
<data name="AppLabel" xml:space="preserve">
  <value>Application Name</value>
</data>
~~~

- 自動的にプロパティが追加される

~~~csharp
public static string AppLabel {
    get {
        return ResourceManager.GetString("AppLabel", resourceCulture);
    }
}
~~~

## 言語リソースファイル(ja_JP)を作成　

- LibResources_ja_JP.resx とかを作成(LibResources.ja_JP.resxで作ろうとするとLibResources.resxを更新しようとしてしまう)
- 作成したあとで、名前を LibResources.ja_JP.resx に変更する
- .cs ファイルは不要

### ファイルのプロパティを変更

- リソースID: `CoolLib.Properties.LibResources.ja_JP.resources` に変更
- ビルドアクション: `EmbeddedResource` であることを確認
- カスタムツール: `Public` を加えて `PublicResXFileCodeGenerator`にする

### リソース追加

~~~xml
<data name="AppLabel" xml:space="preserve">
  <value>アプリケーション名</value>
</data>
~~~

## CurrentCulture で .resx を切り替える

- LibResources.Desingner.cs で `ResourceManager` の getter を変更

~~~csharp
public static System.Resources.ResourceManager ResourceManager {
    get {
        if (object.Equals(null, resourceMan)) {
            var ci = System.Globalization.CultureInfo.CurrentCulture;

            System.Resources.ResourceManager temp = new System.Resources.ResourceManager(
                $"CoolLib.Properties.LibResources.{ci.Name}",
                typeof(LibResources).GetTypeInfo().Assembly);
            resourceMan = temp;
        }
        return resourceMan;
    }
}
~~~

- 日本語以外にすると例外が発生
- なぜか ResourceManager のなかでMissingManifestResourceExceptionをキャッチできない

## DLLのリソース一覧に存在したら切り替える

~~~csharp

using System.Linq;      // for sting[].Contains()
...

public static System.Resources.ResourceManager LoadManager(string lang = ""){
  var default_name = "CoolLib.Properties.LibResources";
  var asm = typeof(LibResources).GetTypeInfo ().Assembly;
  var reslist = asm.GetManifestResourceNames();
  foreach(var ln in new string[]{$".{lang}", ""})
  {
      if (reslist.Contains ($"{default_name}{ln}.resources")){
        return new global::System.Resources.ResourceManager (
						$"{default_name}{ln}",asm);
      }
  }
  return  null;
}

public static System.Resources.ResourceManager ResourceManager {

      get {
          if (object.Equals(null, resourceMan)) {

              var ci = System.Globalization.CultureInfo.CurrentCulture;
              System.Resources.ResourceManager temp = LoadManager (ci.Name);
              resourceMan = temp;
          }
          return resourceMan;
      }

  }    
~~~    

## アプリケーションから参照

- システム設定した言語に切り替わっているはず
- ja_JP 以外を設定すると英語になっているはず (iOSで確認)

~~~csharp
var label = CoolLib.LibResources.AppLabel;
~~~
