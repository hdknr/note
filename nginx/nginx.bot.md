# bot blocker

- [mitchellkrogza/nginx-ultimate-bad-bot-blocker](https://github.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker)
- [悪質なbotのアクセスをNginxでバッサリ切り捨てる](https://qiita.com/ihsiek/items/3bde1fda87ff4a0022cb)

~~~bash 
$ sudo curl -sL https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/install-ngxblocker -o /usr/local/sbin/install-ngxblocker

$ sudo chmod +x /usr/local/sbin/install-ngxblocker
~~~

~~~bash
$ cd /usr/local/sbin/
$ sudo ./install-ngxblocker 
Checking url: https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/include_filelist.txt

** Dry Run ** | not updating files | run  as 'install-ngxblocker -x' to install files.

Creating directory: /etc/nginx/bots.d

REPO = https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master

Downloading [FROM]=>  [REPO]/conf.d/globalblacklist.conf            [TO]=>  /etc/nginx/conf.d/globalblacklist.conf
Downloading [FROM]=>  [REPO]/conf.d/botblocker-nginx-settings.conf  [TO]=>  /etc/nginx/conf.d/botblocker-nginx-settings.conf

REPO = https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master

Downloading [FROM]=>  [REPO]/bots.d/blockbots.conf              [TO]=>  /etc/nginx/bots.d/blockbots.conf
Downloading [FROM]=>  [REPO]/bots.d/ddos.conf                   [TO]=>  /etc/nginx/bots.d/ddos.conf
Downloading [FROM]=>  [REPO]/bots.d/custom-bad-referrers.conf   [TO]=>  /etc/nginx/bots.d/custom-bad-referrers.conf
Downloading [FROM]=>  [REPO]/bots.d/bad-referrer-words.conf     [TO]=>  /etc/nginx/bots.d/bad-referrer-words.conf
Downloading [FROM]=>  [REPO]/bots.d/blacklist-domains.conf      [TO]=>  /etc/nginx/bots.d/blacklist-domains.conf
Downloading [FROM]=>  [REPO]/bots.d/blacklist-ips.conf          [TO]=>  /etc/nginx/bots.d/blacklist-ips.conf
Downloading [FROM]=>  [REPO]/bots.d/blacklist-user-agents.conf  [TO]=>  /etc/nginx/bots.d/blacklist-user-agents.conf
Downloading [FROM]=>  [REPO]/bots.d/whitelist-domains.conf      [TO]=>  /etc/nginx/bots.d/whitelist-domains.conf
Downloading [FROM]=>  [REPO]/bots.d/whitelist-ips.conf          [TO]=>  /etc/nginx/bots.d/whitelist-ips.conf

REPO = https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master

Downloading [FROM]=>  [REPO]/setup-ngxblocker      [TO]=>  /usr/local/sbin/setup-ngxblocker
Downloading [FROM]=>  [REPO]/update-ngxblocker     [TO]=>  /usr/local/sbin/update-ngxblocker
~~~

~~~bash 
$ sudo ./install-ngxblocker -x
~~~

~~~bash 
$ sudo ./setup-ngxblocker -x -v /etc/nginx/conf.d -e conf 
Checking url: https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/include_filelist.txt

INFO:      /etc/nginx/conf.d/* detected               => /etc/nginx/nginx.conf

Whitelisting ip:  153.201.112.117 => /etc/nginx/bots.d/whitelist-ips.conf

Checking for missing includes:

Checking url: https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/include_filelist.txt

Nothing to update for directory: /etc/nginx/conf.d
Nothing to update for directory: /etc/nginx/bots.d
Nothing to update for directory: /usr/local/sbin
Setting mode: 700 => /usr/local/sbin/install-ngxblocker
Setting mode: 700 => /usr/local/sbin/setup-ngxblocker
Setting mode: 700 => /usr/local/sbin/update-ngxblocker
~~~

~~~bash
$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

$ sudo nginx -s reload
~~~

~~~bash 
 $ sudo chmod +x /usr/local/sbin/update-ngxblocker
~~~

~~~bash
$ sudo /usr/local/sbin/update-ngxblocker 

LOCAL Version: 3.2018.07.1125
Updated: Thu Jul  5 16:41:36 SAST 2018

REMOTE Version: 3.2018.07.1125
Updated: Thu Jul  5 16:41:36 SAST 2018

Latest Blacklist Already Installed: 3.2018.07.1125

~~~

~~~bash
$ sudo crontab -l -u root

00 */8 * * * /usr/local/sbin/update-ngxblocker
~~~


# URL

- `.git` のアクセス

~~~
    location ~ \.git {
       return 404;
       break;
    }
~~~