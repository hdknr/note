# 型

## コマンド(レット)の型

~~~ps1
PS > (Get-Command Get-Date)

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Get-Date                                           6.1.0.0    Microsoft.PowerShell.Utility

PS > (Get-Command Get-Date).OutputType

Name            Type            TypeDefinitionAst
----            ----            -----------------
System.DateTime System.DateTime
System.String   System.String
~~~