![image](./php.png)

# スクリプトのパス

```
$p = pathinfo(realpath(__FILE__));
echo $p["dirname"];
```


# Python

| | Python	| PHP	|
|:-------------|:----------------| :-------------|
| 型 | type(obj) | get_class(obj) |
| [ループ](##Loop) | for i in collection | foreach($collection as &$i) |

## Loop

- python

```
a = [80, 100, 120]
for i in a:
   print a

```

- PHP

```
$a = array(80, 100, 120);
foreach($a as &$i){
    echo "{$i}¥n";
};
```