#!/usr/bin/env python
from threading import Thread

import cfg
from trackcontrol import updateTrack
from remotecontrol import updateRemote

handler = { RMT: updateRemote, TRCK: updateTrack}

class Control(Thread):
    '''robot control thread'''
    def __init__(self):
        super(ctrl_thread, self).__init__()
        self.data = []

    def run(self):

        print "run control thread..."

        while True:
            # enter critical region...

            if not cfg.queue.empty():
                
                payloadstr = cfg.queue.get(False)
                payloadlst = payloadstr(":")

                self.cmd    = payload[0]
                self.subcmd = payload[1]

                print "consum queue... ", payloadstr

                # execute robot control command...
                handler[self.cmd](self.subcmd)
