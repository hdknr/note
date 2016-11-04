
## Cannot get remote repository information.

- gitが古すぎる (> <)

~~~
$ git clone https://github.com/hdknr/bin.git
Initialized empty Git repository in /home/ubuntu/bin/.git/
Cannot get remote repository information.
Perhaps git-update-server-info needs to be run there?

$ git --version
git version 1.5.4.3

$ git clone git://github.com/hdknr/bin.git
Initialized empty Git repository in /home/ubuntu/bin/.git/
remote: Counting objects: 641, done.
remote: Total 641 (delta 0), reused 0 (delta 0), pack-reused 641
Receiving objects: 100% (641/641), 77.96 KiB, done.
Resolving deltas: 100% (344/344), done.
~~~
