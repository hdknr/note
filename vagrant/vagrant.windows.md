# Windows


## VirtualBox

- https://www.virtualbox.org/wiki/Downloads

## scoop

~~~ps1
PS C:\Users\hdknr> Set-ExecutionPolicy RemoteSigned -scope CurrentUser
PS C:\Users\hdknr> iwr -useb get.scoop.sh | iex
~~~

~~~ps1
PS> scoop install curl
PS> scoop install openssh
PS> scoop install git-with-openssh
~~~

~~~ps1
PS> scoop bucket add extras
PS> scoop install vscode
~~~

## vagrant

~~~ps1
PS C:\Users\hdknr> vagrant plugin install vagrant-vbguest
PS C:\Users\hdknr> vagrant plugin install vagrant-winnfsd
~~~

