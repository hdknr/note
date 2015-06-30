
## Vagrant 

~~~
Peeko:~ hide$ cd ~/Documents/Boxes/

Peeko:Boxes hide$ git clone https://github.com/coreos/coreos-vagrant.git
Cloning into 'coreos-vagrant'...
remote: Counting objects: 300, done.
remote: Total 300 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (300/300), 65.96 KiB | 0 bytes/s, done.
Resolving deltas: 100% (129/129), done.
Checking connectivity... done.

Peeko:Boxes hide$ cd coreos-vagrant
~~~


~~~
Peeko:coreos-vagrant hide$ vagrant up
Bringing machine 'core-01' up with 'virtualbox' provider...
==> core-01: Box 'coreos-alpha' could not be found. Attempting to find and install...
    core-01: Box Provider: virtualbox
    core-01: Box Version: >= 308.0.1
==> core-01: Loading metadata for box 'http://alpha.release.core-os.net/amd64-usr/current/coreos_production_vagrant.json'
    core-01: URL: http://alpha.release.core-os.net/amd64-usr/current/coreos_production_vagrant.json
==> core-01: Adding box 'coreos-alpha' (v472.0.0) for provider: virtualbox
    core-01: Downloading: http://alpha.release.core-os.net/amd64-usr/472.0.0/coreos_production_vagrant.box
    core-01: Calculating and comparing box checksum...
==> core-01: Successfully added box 'coreos-alpha' (v472.0.0) for 'virtualbox'!
==> core-01: Importing base box 'coreos-alpha'...
==> core-01: Matching MAC address for NAT networking...
==> core-01: Checking if box 'coreos-alpha' is up to date...
==> core-01: Setting the name of the VM: coreos-vagrant_core-01_1415061172027_48865
==> core-01: Clearing any previously set network interfaces...
==> core-01: Preparing network interfaces based on configuration...
    core-01: Adapter 1: nat
    core-01: Adapter 2: hostonly
==> core-01: Forwarding ports...
    core-01: 22 => 2222 (adapter 1)
==> core-01: Running 'pre-boot' VM customizations...
==> core-01: Booting VM...
==> core-01: Waiting for machine to boot. This may take a few minutes...
    core-01: SSH address: 127.0.0.1:2222
    core-01: SSH username: core
    core-01: SSH auth method: private key
    core-01: Warning: Connection timeout. Retrying...
==> core-01: Machine booted and ready!
==> core-01: Setting hostname...
==> core-01: Configuring and enabling network interfaces...
Peeko:coreos-vagrant hide$ vagrant destroy
    core-01: Are you sure you want to destroy the 'core-01' VM? [y/N] y
==> core-01: Forcing shutdown of VM...
==> core-01: Destroying VM and associated drives...
~~~

~~~
Peeko:coreos-vagrant hide$ vagrant ssh
CoreOS (alpha)
core@core-01 ~ $
~~~

## version

~~~
core@core-01 ~ $ docker version

Client version: 1.3.0
Client API version: 1.15
Go version (client): go1.3.2
Git commit (client): c78088f
OS/Arch (client): linux/amd64
Server version: 1.3.0
Server API version: 1.15
Go version (server): go1.3.2
Git commit (server): c78088f
~~~

## network

~~~
core@core-01 ~ $ sudo ifconfig
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::a00:27ff:fefb:95c5  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:fb:95:c5  txqueuelen 1000  (Ethernet)
        RX packets 381  bytes 41154 (40.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 258  bytes 38217 (37.3 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.8.101  netmask 255.255.255.0  broadcast 172.17.8.255
        inet6 fe80::a00:27ff:fe60:3bef  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:60:3b:ef  txqueuelen 1000  (Ethernet)
        RX packets 2  bytes 478 (478.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11  bytes 1578 (1.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 80  bytes 8262 (8.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 80  bytes 8262 (8.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
~~~

# Debian Jessie

## pull

~~~
core@core-01 ~ $ docker pull debian:jessie

debian:jessie: The image you are pulling has been verified
511136ea3c5a: Pull complete 
848d84b4b2ab: Pull complete 
71d9d77ae89e: Pull complete 
Status: Downloaded newer image for debian:jessie
~~~

~~~
core@core-01 ~ $ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
debian              jessie              71d9d77ae89e        2 weeks ago         121.9 MB
~~~

~~~
core@core-01 ~ $ docker run debian:jessie
~~~

~~~
core@core-01 ~ $ docker ps -as
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES               SIZE
65b86c168e57        debian:jessie       "/bin/bash"         21 seconds ago      Exited (0) 20 seconds ago                       desperate_elion     0 B
~~~


