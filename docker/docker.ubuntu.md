# Docker: Ubuntu

- [Ubuntu 20.04へのDockerのインストールおよび使用方法](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ja)

~~~bash
% sudo apt update
% sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
% curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
% sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
% sudo apt update
% apt-cache policy docker-ce
% sudo apt install -y docker-ce
% sudo systemctl status docker
% sudo usermod -aG docker ${USER}
~~~

ログインし直し:

~~~bash
% id -nG | grep  docker | wc
~~~

