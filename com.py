#!/usr/bin/env python
import paho.mqtt.client as mqtt
from threading import Thread

import cfg


def on_connect(client, userdata, rc):
    print("connected with result code " + str(rc))
    client.subscribe("robo/ctrl/1")

    
def on_message(client, userdata, msg):

    # enter critical region...
    
    if not cfg.queue.full():
        
        # enqueue incoming control command
        cfg.queue.put(msg.payload, False)
        print "prodcue queue... ", msg.topic + ":" + str(msg.payload)

    
class Com(Thread):
    '''robot com thread (mqtt)'''
    def __init__(self):
        super(Com, self).__init__()
        
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message

        self.client.connect("test.mosquitto.org", 1883, 60)

    def run(self):
        print "run com thread..."
        self.client.loop_forever()
