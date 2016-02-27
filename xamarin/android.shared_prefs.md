Android: shared_prefs 内容の確認

- 5.0 だと `adb exec-out` でファイル取り出せるようですが...
- とりあえず XMLをcatする
- XMLを json化して jq でクエリする

## bash alias

- tools.bash

~~~bash
# pip install xmltodict && sudo apt-get install jq
alias XJ='python -c "import xmltodict, json, sys; print json.dumps(xmltodict.parse(sys.stdin));"'

# shared_pref
alias PREF='adb shell "run-as ${DROID_PACKAGE} cat shared_prefs/${DROID_PACKAGE}_preferences.xml"'
~~~

~~~bash
$ source tools.bash
~~~

## string を取得

~~~
$ export DROID_PACKAGE=jp.lafoglia.droidmap
$ PREF | XJ | jq '.map.string["#text"]' -r

http://test.com:8000
~~~
