nMQTT: Subscribeできない

- [nmqtt](https://github.com/markallanson/nmqtt) をさわってみた
- プロトコルレベル = 3 でちょっと古いようです


# MqttConnectMessage

~~~
10-11-00-06-4D-51-49-73-64-70-03-02-00-1E-00-03-61-6E-79
~~~

- 10: 0x10 == CONNECT
- 11: 17バイトのメッセージ
- 00-06 : 6バイトの Protocol Name が続く([UTF-8 encoding string長](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/cos02/mqtt-v3.1.1-cos02.html#_Toc398718016))
- 4D-51-49-73-64-70 : 

~~~
    >>> binascii.unhexlify('4D-51-49-73-64-70'.replace('-',''))
    'MQIsdp
~~~

- 03: MQIsdp なので、 Protocol Level = 3
- 02: Clean Session(0x02)だけが Connect Flagsに設定されている
- 00-1E: Keep Alive = 30秒
- 00-03: Payload サイズ = 3バイト (UTF-8 encoding string 長)
- 61-6E-79: Payload はClientId(=any)だけ指定されている(明示的に指定した)

~~~
    >>> binascii.unhexlify('61-6E-79'.replace('-',''))
    'any'
~~~    

問題ないような気が。

# MqttSubscribeMessage

~~~
80-14-00-01-00-0F-6D-79-2F-74-6F-70-69-63-2F-73-74-72-69-6E-67-00
~~~

- 80: 0x80 == SUBSCRIBE
- 14: 20バイトのメッセージ
- 00-01: パケット識別子
- 00-0F: [UTF-8 encoding string長](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/cos02/mqtt-v3.1.1-cos02.html#_Toc398718016)
- 0F-6D-79-2F-74-6F-70-69-63-2F-73-74-72-69-6E-67: トピック(my/topic/string)
- 00 : Topic QoS バイト

~~~
>>> binascii.unhexlify('6D-79-2F-74-6F-70-69-63-2F-73-74-72-69-6E-67'.replace('-',''))
'my/topic/string'
~~~

コントロールパケットタイプが 0x82 じゃなければいけないような(0x02はControl Packet Type Flag)

# Control Packet Type Flag

[2.2.2. Flags](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/cos02/mqtt-v3.1.1-cos02.html#_Toc398718022) を参考にとりあえず、Flagを追加してみた。

Nmqtt.MqttHeader:

~~~csharp:MqttHeader.cs

		static byte[] ControlPacketFlag = new byte[16]{
			0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0
		};
			
        /// <summary>
        ///     Gets the value of the Mqtt header as a byte array
        /// </summary>
        private List<byte> HeaderBytes {
            get {
                var headerBytes = new List<byte>();

                // build the bytes that make up the header. The first byte is a combination of message type, dup,
                // qos and retain, and the follow bytes (up to 4 of them) are the size of the payload + variable header.
                headerBytes.Add(
                    (byte)
					((((int) MessageType) << 4) 
						+ ControlPacketFlag [(int)MessageType]			// ADD by HDKNR
						+ ((Duplicate ? 1 : 0) << 3) + (((int) Qos) << 1) + (Retain ? 1 : 0)));
                headerBytes.AddRange(GetRemainingLengthBytes());
                return headerBytes;
            }
        }
~~~        

- これでrabbitmq-mqttに接続後、PythonのPahoのパブリッシャーからメッセージもらえた
- フォークしてプロトコルレベル4で動作確認必要
