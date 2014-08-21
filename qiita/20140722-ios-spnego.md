SPNEGO: iOS Safari SSO

# .mobileconfig plist 

ios.mobileconfig XMLファイルを作る([Apple](https://developer.apple.com/library/ios/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html) ):

    <?xml version="1.0" encoding="UTF-8"?> 
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> 
    <plist version="1.0"> 
    <dict> 
      <key>PayloadContent</key> 
      <array> 
        <dict> 
          <key>PayloadDisplayName</key> <string>Single Sign-On via SPNego</string> 
          <key>PayloadType</key> <string>com.apple.sso</string> 
          <key>PayloadVersion</key> <integer>1</integer> 
          <key>PayloadUUID</key> <string>d3fe4709-0cc6-4f51-afed-839c6ab1451c</string> 
          <key>PayloadIdentifier</key> <string>local.openid.windomain</string>  <!-- AD Server -->
          <key>Name</key> <string>Kerberos SSO</string> 
          <key>Kerberos</key> 
          <dict> 
            <key>PrincipalName</key> <string>hide</string>     <!-- ドメインユーザー名 -->
            <key>Realm</key> <string>OPENID.LOCAL</string>     <!-- レルム/AD ドメイン名 -->
            
            <key>URLPrefixMatches</key> 
                <!--
                    List of URLs prefixes that must be matched to use 
                    this account for Kerberos authentication over HTTP. 
                    Note that the URL postfixes must match as well.
                -->
            <array> 
      	      <string>http://ubuntu.openid.local</string>      
            </array> 
            
            <key>AppIdentifierMatches</key> 
                <!-- 
                    Optional. List of app identifiers that are allowed to use this login. 
                    If this field missing, this login matches all app identifie
                    This array, if present, may not be empty.
                -->
            <array> 
              <string>com.apple.mobilesafari</string> 
              <string>local.openid.*</string> 
            </array> 
            
          </dict> 
        </dict> 
      </array> 
      
      <key>PayloadOrganization</key> <string>Lafoglia</string> 
      <key>PayloadDisplayName</key> <string>SSO for mod_auth_kerb</string> 
      <key>PayloadVersion</key> <integer>1</integer> 
      <key>PayloadUUID</key> <string>95A9BDB1-D1F1-4A66-8F10-E72B48D79665</string> 
      <key>PayloadIdentifier</key> <string>local.openid.windomain</string>   
      <key>PayloadDescription</key> <string>SSO Configuration profile</string> 
      <key>PayloadType</key> <string>Configuration</string> 
    </dict> 
    </plist> 
    
# インストール&SSO
mod_auth_kerbで認証かけたLocation("/i"以下)にアクセスすると認証エラー

![image](https://lh3.googleusercontent.com/-rdOze8Nw1Yo/U82saWjWrDI/AAAAAAAAAk0/uqgNqKf1tRc/w394-h559-no/%25E3%2582%25B9%25E3%2582%25AF%25E3%2583%25AA%25E3%2583%25BC%25E3%2583%25B3%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%2583%25E3%2583%2588+2014-07-22+9.11.56.png)  

http://ubuntu.openid.local/ios.mobileconfig (apache)に配置して、ダウンロード

![image](https://lh5.googleusercontent.com/-YjNzl0_6qQE/U82opsyHBTI/AAAAAAAAAkA/k7PZ-mbZ46s/w394-h559-no/ios_safari_1.png)

インストール
![image](https://lh3.googleusercontent.com/-B1FocnEWWFk/U82opeFqrAI/AAAAAAAAAkI/2tcYV1ptvnE/w394-h559-no/ios_safari_2.png)

再度アクセスする


![image](https://lh6.googleusercontent.com/--GDvoTUAGc0/U82oqB_SDgI/AAAAAAAAAkM/4TpKZlBOwQo/w394-h559-no/ios_safari_4.png)

アクセスできた

![image](https://lh4.googleusercontent.com/-IE9Hw_IORSY/U82oqpkOQoI/AAAAAAAAAkQ/nERrJvCU91c/w394-h559-no/ios_safari_5.png)


 
