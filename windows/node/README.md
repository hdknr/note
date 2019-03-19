# nvm  + node

- [chocolatey](../chocolatey) でインストール

~~~bash
C:\Users\spin>powershell start-process cmd -verb runas
~~~

~~~bash
Microsoft Windows [Version 10.0.17134.407]
(c) 2018 Microsoft Corporation. All rights reserved.
~~~

~~~bash
C:\windows\system32>choco install nvm
Chocolatey v0.10.11
Installing the following packages:
nvm
By installing you accept licenses for the packages.
Progress: Downloading nvm.portable 1.1.7... 100%
Progress: Downloading nvm 1.1.5... 100%

nvm.portable v1.1.7 [Approved]
nvm.portable package files install completed. Performing other installation steps.
The package nvm.portable wants to run 'chocolateyinstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

Downloading nvm
  from 'https://github.com/coreybutler/nvm-windows/releases/download/1.1.7/nvm-noinstall.zip'
Progress: 100% - Completed download of C:\Users\spin\AppData\Local\Temp\chocolatey\nvm.portable\1.1.7\nvm-noinstall.zip (2.3 MB).
Download of nvm-noinstall.zip (2.3 MB) completed.
Hashes match.
Extracting C:\Users\spin\AppData\Local\Temp\chocolatey\nvm.portable\1.1.7\nvm-noinstall.zip to C:\ProgramData\nvm...
C:\ProgramData\nvm
PATH environment variable does not have %NVM_HOME% in it. Adding...
PATH environment variable does not have %NVM_SYMLINK% in it. Adding...
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (or in powershell/cmd.exe just type `refreshenv`).
 The install of nvm.portable was successful.
  Software installed to 'C:\ProgramData\nvm'

nvm v1.1.5 [Approved]
nvm package files install completed. Performing other installation steps.
 The install of nvm was successful.
  Software install location not explicitly set, could be in package or
  default install location if installer.

Chocolatey installed 2/2 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
~~~

~~~bash
C:\windows\system32>nvm list available

|   CURRENT    |     LTS      |  OLD STABLE  | OLD UNSTABLE |
|--------------|--------------|--------------|--------------|
|    11.2.0    |   10.13.0    |   0.12.18    |   0.11.16    |
|    11.1.0    |    8.12.0    |   0.12.17    |   0.11.15    |
|    11.0.0    |    8.11.4    |   0.12.16    |   0.11.14    |
|   10.12.0    |    8.11.3    |   0.12.15    |   0.11.13    |
|   10.11.0    |    8.11.2    |   0.12.14    |   0.11.12    |
|   10.10.0    |    8.11.1    |   0.12.13    |   0.11.11    |
|    10.9.0    |    8.11.0    |   0.12.12    |   0.11.10    |
|    10.8.0    |    8.10.0    |   0.12.11    |    0.11.9    |
|    10.7.0    |    8.9.4     |   0.12.10    |    0.11.8    |
|    10.6.0    |    8.9.3     |    0.12.9    |    0.11.7    |
|    10.5.0    |    8.9.2     |    0.12.8    |    0.11.6    |
|    10.4.1    |    8.9.1     |    0.12.7    |    0.11.5    |
|    10.4.0    |    8.9.0     |    0.12.6    |    0.11.4    |
|    10.3.0    |    6.14.4    |    0.12.5    |    0.11.3    |
|    10.2.1    |    6.14.3    |    0.12.4    |    0.11.2    |
|    10.2.0    |    6.14.2    |    0.12.3    |    0.11.1    |
|    10.1.0    |    6.14.1    |    0.12.2    |    0.11.0    |
|    10.0.0    |    6.14.0    |    0.12.1    |    0.9.12    |
|    9.11.2    |    6.13.1    |    0.12.0    |    0.9.11    |
|    9.11.1    |    6.13.0    |   0.10.48    |    0.9.10    |

This is a partial list. For a complete list, visit https://nodejs.org/download/release
~~~

~~~bash
C:\windows\system32>nvm install 11.1.0
Downloading node.js version 11.1.0 (64-bit)...
Complete
Creating C:\ProgramData\nvm\temp

Downloading npm version 6.4.1... Complete
Installing npm v6.4.1...

Installation complete. If you want to use this version, type

nvm use 11.1.0
~~~

~~~bash
C:\windows\system32>nvm use 11.1.0
Now using node v11.1.0 (64-bit)

C:\windows\system32>node -v
v11.1.0
~~~

~~~bash
C:\windows\system32>npm install --global --production npm-windows-upgrade
C:\Program Files\nodejs\npm-windows-upgrade -> C:\Program Files\nodejs\node_modules\npm-windows-upgrade\bin\npm-windows-upgrade.js
+ npm-windows-upgrade@5.0.0
added 87 packages from 54 contributors in 19.055s
~~~

~~~bash
C:\windows\system32>npm-windows-upgrade --npm-version latest
npm-windows-upgrade v5.0.0

Scripts cannot be executed on this system.
To fix, run the command below as Administrator in PowerShell and try again:
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
~~~

~~~bash
C:\windows\system32>powershell "Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force"
~~~

~~~bash
C:\windows\system32>npm-windows-upgrade --npm-version latest
npm-windows-upgrade v5.0.0
Checked system for npm installation:
According to PowerShell: C:\Program Files\nodejs
According to npm:        C:\Program Files\nodejs
Decided that npm is installed in C:\Program Files\nodejs
Upgrading npm... |

Upgrade finished. Your new npm version is 6.4.1. Have a nice day!
~~~