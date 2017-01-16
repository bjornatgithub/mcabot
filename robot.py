#!/usr/bin/env python

# general system includes...
import time
import RPi.GPIO as GPIO

# robo control modules
import env     # enviroment control (temperature, pressure, light)
import cas     # collision avoidance system (ultrasound collision detection)
import motor   # motor actor to move robot
import track   # tracking sensor to align on black track line
import com     # communication abstraction layer


# General Settings
SAMPLE_TIME  = 0.001 # sample time for robot control


class Robot(object):
        'robot control logic'

        def __init__(self):
                # global GPIO initialization
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)

                # moduls used for robot control...
                self._cas_sensor   = cas.Cas()
                self._track_sensor = track.Track()                
                self._motor_actor  = motor.Motor()
                self._com          = com()

        def run(self):

                # This is the control feedback loop (EVA von Neumann)
                # On this place a salute to van Neumann the old german fellow!!! ;)

                # E (Eingabe - Input)
                self._com.input()

                # V (Verarbeitung - execution, calculation, control)
                if "REMOTE" == self._com.get_cmd():
                        # this is your turn buddy...
                        
                        if "FOR" == self._com.get_attr():
                                print "move forward"

                                # here you can implement forward movage
                                
                        if "BACK" == self._com.get_attr():
                                print "move Backward"
                        if "LEFT" == self._com.get_attr():
                                print "move left"
                        if "RIGHT" == self._com.get_attr():
                                print "move right"

                elif "TRACK" == self._com.get_cmd():

                        # this is my turn
                        self.track()
                        time.sleep(SAMPLE_TIME)
                else:
                        # unknown command set error indication
                        print "unkown command received..."

                # A (Ausgabe - output)
                # set some feedback for the remote controler
                self._com.output()
                

# __main__
robi = Robot() # a robot called robi is born

while True:
        robi.run()
        time.sleep(SAMPLE_TIME)
