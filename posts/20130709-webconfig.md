Date: 2013-07-09  13:30
Title: .NET : web.config/app.config の書き換え
Type: post  
Excerpt:   

*.configファイルのロード。Machine.configとか、どのユーザー用のとかいろいろめんどくさくなっている。とりあえず、全員向け(ConfigurationUserLevel.None)で開く:

        public static System.Configuration.Configuration LoadConfiguration(string path)
        {
            return  System.Configuration.ConfigurationManager.OpenMappedExeConfiguration(
                    new System.Configuration.ExeConfigurationFileMap() { ExeConfigFilename = path },
               System.Configuration.ConfigurationUserLevel.None);
        }

        
これをロードしたらセクションを指定してセクションのクラスにキャストすればいい。:


    
            var conf = LoadConfiguration(path);

            var connect_config = (Connect.Setting) conf.GetSection("Connect");
            var new_path = string.Format(@"C:\{0}",System.Guid.NewGuid().ToString());
            Assert.AreNotEqual(connect_config.Storage.Path,new_path );
            connect_config.Storage.Path = new_path;
            conf.Save();    // 保存
