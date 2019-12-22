# dpd - Display Port daemon

~~~bash 
$ sudo launchctl list | grep dpd
-	0	com.apple.dpd
~~~


## ターゲットディスプレイモード

- [iMac をターゲットディスプレイモードでディスプレイとして使う - Apple サポート](https://support.apple.com/ja-jp/HT204592)

### command + F2」キーが機能しない場合

- `dpd` を再起動してみる

~~~bash
$ sudo launchctl stop com.apple.dpd
~~~


## launchd

~~~bash 
$ cat /System/Library/LaunchDaemons/com.apple.dpd.plist 
~~~

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.apple.dpd</string>

	<key>MachServices</key>
	<dict>
		<key>com.apple.dpd</key>
		<true/>
	</dict>

	<key>ProgramArguments</key>
	<array>
		<string>/usr/libexec/dpd</string>
	</array>

    <key>ThrottleInterval</key>
    <integer>1</integer>

    <key>POSIXSpawnType</key>
	<string>Adaptive</string>

	<key>LaunchEvents</key>
	<dict>
		<key>com.apple.iokit.matching</key>
		<dict>
			<key>com.apple.device-attach</key>
			<dict>
				<key>IOProviderClass</key>
				<string>IOACPIPlatformDevice</string>
				<key>IONameMatch</key>
				<string>smc-dppt</string>
				<key>IOMatchLaunchStream</key>
				<true/>
			</dict>
		</dict>
	</dict>

	<key>KeepAlive</key>
	<dict>
		<key>AfterInitialDemand</key>
		<true/>                         <!-- stopすると自動起動します -->
		<key>SuccessfulExit</key>
		<false/>
	</dict>
</dict>
</plist>
~~~