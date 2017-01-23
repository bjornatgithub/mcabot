from syslog import syslog

import cfg
import motor

gear    = motor.MOTOR_GEAR1


def goForward():
    print "move forward"
    cfg.drive.forward(gear)

    
def goBackward():
    print "move backward"    
    cfg.drive.backward(gear)

    
def goRight():
    print "move right"
    cfg.drive.right(gear)

    
def gosoftRight():
    print "move soft right"
    cfg.drive.softright(gear)

    
def goLeft():
    print "move left"
    cfg.drive.lef(gear)

    
def gosoftLeft():
    print "move soft left"
    cfg.drive.softleft(gear)


def stop():
    print "move stop"
    cfg.drive.stop()


def setGear1():
    print "move gear1"
    gear = motor.MOTOR_GEAR1


def setGear2():
    print "move gear2"
    gear = motor.MOTOR_GEAR2


def setGear3():
    print "move gear3"
    gear = motor.MOTOR_GEAR3


def setGear4():
    print "move gear4"
    gear = motor.MOTOR_GEAR4


handler = {cfg.FOR : goForward, cfg.BACK : goBackward, cfg.RIGHT : goRight, cfg.LEFT : goLeft, cfg.STOP : stop,\
           cfg.G1 : setGear1, cfg.G2 : setGear2, cfg.G3 : setGear3, cfg.G4 : setGear4}


def updateRemote(command):
    
    if cfg.isRemoteSubCommand(command):
        # execute next move...
        handler[command]()

    else:
        # handle protocol error
        syslog("unknown subcommand")
