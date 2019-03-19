# git

- [chocolatey](../chocolatey) がインストールされていること

~~~bash
C:\Users\spin\Documents\Projects>cinst git
Chocolatey v0.10.11
Installing the following packages:
git
By installing you accept licenses for the packages.
Progress: Downloading git.install 2.19.1... 100%
Progress: Downloading chocolatey-core.extension 1.3.3... 100%
Progress: Downloading git 2.19.1... 100%

chocolatey-core.extension v1.3.3 [Approved]
chocolatey-core.extension package files install completed. Performing other installation steps.
 Installed/updated chocolatey-core extensions.
 The install of chocolatey-core.extension was successful.
  Software installed to 'C:\ProgramData\chocolatey\extensions\chocolatey-core'

git.install v2.19.1 [Approved]
git.install package files install completed. Performing other installation steps.
The package git.install wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

Using Git LFS
Installing 64-bit git.install...
git.install has been installed.
git.install installed to 'C:\Program Files\Git'
  git.install can be automatically uninstalled.
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (or in powershell/cmd.exe just type `refreshenv`).
 The install of git.install was successful.
  Software installed to 'C:\Program Files\Git\'

git v2.19.1 [Approved]
git package files install completed. Performing other installation steps.
 The install of git was successful.
  Software install location not explicitly set, could be in package or
  default install location if installer.

Chocolatey installed 3/3 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

C:\Users\spin\Documents\Projects>refreshenv
Refreshing environment variables from registry for cmd.exe. Please wait...Finished..
~~~

~~~bash
C:\Users\spin\Documents\Projects>git --version
git version 2.19.1.windows.1
~~~