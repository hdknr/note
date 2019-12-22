#!/bin/bash

sudo mkdir /var/swap/
sudo dd if=/dev/zero of=/var/swap/swap0 bs=2M count=512
sudo chmod 600 /var/swap/swap0
sudo mkswap /var/swap/swap0
sudo swapon /var/swap/swap0

cat <<- EOS
/etc/fstab:

/var/swap/swap0 swap swap defaults 0 0
EOS
