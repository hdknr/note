Xamarin.Mac: ファイルオープンダイアログ = NSOpenPanel

- [NSOpenPanel members](http://macapi.xamarin.com/?link=T%3aMonoMac.AppKit.NSOpenPanel%2f*)

~~~csharp

NSOpenPanel openDlg= new NSOpenPanel{ CanChooseFiles =true };

if ((NSPanelButtonType)openDlg.RunModal()== NSPanelButtonType.Ok)
{
    // 何かする
    player.AddVideo( openDlg.Filename);
}
~~~				
