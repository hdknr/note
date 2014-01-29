Date: 2013-10-09  12:30
Title: C#: app.configに追加修正して保存
Type: post  
Excerpt:   



インストーラとか設定プログラムでapp.config(web.config)のパス名を指定して
書き換える時に使える。 プロジェクトの各アセンブリで設定セクションをカスタム
で定義しているシナリオ。:

    public class SystemConfiguration
    {
        protected System.Configuration.Configuration _conf;

        public SystemConfiguration(string path = null)
        {
            if (!string.IsNullOrEmpty(path))
            {
                _conf = 
                    System.Configuration.ConfigurationManager.OpenMappedExeConfiguration(
                        new System.Configuration.ExeConfigurationFileMap() 
                        { ExeConfigFilename = path },
                        System.Configuration.ConfigurationUserLevel.None);
            }
        }

        public void Save()
        {
            _conf.Save();
        }

        public T GetSection<T>(string section_name=null) 
                        where T: ConfigurationSection
        {
            // section_name が指定されていないと、アセンブリ名を使う
            section_name = string.IsNullOrEmpty(section_name) ?
                typeof(T).FullName.Split('.')[0] : section_name;

            if (_conf != null)
            {
                return (T)_conf.GetSection(section_name);
            }

            return (T) System.Configuration.ConfigurationManager.GetSection(section_name);

        }
    }


サンプル app.config。プロジェクトでは、Jose.dllとConnect.dllがそれぞれ設定セクションを定義しています:

    <?xml version="1.0" encoding="utf-8" ?>
    <configuration>
      <configSections>
        <section name="Connect" type="Connect.Setting, Connect" />
        <section name="Jose" type="Jose.Setting, Jose" />
      </configSections>
        <startup> 
            <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.5" />
        </startup>
    </configuration>

テスト:

    var settings = new SystemConfiguration(test_config_file);
    var connect_settings = settings.GetSection<Connect.Setting>();

    Func<string,Uri> iss = x =>  new Uri(string.Format("http://op.net/auth/op/{0}",x) );
    Func<string, Uri> jku = x => new Uri(string.Format("http://op.net/auth/op/{0}/jwkset", x));

    var ops = new string[] { "std", "0001" };

    foreach (var op in ops )
    {
        // サブセクション Providersをコレクションでカスタム定義しています
        var provider = new Connect.ProviderSetting()
        {
            ID = op,
            IssuerIdentifier = iss(op),
            KeyURL = jku(op),
        };

        connect_settings.Providers.Add(provider);
    }    

    settings.save();

    Console.WriteLine(XElement.Load(test_config_file)
                        .XPathSelectElement("/Connect/Providers/add[@ID='std']")
                        .Attribute("IssuerIdentifier").Value);

結果:

    結果  の標準出力:   http://op.net/auth/op/std



