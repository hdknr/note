Date: 2013-09-05  16:00
Title: ASP.NET MVC: MapHttpRouteでコントローラクラスのネームスペースを指定できない
Type: post  
Excerpt:   


ページのルーティングでMapRouteだったら、namespaces: を指定出来ます:

    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Top", 
                          action = "Index",
                          id = UrlParameter.Optional },
                namespaces: new string[] 
                     { "WinConnectRegistry.Controllers.Custom",
                      "WinConnectRegistry" }
            );
        }
    }

が、APIルーてイングのMapHttpRouteだと出来ない、のでコントローラクラス名を一意にして、default: で controller を明示的に指定します。たとえば、コントローラクラスが以下のパターンであるとすると、 :


    PublicConfController.cs
    PublicJwksetController.cs
    PublicTokenController.cs
    RegConfController.cs
    RegJwksetController.cs
    RegTokenController.cs
    StoreConfController.cs
    StoreJwksetController.cs
    StoreTokenController.cs

APIルーティングを以下のようにしてやると /ロール名/オブジェクト名/ のURLマッピングができます (ロールが Publicの場合は、パスに指定しないようにしています):

    public static class WebApiConfig
    {
        public static void Register(HttpConfiguration config)
        {
            var roles = new string[] { "public", "reg", "store" };
            var objs = new string[] { "conf", "jwkset", "token" };

            foreach ( var role in roles )
                foreach (var obj in objs)
                {
                    var name = string.Format("{0}{1}",
                            (role =="public" ) ? "" : role+"/", obj );

                    config.Routes.MapHttpRoute(
                            name: "Api/" + name,
                            routeTemplate: "opop/{id}/" + name ,
                            defaults: new { controller = role + obj }
                        );
                }
        }
    }


