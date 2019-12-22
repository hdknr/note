# nginx

~~~bash
$ sudo apt install python3-certbot-nginx -y
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  python3-pyparsing
Suggested packages:
  python-certbot-nginx-doc python-pyparsing-doc
The following NEW packages will be installed:
  python3-certbot-nginx python3-pyparsing
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 95.7 kB of archives.
After this operation, 510 kB of additional disk space will be used.
Get:1 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic/main amd64 python3-pyparsing all 2.2.0+dfsg1-2 [52.2 kB]
Get:2 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-certbot-nginx all 0.23.0-1 [43.5 kB]
Fetched 95.7 kB in 0s (284 kB/s)
Selecting previously unselected package python3-pyparsing.
(Reading database ... 171397 files and directories currently installed.)
Preparing to unpack .../python3-pyparsing_2.2.0+dfsg1-2_all.deb ...
Unpacking python3-pyparsing (2.2.0+dfsg1-2) ...
Selecting previously unselected package python3-certbot-nginx.
Preparing to unpack .../python3-certbot-nginx_0.23.0-1_all.deb ...
Unpacking python3-certbot-nginx (0.23.0-1) ...
Setting up python3-pyparsing (2.2.0+dfsg1-2) ...
Setting up python3-certbot-nginx (0.23.0-1) ...
~~~

~~~bash
$ sudo certbot renew --dry-run --nginx
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/www.mycoolsite.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert not due for renewal, but simulating renewal for dry run
Plugins selected: Authenticator nginx, Installer nginx
Renewing an existing certificate
Performing the following challenges:
http-01 challenge for stage.mycoolsite.com
http-01 challenge for www.mycoolsite.com
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed with reload of nginx server; fullchain is
/etc/letsencrypt/live/www.mycoolsite.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates below have not been saved.)

Congratulations, all renewals succeeded. The following certs have been renewed:
  /etc/letsencrypt/live/www.mycoolsite.com/fullchain.pem (success)
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates above have not been saved.)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
~~~
