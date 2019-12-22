Xamarin:  Visual Studio とプロジェクト共有 : パッケージディレクトリを共有する

- デフォルトで ソリューション/packages に作る
- 普通、packagesのフォルダはレポジトリに入れない
- ので、ソリューションに取り込まれる `*.csprojの<Reference><HintPath>`に存在しない参照ができてしまって、ビルドできない
- nuget.config に設定してpackagesフォルダを共有しましょう

##  レポジトリ

```
:connectsharp
├── Josse
│   └── Jose.csproj
├── Jose.Unit
│   └── Jose.Unit.csproj
├── XmJose
│   └── XmJose.sln
├── VsJose
│   ├── .nuget
│   └── VsJose.sln
```

## 共通パッケージフォルダ

- 作らなくてもいいです。 VS,Xamariが作ってくれる。

```
Peeko:connectsharp hide$ mkdir .packages
```

## ソリューション/.nuget/nuget.config 作成

- Xamarin 5.2 から

```
Peeko:connectsharp hide$ mkdir -p XmJose/.nuget
```

```
Peeko:connectsharp hide$ cat > XmJose/.nuget/nuget.config << EOF
> <configuration>
>   <config>
>      <add key="repositoryPath" value="../../.packages" />
>    </config>
>  </configuration>
> EOF
```

- VS側にもコピー

```
Peeko:connectsharp hide$ cp XmJose/.nuget/nuget.config  VsJose/.nuget/
```
