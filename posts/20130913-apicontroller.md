Date: 2013-09-13  05:00
Title: ASP.NET MVC: ApiControllerに渡したPOSTのデータはクラスで受け取る事..
Type: post  
Excerpt:   


通常の Controllerクラスのようにapplication/x-www-form-urlencodedでボディに入れられたPOSTデータをFormCollectionで受け取れないです。:

    public class PublicTokenController : ApiController
    {   
        [HttpPost]
        public Connect.Messages.TokenRes Post(string id, 
             [FromBody] FormCollection request )
        {   
            // request のインスタンスは作成されますが、中身は無しです
        }   
    }   

なので、フォームパラメータをフィールドに持ったクラスを定義して、それで受け取ればいいです。

    public TokenRequest
    {
        publc string code {get;set;}
        //....
    }
    
    public class PublicTokenController : ApiController
    {   
        [HttpPost]
        public Connect.Messages.TokenRes Post(string id,
             [FromBody] TokenRequest request )
        {
            // request.codeにデータはいっています
        }
    }

Json.NETのシリアライザ属性入れると文字列をEnumに入れてくれているようです。:

    public TokenRequest
    {
        public enum GrantTypeEnum
        {
            none = 0,
            authorization_code = 1,
            client_credentials = 2,
        }
        publc string code {get;set;}

        [JsonConverter(typeof(StringEnumConverter)] 
        public GrantTypeEnum grant_type { get; set; }
        
        //....
    }
    
    public class PublicTokenController : ApiController
    {   
        [HttpPost]
        public Connect.Messages.TokenRes Post(string id,
             [FromBody] TokenRequest request )
        {   
            // request.grant_type にデータはいっています
        }
    }

これは application/jsonでJson形式でポストしても、サーバーの処理は同じになります:

    { "code" : "fdsa0fdsafdsa", "grant_type" : "authorization_code" }
    
“APIなんだからデータ形式きまっているだろ？”という思想なんでしょうか。。。
    