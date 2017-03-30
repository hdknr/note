embedded.mobileprovision: UDID一覧

- テスト用IPAパッケージからUDIDを抜く

~~~bash
#!/bin/bash

CODE="
from plistlib import readPlist;
from sys import stdin;
print '\n'.join(readPlist(stdin)['ProvisionedDevices']);"

IPA=$1
GREP_OPTIONS=
exml=$(unzip -Z1 $IPA | grep mobileprovision)
unzip -p $IPA ${exml[0]} | security cms -D | python -c "$CODE"
~~~
