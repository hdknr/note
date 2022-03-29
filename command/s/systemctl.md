# systemctl


## `list-unit-files`

~~~bash
$ sudo systemctl list-unit-files --type=service | grep google 

google-disk-expand.service                    enabled 
google-guest-agent.service                    enabled 
google-osconfig-agent.service                 enabled 
google-oslogin-cache.service                  static  
google-shutdown-scripts.service               enabled 
google-startup-scripts.service                enabled 
~~~ 

## 資料

- [systemctl コマンド](https://qiita.com/sinsengumi/items/24d726ec6c761fc75cc9)
