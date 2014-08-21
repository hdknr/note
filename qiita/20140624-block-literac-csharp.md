C#:Regex:JSONヒアドキュメント



テストコードとかでJSONを埋め込むときとかの対応。　
"_" というラムダを定義して各行のホワイトスペースを抜く。
   
```csharp

    using System;
    using NUnit.Framework;
    using System.Text.RegularExpressions;
    using System.Collections.Generic;
    using System.Linq;
    using System.Linq.Expressions;
```
    
    
```csharp

    namespace ConnectTestIos
    {
    	public class JweAppendixA1 
    	{
    		public static string _re_sp = @"^(\s+)?(.+\S)?(\s+)?$";
    		public static Func<string, string> _ = src => 
    			string.Join("", src.Split('\n').Select(i=> Regex.Replace(i, _re_sp,"$2")));
    
    		public string _jwkstr = _(@"
         {""kty"" : ""RSA"",
          ""n"":""oahUIoWw0K0usKNuOR6H4wkf4oBUXHTxRvgb48E-BVvxkeDNjbC4he8rUW
               cJoZmds2h7M70imEVhRU5djINXtqllXI4DFqcI1DgjT9LewND8MW2Krf3S
               psk_ZkoFnilakGygTwpZ3uesH-PFABNIUYpOiN15dsQRkgr0vEhxN92i2a
               sbOenSZeyaxziK72UwxrrKoExv6kc5twXTq4h-QChLOln0_mtUZwfsRaMS
               tPs6mS6XrgxnxbWhojf663tuEQueGC-FCMfra36C9knDFGzKsNa7LZK2dj
    			YgyD3JR_MB_4NUJW_TqOQtwHYbxevoJArm-L5StowjzGy-_bq6Gw"",
    		""e"":""AQAB"",
    		""d"":""kLdtIj6GbDks_ApCSTYQtelcNttlKiOyPzMrXHeI-yk1F7-kpDxY4-WY5N
               WV5KntaEeXS1j82E375xxhWMHXyvjYecPT9fpwR_M9gV8n9Hrh2anTpTD9
               3Dt62ypW3yDsJzBnTnrYu1iwWRgBKrEYY46qAZIrA2xAwnm2X7uGR1hghk        
               qDp0Vqj3kbSCz1XyfCs6_LehBwtxHIyh8Ripy40p24moOAbgxVw3rxT_vl
               t3UVe4WO3JkJOzlpUf-KTVI2Ptgm-dARxTEtE-id-4OJr0h-K-VFs3VSnd
    		VTIznSxfyrj8ILL6MG_Uv8YAu7VILSB3lOW085-4qE3DzgrTjgyQ""
         }");
         
         public Jose.Jwk PrivateJwk {
    			get{
    				return Jose.Jwk.FromJson (_jwkstr);
    			}
    	 }	
       }
    }
 
```
