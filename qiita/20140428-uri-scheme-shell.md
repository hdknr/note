.NET: カスタムスキーマでデスクトップアプリを起動させる


```csharp


        /// <summary>
        /// URI Schemeのシェルハンドラを登録する
        /// </summary>
        /// <param name="proto">URI Scheme</param>
        /// <param name="path_exe">アプリケーションのパス</param>
        /// <param name="path_icon">アイコンのパス</param>
        public static void RegisterUriSchemeShellHandler(string proto, string path_exe = null, string path_icon = null)
        {
            path_exe = path_exe ?? System.Reflection.Assembly.GetExecutingAssembly().Location;
            path_icon = path_icon ?? path_exe;

            var key_proto = Microsoft.Win32.Registry.CurrentUser
                            .CreateSubKey("Software").CreateSubKey("Classes").CreateSubKey(proto);

            // Protocol Handler
            key_proto.SetValue("", "URL:OpenID Protocol");
            key_proto.SetValue("URL Protocol", "");

            // Icon
            var key_deficon = key_proto.CreateSubKey("DefaultIcon");
            key_deficon.SetValue("", string.Format(@"""{0}""", path_icon));

            // Executable Path
            var key_command = key_proto.CreateSubKey("shell").CreateSubKey("open").CreateSubKey("command");
            key_command.SetValue("",
                string.Format(@"""{0}"" ""%1"" ""%2"" ""%3"" ""%4"" ""%5"" ""%6"" ""%7"" ""%8"" ""%9""", path_exe)
                );

        }

```


メインのWindowsFormで:

```csharp

        public FormMain()
        {
            InitializeComponent();

            RegisterUriSchemeShellHandler("openid");       // "openid://?...." でこのプログラムが呼ばれる
        }    

```
        
