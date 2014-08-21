Bash:substring (例:7.* というファイルを 8.* に変更する)


```bash

    for i in 7* ; do git mv  $i 8${i:1:${#i}} ; done
    
```    

変数:

```bash

    $ export VAR=0123456789

```

変数の文字列長:

```bash

    $ echo ${#VAR}
    10
```

変数の切り出し${VAR:開始(0起点):長さ):

```bash

    $ echo ${VAR:5:2}                                                                                                
    56
```
    
