# global-status

- https://www.vagrantup.com/docs/cli/global-status.html

~~~bash
vagrant global-status --prune
~~~

~~~bash
id       name    provider   state    directory
----------------------------------------------------------------------------
397d693  default virtualbox saved    /Users/hide/Documents/Boxes/js2
7ec5b2c  default virtualbox poweroff /Users/hide/Documents/Boxes/ubuntu1704
4331eef  default virtualbox running  /Users/hide/Documents/Boxes/ubn
a2afe41  default virtualbox poweroff /Users/hide/Documents/Boxes/msedge
3fd8925  default virtualbox poweroff /Users/hide/Documents/Boxes/ie11
c3dbf8f  default virtualbox aborted  /Users/hide/Documents/Boxes/arch
50d2345  default virtualbox saved    /Users/hide/Documents/Boxes/ubn1804

The above shows information about all known Vagrant environments
on this machine. This data is cached and may not be completely
up-to-date (use "vagrant global-status --prune" to prune invalid
entries). To interact with any of the machines, you can go to that
directory and run Vagrant, or you can use the ID directly with
Vagrant commands from any directory. For example:
"vagrant destroy 1a2b3c4d"
~~~