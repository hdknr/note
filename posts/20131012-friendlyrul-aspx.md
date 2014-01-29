Date: 2013-10-12  4:00
Title:  ASP.NET:Microsoft.AspNet.FriendlyUrlsでURLを作る
Type: post  
Excerpt:   


~/admin/op.aspxで、 "/admin/op/create" というURLを作る:

    <%@ Import Namespace="Microsoft.AspNet.FriendlyUrls" %>
    :
    :
    :
    <a href="<%= FriendlyUrl.Href("~/admin/op", "create") %>"> 作成</a>   
    