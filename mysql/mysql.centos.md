# CentOS

## systemctrl

| **操作**     | **コマンド**                               |
| ------------ | ------------------------------------------ |
| 開始         | `sudo systemctl start mysqld.service`      |
| 停止         | `sudo systemctl stop mysqld.service`       |
| 確認         | `sudo systemctl status mysqld.service`     |
| 自動起動     | `sudo systemctl enable mysqld.service`     |
| 自動起動解除 | `sudo systemctl disable mysqld.service`    |
| 自動起動確認 | `sudo systemctl is-enabled mysqld.service` |
