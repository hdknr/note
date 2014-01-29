Date: 2013-04-12 04:11
Title: python-phonenumbers が微妙に使えなかった

* 5桁の市外局番が対応されていないっぽい
* * あと、042だっけ？ 4桁で始まる市外局番と３桁のやつの両方があるのでうまくフォーマットできない。
* [81.txt](https://github.com/daviddrysdale/python-phonenumbers/blob/dev/resources/geocoding/ja/81.txt) をみると対応が古いんでしょう
* [JPメタデータ](https://github.com/daviddrysdale/python-phonenumbers/blob/dev/python/phonenumbers/data/region_JP.py) の編集が必要
* [本家](https://code.google.com/p/libphonenumber/source/browse/trunk/java/release_notes.txt#13)にはメタデータ更新ありますね