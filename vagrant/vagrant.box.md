# イメージ

## `prune` : 不要なBoxを削除

~~~zsh
% vagrant box prune

The following boxes will be kept...
js2             (virtualbox, 0)
ubuntu/bionic64 (virtualbox, 20200701.0.0)
ubuntu/focal64  (virtualbox, 20201210.0.0)

Checking for older boxes...
Box 'ubuntu/bionic64' (v20191014.0.0) with provider 'virtualbox' appears
to still be in use by at least one Vagrant environment. Removing
the box could corrupt the environment. We recommend destroying
these environments first:

default (ID: 2a5c0c72d407408ab9915e6ec6fd9859)

Are you sure you want to remove this box? [y/N] y
Removing box 'ubuntu/bionic64' (v20191014.0.0) with provider 'virtualbox'...
Removing box 'ubuntu/focal64' (v20200814.0.0) with provider 'virtualbox'...
Box 'ubuntu/focal64' (v20200903.0.0) with provider 'virtualbox' appears
to still be in use by at least one Vagrant environment. Removing
the box could corrupt the environment. We recommend destroying
these environments first:

default (ID: 0e8fb1e4d849474281bcffee3f18a677)

Are you sure you want to remove this box? [y/N] y
Removing box 'ubuntu/focal64' (v20200903.0.0) with provider 'virtualbox'...
Removing box 'ubuntu/focal64' (v20200917.0.0) with provider 'virtualbox'...
~~~