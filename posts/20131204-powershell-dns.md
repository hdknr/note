Date: 2013-12-04  12:00
Title: Powershell: DNSの変更
Type: post  
Excerpt:   

    
    

インターフェースを取得:    
    
    C:\Users\Administrator>powershell
    Windows PowerShell
    Copyright (C) 2012 Microsoft Corporation. All rights reserved.
    
    PS C:\Users\Administrator> Get-NetIPConfiguration
    
    
    InterfaceAlias       : Ethernet
    InterfaceIndex       : 12
    InterfaceDescription : Citrix PV Ethernet Adapter #0
    NetProfile.Name      : Network
    IPv4Address          : 10.0.0.25
    IPv4DefaultGateway   : 10.0.0.1
    DNSServer            : 10.0.0.2
    
    
このインターフェース(#12)に対してDNSのアドレスを変更:
    
    PS C:\Users\Administrator> Set-DNSClientServerAddress -interfaceindex 12 -ServerAddress ("10.0.0.190")
    
    
確認:
    
    PS C:\Users\Administrator> Get-NetIPConfiguration
    
    
    InterfaceAlias       : Ethernet
    InterfaceIndex       : 12
    InterfaceDescription : Citrix PV Ethernet Adapter #0
    NetProfile.Name      : Network
    IPv4Address          : 10.0.0.25
    IPv4DefaultGateway   : 10.0.0.1
    DNSServer            : 10.0.0.190
    
    
    
