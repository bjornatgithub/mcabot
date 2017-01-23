from syslog import syslog

import cfg
import motor

handler = {cfg.FOR : goForward, cfg.BACK : goBackward, cfg.RIGHT : goRight, cfg.LEFT : goLeft cfg.STOP : stop\
           cfg.G1 : setGear1, cfg.G2 : setGear2, cfg.G3 : setGear3 cfg.G4 : setGear4}
gear    = MOTOR_GEAR1


def goForward():
    cfg.drive.forward(gear)

    
def goBackward():
    cfg.drive.backward(gear)

    
def goRight():
    cfg.drive.right(gear)

    
def gosoftRight():
    cfg.drive.softright(gear)

    
def goLeft():
    cfg.drive.lef(gear)

    
def gosoftLeft():
    cfg.drive.softleft(gear)


def stop():
    cfg.drive.stop()


def setGear1():
    gear = motor.MOTOR_GEAR1


def setGear2():
    gear = motor.MOTOR_GEAR2


def setGear3():
    gear = motor.MOTOR_GEAR3


def setGear4():
    gear = motor.MOTOR_GEAR4
    

def updateRemote(command):
    
    if cfg.isRemoteSubCommand():

        # execute next move...
        handler[command]()

    else:
        # handle protocol error
        syslog("unknown subcommand")
