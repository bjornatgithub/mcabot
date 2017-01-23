#!/usr/bin/env python
from syslog import syslog
from threading import Thread

import cfg
#from trackcontrol import updateTrack
from remotecontrol import updateRemote

handler = { cfg.RMT: updateRemote}

class Control(Thread):
    '''robot control thread'''
    def __init__(self):
        super(Control, self).__init__()
        self.data = []

    def run(self):

        print "run control thread..."

        while True:
            # enter critical region...

            if not cfg.queue.empty():
                payloadstr = cfg.queue.get(False)
                payloadlst = payloadstr.split(":")

                print "consum queue... ", payloadstr

                if 2 == len(payloadlst):
                    self.cmd    = payloadlst[0]
                    self.subcmd = payloadlst[1]

                    if cfg.isCommand(self.cmd):
                        # execute robot control command...
                        handler[self.cmd](self.subcmd)
                        
                    else:
                        syslog("unknown command")
                        
                else:
                    syslog("invalid protocol format")






