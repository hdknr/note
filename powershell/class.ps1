class Profile{
    [DateTime] $now = (Get-Date)
    [string] greetings(){
        # https://www.c-sharpcorner.com/blogs/date-and-time-format-in-c-sharp-programming1
        return "Hello from a Class $($this.now.ToString('yyyy-MM-dd hh:mm')) !!"
    }
}

Write-Host (New-Object Profile).greetings()
