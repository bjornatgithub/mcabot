# general system includes...
from threading import Condition
import Queue

# Hardware Abstraction Layer imports
import env      # enviroment control (temperature, pressure, light)
import cas      # collision avoidance system (ultrasound sensor)
import motor    # motor actor to move
import irsensor # Infrared Sensor

# Hardware Abstraction Layer instances
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

remoteSubCommands = (FOR, BACK, RIGHT, LEFT)

def isCommand(cmd):
    return cmd in commands

def isRemoteSubCommand(cmd):
    return cmd in remoteSubCommands
