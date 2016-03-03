scriptcs: C# scripting

- [scriptcs](http://scriptcs.net/)
- 途中メモ

## Macでビルド

- [Building on Mac and Linux](https://github.com/scriptcs/scriptcs/wiki/Building-on-Mac-and-Linux)

- Xamarin + Mono がインストール済みのMac

~~~bash
$ git clone https://github.com/scriptcs/scriptcs
Cloning into 'scriptcs'...

remote: Counting objects: 12894, done.
remote: Total 12894 (delta 0), reused 0 (delta 0), pack-reused 12894
Receiving objects: 100% (12894/12894), 16.32 MiB | 1.76 MiB/s, done.
Resolving deltas: 100% (8231/8231), done.
Checking connectivity... done.
~~~

~~~bash
$ cd scriptcs/
$ git checkout dev
Already on 'dev'
Your branch is up-to-date with 'origin/dev'.
~~~

~~~bash
$ chmod +x build.sh
$ ./build.sh
......
......
Copyright (C) 2013 Outercurve Foundation.

xunit.dll:     Version 1.9.2.1705
Test assembly: /Users/hide/Projects/scriptcs/test/ScriptCs.Tests.Acceptance/bin/Release/ScriptCs.Tests.Acceptance.dll

82 total, 0 failed, 0 skipped, took 30.386 seconds

~~~

~~~bash
$ alias scriptcs='mono /Users/hide/Projects/scriptcs/src/ScriptCs/bin/Release/scriptcs.exe'
~~~

~~~bash
$ scriptcs
WARN: Some assemblies failed to load. Launch with '-repl -loglevel debug' to see the details
scriptcs (ctrl-c to exit or :help for help)

>  

~~~

~~~bash
$ scriptcs --help
Unexpected named argument: -help
Usage: scriptcs options

   OPTION                    DESCRIPTION                                                                                     
   -ScriptName (-script)     Script file name, must be specified first                                                       
   -Repl (-R)                Launch REPL mode when running script. To just launch REPL, simply omit the 'script' argument.   
   -Help (-?)                Displays help                                                                                   
   -Debug (-D)               Emits PDB symbols allowing for attaching a Visual Studio debugger                               
   -Cache (-C)               Flag which determines whether to run in memory or from a .dll                                   
   -LogLevel (-log)          Flag which defines the log level used.                                                          
   -Install (-i)             Installs and restores packages which are specified in packages.config                           
   -Global (-g)              Installs and restores global packages which are specified in packages.config                    
   -Save (-S)                Creates a packages.config file based on the packages directory                                  
   -Clean (-Cl)              Cleans installed packages from working directory                                                
   -AllowPreRelease (-pre)   Allows installation of packages prelease versions                                              
   -Version (-V)             Outputs version information                                                                     
   -Watch (-W)               Watch the script file and reload it when changed                                                
   -Modules (-M)             Specify modules to load                                                                         
   -Config (-Co)             Defines config file name                                                                        
   -PackageVersion (-P)      Defines the version of the package to install. Used in conjunction with -install                
   -Output (-O)              Write all console output to the specified file                                                  

   EXAMPLE: scriptcs server.csx -logLevel debug
   Executes the 'server.csx' script and displays detailed log messages. Useful for debugging.

~~~

## Newtonsoft.Json を使って見る

~~~bash
$ scriptcs -install Newtonsoft.Json

Installing packages...
Installed: Newtonsoft.Json
Package installation succeeded.
Saving packages in scriptcs_packages.config...
Creating scriptcs_packages.config...
Added Newtonsoft.Json (v7.0.1, .NET 4.5) to scriptcs_packages.config
Successfully updated scriptcs_packages.config.
~~~

~~~bash

$ tree .
.
├── scriptcs_packages
│   └── Newtonsoft.Json.7.0.1
│       ├── Newtonsoft.Json.7.0.1.nupkg
│       ├── lib
│       │   ├── net20
│       │   │   ├── Newtonsoft.Json.dll
│       │   │   └── Newtonsoft.Json.xml
│       │   ├── net35
│       │   │   ├── Newtonsoft.Json.dll
│       │   │   └── Newtonsoft.Json.xml
│       │   ├── net40
│       │   │   ├── Newtonsoft.Json.dll
│       │   │   └── Newtonsoft.Json.xml
│       │   ├── net45
│       │   │   ├── Newtonsoft.Json.dll
│       │   │   └── Newtonsoft.Json.xml
│       │   ├── portable-net40+sl5+wp80+win8+wpa81
│       │   │   ├── Newtonsoft.Json.dll
│       │   │   └── Newtonsoft.Json.xml
│       │   └── portable-net45+wp80+win8+wpa81+dnxcore50
│       │       ├── Newtonsoft.Json.dll
│       │       └── Newtonsoft.Json.xml
│       └── tools
│           └── install.ps1
└── scriptcs_packages.config

10 directories, 15 files
~~~

~~~csharp
$ scriptcs
scriptcs (ctrl-c to exit or :help for help)

> using Newtonsoft.Json;
> using Newtonsoft.Json.Linq;
> var json = JToken.Parse("{ name: 'Bob James'}");
> json.Value<string>("name");
Bob James
~~~

~~~bash
> :references
[
  "System",
  "System.Core",
  "System.Data",
  "System.Data.DataSetExtensions",
  "System.Xml",
  "System.Xml.Linq",
  "System.Net.Http",
  "Microsoft.CSharp",
  "/Users/hide/Projects/scriptcs/src/ScriptCs/bin/Release/ScriptCs.Core.dll",
  "/Users/hide/Projects/scriptcs/src/ScriptCs/bin/Release/ScriptCs.Contracts.dll",
  "/Users/hide/Downloads/sandbox/scriptcs_packages/Newtonsoft.Json.7.0.1/lib/net45/Newtonsoft.Json.dll"
]
~~~

## 自作DLLを使って見る

- RestSharp.Portable で JSONをGET

~~~csharp
using System;
using Newtonsoft.Json.Linq;
using RestSharp.Portable;
using RestSharp.Portable.HttpClient;

namespace Helper
{
	public class Rest
	{
		public Rest (string url)
		{
			_url = url;
		}
		string _url;
		public JToken Json { get; set; }

		public async void Get(string path, Action<Rest> action)
		{							
			using (var client = new RestClient (this._url)) {
				try {
					var req = new RestRequest (path, Method.GET);
					var res = await client.Execute<JToken> (req);

					if (res != null) {
						this.Json = res.Data;
					}
				} catch (Exception ex) {
					System.Diagnostics.Debug.WriteLine (ex.Message);
				}
			}					

			action (this);
		}
	}
}
~~~

- フルパス指定でロード("#r")

~~~csharp
> #r /Users/hide/Projects/Helper/Helper/bin/Debug/Helper.dll
~~~

- Github から組織一覧を取得して`login`の一覧を表示

~~~csharp
> var rest = new Helper.Rest("https://api.github.com");

> rest.Get("/users/hdknr/orgs", (Helper.Rest api) => { foreach(var i in api.Json) Console.Write("\n****  " + i.Value<string>("login"));});
>  
****  harajuku-tech
****  django-docs-ja
****  lafoglia
****  rioja

~~~

## Script-Pack

- [Script Packs](https://github.com/scriptcs/scriptcs/wiki/Script-Packs)


## Modules

- [Modules](https://github.com/scriptcs/scriptcs/wiki/Modules)
