# クラス

## 例

~~~ps1
class Profile{
    [DateTime] $now = (Get-Date -format "yyyy-MM-dd HH:mm")
    [string] greetings(){
        return "Hello from a Class $($this.now) !!"
    }
}

Write-Host (New-Object Profile).greetings()
# Hello from a Class 04/13/2019 11:16:00 !!
~~~