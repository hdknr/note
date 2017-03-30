# ローカライゼーション

- [Localizing Xamarin.Forms Apps with RESX Resource Files
](https://developer.xamarin.com/guides/xamarin-forms/advanced/localization/)

- [System.Resources.ResourceManager](https://developer.xamarin.com/api/type/System.Resources.ResourceManager/)

## カスタムツール

- PublicResXFileCodeGenerator にする
- アセンブリをまたがって利用できる

## ビルドアクション

- EmbeddedResource

## data 要素


## 翻訳ファイル

- .resx の .cs コードビハインド不要




# リソースが見つからない: Could not find any resources appropriate for the specified culture or the neutral culture.  

~~~
Could not find any resources appropriate for the specified culture or the neutral culture.  

Make sure "CoolApp.AppResources.resources" was correctly embedded
or linked into assembly "CoolApp" at compile time,
or that all the satellite assemblies required are loadable and fully signed."
~~~

リソースIDがちがっている:

- .resxファイルの リソースIDが`CoolApp.Properties.AppResources.resources ` で作成されている
- CoolApp.AppResources.resources に修正してビルドするとよい
