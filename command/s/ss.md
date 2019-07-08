- [ssコマンドの使い方](https://qiita.com/hana_shin/items/632b3a1eb44bf84e94f7)


## Listing ソケット

~~~bash 
$ sudo ss -lt4

State      Recv-Q Send-Q            Local Address:Port                             Peer Address:Port                
LISTEN     0      80                    127.0.0.1:mysql                                       *:*                    
LISTEN     0      128                           *:hostmon                                     *:*                    
LISTEN     0      128                   127.0.0.1:11211                                       *:*                    
LISTEN     0      128                           *:http                                        *:*                    
LISTEN     0      128                           *:ssh                                         *:*                    
LISTEN     0      128                           *:8800                                        *:*   
~~~