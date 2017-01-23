#!/usr/bin/env python
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import paho.mqtt.client as mqtt

import cfg

client = mqtt.Client("python_pub")
client.connect("test.mosquitto.org", 1883)

client.publish("robo/ctrl/1", cfg.RMT + ":" + cfg.FOR)
client.loop(2)
