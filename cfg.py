# general system includes...
from threading import Condition
import Queue

# Hardware Abstraction Layer imports
import RPi.GPIO as GPIO
import env      # enviroment control (temperature, pressure, light)
import cas      # collision avoidance system (ultrasound sensor)
import motor    # motor actor to move
import irsensor # Infrared Sensor

# Hardware Abstraction Layer instances
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
drive = motor.Motor()

# shared memory inter thread communication
cond  = Condition()   # conditional synchronisation
queue = Queue.Queue() # shared commemory

# protocol
# command
RMT  = "remote"
TRCK = "track"
EXP  = "explore"
STAT = "status"

commands = (RMT, TRCK, EXP, STAT)

# RMT subcommand
FOR   = "f"
BACK  = "b"
RIGHT = "r"
LEFT  = "l"
STOP  = "s"
G1    = "1"
G2    = "2"
G3    = "3"
G4    = "4"

remoteSubCommands = (FOR, BACK, RIGHT, LEFT)

def isCommand(cmd):
    return cmd in commands

def isRemoteSubCommand(cmd):
    return cmd in remoteSubCommands
