Date: 2014-01-30 11:30  
Title: jquery-ui : ui-icon の後で改行させない
Type: post  
Excerpt:   


jquery-ui :

    <script language="javascript" type="text/javaScript" src="/js/jquery-ui-1.10.4/js/jquery-ui-1.10.4.custom.min.js"></script>
    <script language="javascript" type="text/javaScript" src="/js/jquery-ui-1.10.4/js/jquery-1.10.2.js"></script>
    <link type="text/css" href="/js/jquery-ui-1.10.4/css/cupertino/jquery-ui-1.10.4.custom.css" rel="stylesheet" />

dislay:inline-block でメールアイコンを指定する :

    <td>
     <a href="mailto:{{user.email}}" title="{{user.email}}">
       <span style="display:inline-block" class="ui-icon ui-icon-mail-closed"/> </a>
       {{ user.full_name  }} </td>
