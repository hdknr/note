Date: 2013-11-29  
Title:  PowerShell:デフォルトではファイル実行できません
Type: post  
Excerpt:   


テストスクリプト:

    $ more test.ps1

    Write-Host "Hello,PowerShell"



実行するとエラー:

    $ powershell .\test.ps1

    .\test.ps1 : このシステムではスクリプトの実行が無効になっているため、
    ファイル C:\Users\Administrator\test.ps1 を読み込むことができません。
    詳細については、「about_Execution_Policies」
    (http://go.microsoft.com/fwlink/?LinkID=135170) を参照してください。

    発生場所 行:1 文字:1
    + .\test.ps1
    + ~~~~~~~~~~
        + CategoryInfo          : セキュリティ エラー: (: ) []、PSSecurityException
        + FullyQualifiedErrorId : UnauthorizedAccess


設定変更:

    $ powershell

    Windows PowerShell
    Copyright (C) 2012 Microsoft Corporation. All rights reserved.
    
    PS C:\Users\Administrator> Get-ExecutionPolicy

    Restricted

    PS C:\Users\Administrator> Set-ExecutionPolicy RemoteSigned

    PS C:\Users\Administrator> Get-ExecutionPolicy

    RemoteSigned
    
    PS C:\Users\Administrator> exit


実行:

    $ powershell .\test.ps1

    Hello,PowerShell

