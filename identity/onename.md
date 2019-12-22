# opendig

~~~
$ pip install opendig

Downloading/unpacking opendig
  Downloading opendig-0.1.0.tar.gz
  Running setup.py egg_info for package opendig
    
Downloading/unpacking cement==2.2.2 (from opendig)
  Downloading cement-2.2.2.tar.gz (101Kb): 101Kb downloaded
  Running setup.py egg_info for package cement
    
Downloading/unpacking dnspython==1.11.1 (from opendig)
  Downloading dnspython-1.11.1.zip (220Kb): 220Kb downloaded
  Running setup.py egg_info for package dnspython
    
Installing collected packages: opendig, cement, dnspython
  Running setup.py install for opendig
    changing mode of build/scripts-2.7/opendig from 644 to 755
    
    changing mode of /Users/hide/ve/tact/bin/opendig to 755
  Running setup.py install for cement
    
  Running setup.py install for dnspython
    
Successfully installed opendig cement dnspython
Cleaning up...
~~~

~~~
$ opendig --help
usage: opendig (sub-commands ...) [options ...] {arguments ...}

OpenDig: Command-line client for ONS (http://OpenNameSystem.org)

commands:

  bitcoin (aliases: btc)
    get the bitcoin address of a user

  github
    get the github username of a user

  twitter
    get the twitter handle of a user

optional arguments:
  -h, --help            show this help message and exit
  --debug               toggle debug output
  --quiet               suppress all output
  -u USER, --user USER  get user info
  -d DOMAIN, --domain DOMAIN
                        get domain info

~~~

~~~
$ opendig twitter -u hidelafoglia

;; <<>> OpenDig 0.1.0 <<>> twitter -u hidelafoglia
;; Got answer:

{
    "username": "hdknr"
}

;; EXECUTION TIME: 2560 msec
;; SERVERS CHECKED: 162.243.253.65 107.170.167.141 
;; WHEN: Fri Nov 14 21:45:19 2014
~~~

~~~
$ opendig -d onename.io

;; <<>> OpenDig 0.1.0 <<>> -d onename.io
;; Got answer:

onename.io. 21599 IN SOA rob.ns.cloudflare.com. dns.cloudflare.com. 2016743761 10000 2400 604800 3600
onename.io. 299 IN MX 10 aspmx.l.google.com.
onename.io. 299 IN MX 20 alt1.aspmx.l.google.com.
onename.io. 299 IN MX 20 alt2.aspmx.l.google.com.
onename.io. 299 IN MX 30 aspmx2.googlemail.com.
onename.io. 299 IN MX 30 aspmx3.googlemail.com.
onename.io. 299 IN TXT "v=spf1 include:mailgun.org ~all"
onename.io. 21599 IN NS rose.ns.cloudflare.com.
onename.io. 21599 IN NS rob.ns.cloudflare.com.
onename.io. 59 IN A 174.129.37.147
onename.io. 59 IN A 54.235.187.32
onename.io. 59 IN A 54.243.114.254

;; Query time: 633 msec
;; SERVER: 8.8.8.8 
;; WHEN: Fri Nov 14 21:46:55 2014
~~~

