# https://gist.github.com/voluntas/8238751

import paho.mqtt.client as paho
import argparse
from datetime import datetime


def on_connect(mqttc, obj, rc):
    mqttc.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))


def on_log(mqttc, obj, level, string):
    print(string)


def main(args):
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish

    mqttc.connect(args.server, 1883, 60)
    mqttc.publish(args.topic, 
                  args.message, 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Paho Publisher')

    parser.add_argument("server", type=str, nargs='?', 
                        default="192.168.56.50", help="MQTT Server")
    parser.add_argument("topic", type=str, nargs='?', 
                        default="my/topic/string", help="Topic")
    parser.add_argument("message", type=str, nargs='?', 
                        default=datetime.now().strftime("Hello %c"),
                        help="Message")
    main(parser.parse_args())

