## メールサービス

- [Amazon SES](https://aws.amazon.com/jp/ses/)
- [Elastic Email](https://elasticemail.com/)
- [Gmail](https://mail.google.com/mail/u/0/#inbox)
- [Mailjet](https://app.mailjet.com/signup?utm_source=mautic)
- [Mandrill](http://mandrill.com/)
- [Momentum](https://www.sparkpost.com/messagesystems-momentum/) (実際はSparkpost)
- PHP Mail
- [Postmark](https://postmarkapp.com/)
- [Sendgrid - API](https://sendgrid.com/)
- [Sendgrid - SMTP](https://sendgrid.com/)
- [Sendmail](https://www.proofpoint.com/us/products/mail-routing-agent)
- [Sparkpost](https://www.sparkpost.com/)
- 他のSMTPサーバー

## スケジュールメール

- [Send Scheduled Broadcasts (e.g. segment emails)](https://www.mautic.org/docs/en/setup/cron_jobs.html)

コマンド:

~~~bash 
$ php /data/projects/taberu/landing/pr/app/console mautic:broadcasts:send --help
Usage:
  mautic:broadcasts:send [options]

Options:
  -c, --channel[=CHANNEL]                A specific channel to process broadcasts for pending contacts.
  -i, --id[=ID]                          The ID for a specifc channel to process broadcasts for pending contacts.
      --min-contact-id[=MIN-CONTACT-ID]  Min contact ID to filter recipients.
      --max-contact-id[=MAX-CONTACT-ID]  Max contact ID to filter recipients.
  -l, --limit[=LIMIT]                    Limit how many contacts to load from database to process.
  -b, --batch[=BATCH]                    Limit how many messages to send at once.
  -f, --force                            Force execution even if another process is assumed running.
      --bypass-locking                   Bypass locking.
  -t, --timeout=TIMEOUT                  If getmypid() is disabled on this system, lock files will be used. This option will assume the process is dead afer the specified number of seconds and will execute anyway. This is disabled by default. [default: false]
  -x, --lock_mode=LOCK_MODE              Force use of PID or FILE LOCK for semaphore. Allowed value are "pid" or "file_lock". By default, lock will try with pid, if not available will use file system [default: "pid"]
  -h, --help                             Display this help message
  -q, --quiet                            Do not output any message
  -V, --version                          Display this application version
      --ansi                             Force ANSI output
      --no-ansi                          Disable ANSI output
  -n, --no-interaction                   Do not ask any interactive question
  -s, --shell                            Launch the shell.
      --process-isolation                Launch commands from shell as a separate process.
  -e, --env=ENV                          The Environment name. [default: "prod"]
      --no-debug                         Switches off debug mode.
  -v|vv|vvv, --verbose                   Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Help:
                  The mautic:broadcasts:send command is send a channel broadcast to pending contacts.
  
  php /data/projects/taberu/landing/pr/app/console mautic:broadcasts:send --channel=email --id=3

~~~

- `--channel=email` どのチャネルを実行するか。指定しないと全チャネルに送ります。
- `--id=X` : メール、SMSなどの送るべきエンティティのID
- `--limit=X`:  何件づつおくるか。デフォルト100。 
- `--batch=X`:  最大何件をバッチでおくるか。プロバイダごとにことなります。
- `--segment-id=X`: セグメントをIDで指定します。 セグメントが複数にまたがっているユーザーには1件送ります。
- `--min-contact-id` / `--max-contact-id` : 1度に送るコンタクトIDの範囲を決めます。