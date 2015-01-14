# iBeacon

- BLE (Bluetooth Low Energy)
- 認識距離 50-70m ( NFC は 20-40cm )

1. geofencing / region monitoring - 「誰かがレンジに入ってきたよ！」
2. proximity / ranging - 「近づいてきたよ！」

- ranging は　アプリがフォアグラウンドで動かすことが必要


# Bluetooth Generic Attribute Profile (GATT)


## Profile

- [Profiles Overview](https://developer.bluetooth.org/TechnologyOverview/Pages/Profiles.aspx#GATT)

## Service


### 識別子

- Official BLE Services : 16 bit UUID ([here](https://developer.bluetooth.org/gatt/services/Pages/ServicesHome.aspx) )
- Custom Services : 128 bit UUID


## Characteristics

- データ列

### 識別子

- [Standard Characteristics](https://developer.bluetooth.org/gatt/characteristics/Pages/CharacteristicsHome.aspx) : 16 bit
- Custom Characteristics : 128 bit UUID



## その他

- [データフォーマット](https://developer.bluetooth.org/gatt/Pages/FormatTypes.aspx)




# Reference

- [Building Cross-Platform iBeacon Apps for iOS, Android and Windows with C# and Xamarin](http://vincenth.net/blog/archive/2014/04/24/building-cross-platform-ibeacon-apps-for-ios-android-and-windows-with-c-and-xamarin.aspx)