# aws-cli: `aws logs`

- [logs:公式ドキュメント](https://docs.aws.amazon.com/cli/latest/reference/logs/index.html)

## 実行

- ランチャーが動いています
- `aws logs push` がランチャーに起動されています

~~~bash 
$ sudo ps ax | grep aws
.
29312 ?        S      0:00 /bin/sh /var/awslogs/bin/awslogs-agent-launcher.sh
29315 ?        SNl    0:23 /var/awslogs/bin/python /var/awslogs/bin/aws logs push --config-file /var/awslogs/etc/awslogs.conf --additional-configs-dir /var/awslogs/etc/config
~~~~

## ランチャー: /var/awslogs/bin/awslogs-agent-launcher.sh

- 優先度4で `aws logs push` コマンドを実行します
- システム設定ファイルとして /var/awslogs/etc/awslogs.conf を読み込みます
- ユーザー設定ファイルとして /var/awslogs/etc/config を読み込みます

~~~bash
#!/bin/sh
# Version: 1.4.3
echo -n $$ > /var/awslogs/state/awslogs.pid
[ -f /var/awslogs/etc/proxy.conf ] && . /var/awslogs/etc/proxy.conf

/usr/bin/env -i \
    HTTPS_PROXY=$HTTPS_PROXY \
    HTTP_PROXY=$HTTP_PROXY \
    NO_PROXY=$NO_PROXY \
    AWS_CONFIG_FILE=/var/awslogs/etc/aws.conf \
    HOME=/home/ubuntu \
/usr/bin/nice -n 4 \
/var/awslogs/bin/aws logs push \
    --config-file /var/awslogs/etc/awslogs.conf \
    --additional-configs-dir /var/awslogs/etc/config \
>> /var/log/awslogs.log 2>&1
~~~

## virtualenv: /var/awslogs

- インストールされると、`/var/awslogs` virtualenvが作成されます
- よって、インタプリタは /var/awslogs/bin/python

~~~bash
$ /var/awslogs/bin/python --version
Python 2.7.12
~~~

ヘルプ:

~~~bash
$ /var/awslogs/bin/python /var/awslogs/bin/aws logs help
.
~~~

## pushサブコマンド

- `cwlogs` プラグインが実装されている([awscli-cwlogs](https://pypi.org/project/awscli-cwlogs/))

~~~bash
$ sudo cat /var/awslogs/etc/aws.conf
.
~~~

~~~ini
[plugins]
cwlogs = cwlogs
[default]
region = ap-northeast-1
~~~

## デーモン起動: /etc/init.d/awslogs

- ランチャーをデーモン起動します

~~~bash 
#!/bin/sh

### BEGIN INIT INFO
# Provides:          awslogs
# Required-Start:    networking
# Required-Stop:     networking
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Daemon for AWSLogs agent.
# Description:       This script is responsible for running AWSLogs agent
#                    as a daemon.
### END INIT INFO

# Version: 1.4.3

CONFIG_FILE=/var/awslogs/etc/awslogs.conf
DAEMON=/var/awslogs/bin/awslogs-agent-launcher.sh
DAEMON_NAME=awslogs

DAEMON_USER=root
PIDFILE=/var/awslogs/state/awslogs.pid
LOCKFILE=/var/awslogs/state/awslogs.lock
MUTEXFILE=/var/awslogs/state/awslogs.mutex

START_CMD="start-stop-daemon --start --background --pidfile $PIDFILE --user $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON"
STATUS_CMD="status_of_proc -p $PIDFILE "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?"

RETVAL=0

legacy_start() {
    echo "Starting $DAEMON_NAME daemon"
    daemon --pidfile $PIDFILE --user=$DAEMON_USER "nohup $DAEMON > /dev/null 2>&1 &"
}

if [ -e /etc/init.d/functions ]; then
    . /etc/rc.d/init.d/functions
    START_CMD=legacy_start
    STATUS_CMD="status -p $PIDFILE"
elif [ -e /lib/lsb/init-functions ]; then
    . /lib/lsb/init-functions
else
    echo "Failed to detect LSB compliant init-functions."
    exit 1
fi

do_start () {
    (
        flock -w 10 -x 9
        echo "Starting system $DAEMON_NAME daemon"
        $START_CMD
        RETVAL=$?
        touch $LOCKFILE

        for i in {1..5}
        do
            $STATUS_CMD
            if [ $? -ne 0 ];then
                echo "`date +%F_%T_%N` status is not running, sleep 2 second"
                sleep 2
            else
                break
            fi
        done
    ) 9>$MUTEXFILE
    rm -f $MUTEXFILE
}

do_stop () {
    (
        flock -w 10 -x 9
        echo "Stopping system $DAEMON_NAME daemon"
        ppids=`ps axo pid,comm | grep "awslogs-agent-l" | awk '{print $1}'`
        for pid in $ppids; do
            pkill -15 -P $pid > /dev/null 2>&1
        done

        sleep 3
        procList=`ps axo pid,comm | grep "awslogs-agent-l"`
        procsAlive=$?
        ppids=`${procList} | awk '{print $1}'`
        if [ $procsAlive = 0 ]; then
            for pid in $ppids; do
                pkill -9 -P $pid > /dev/null 2>&1
            done
        fi

        procList=`ps axo pid,comm | grep "awslogs-agent-l"`
        if [ $? != 0 ]; then
            RETVAL=0
        else
            RETVAL=1
        fi

        rm -f $LOCKFILE
    ) 9>$MUTEXFILE
    rm -f $MUTEXFILE
}
do_restart () {
    do_stop
    do_start
}

case "$1" in

    start)
        do_start
        ;;
    stop)
        do_stop
        ;;
    restart)
        do_restart
        ;;
    status)
        $STATUS_CMD
        ;;
    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
        exit 1
        ;;

esac
exit $RETVAL
~~~~

## 記事

- [CloudWatch Logs Agentの中身を探してみた](https://qiita.com/tt2004d/items/fb36a2e751e3dd8985fb)
- [文字列をCloudWatchLogsにPUTしてみた](https://dev.classmethod.jp/cloud/aws/put-cloudwatchlogs/)