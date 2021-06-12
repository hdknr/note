# 関数

## 戻り

~~~ps1
function aboutMe($msg)
{
    "Hello, $($msg)"
    'John Doe'  
    return 36 
    'End.'      # これは評価されない
}

$res = aboutMe 'Good Morning!'

Write-Host $res ($res.length -eq 3) ($res[-1] -eq 36)
# Hello, Good Morning! John Doe 36 True True
~~~