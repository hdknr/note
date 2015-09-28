# systemctl コマンド

コマンドの種類:

- Unit Commands
- Unit File Commands
- Machine Commands
- Job Commands
- Snapshot Commands
- Manager Lifecycle Commands
- System Commands

 関連コマンド:

- systemd : systemd system and service manager (init)
- systemadm
- journalctl : Query the systemd journal
- loginctl : Control the systemd login manager

## list-units

- 一覧するには `systemctl` を実行

~~~bash
# systemctl
# systemctl --all
~~~

## status

~~~bash
# systemctl status ssh.service
~~~

## start / stop
