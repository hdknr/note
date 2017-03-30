

## xcodebuild でSDKの確認

- [How to asssociate iOS 9.0 SDK with Xamarin to compile the default application?](http://stackoverflow.com/questions/36278613/how-to-asssociate-ios-9-0-sdk-with-xamarin-to-compile-the-default-application)

~~~bash
$ xcodebuild -showsdks
OS X SDKs:
        OS X 10.11                      -sdk macosx10.11

iOS SDKs:
        iOS 9.2                         -sdk iphoneos9.2

iOS Simulator SDKs:
        Simulator - iOS 9.2             -sdk iphonesimulator9.2

tvOS SDKs:
        tvOS 9.1                        -sdk appletvos9.1

tvOS Simulator SDKs:
        Simulator - tvOS 9.1            -sdk appletvsimulator9.1

watchOS SDKs:
        watchOS 2.1                     -sdk watchos2.1

watchOS Simulator SDKs:
        Simulator - watchOS 2.1         -sdk watchsimulator2.1
~~~

## Xamarin よりデバッガを起動できない

~~~bash
Please ensure your device is connected...
Connected to: iPhone4h
warning MT1003:
Could not kill the application 'jp.co.lafoglia.lealea'.
You may have to kill the application manually.

warning MT1108:
Could not find developer tools for this 9.3.1 (13E238) device.
Please ensure you are using a compatible Xcode version
and then connect this device to Xcode to install the development support files.

error MT1007:
Failed to launch the application 'jp.co.lafoglia.lealea' on the device 'iPhone4h':
Look for earlier warnings returned: 0x454.
You can still launch the application manually by tapping on it.

~~~
