import RPi.GPIO as GPIO
import time

TIME_IMPULS    = 0.00001 #Echo impuls in seconds
TIME_SETTLE    = 0.5     #Time to settle Distance sensor
SOUND_CM_S     = 34326   #constant for speed of sound in room
COLLISION_DIST = 30      #Collision distance in cm
DETECT_RANGE   = 0.0056  #Detection Range for 1m
DETECT_MIN     = 0.00058
FILT_DEPTH     = 4       #Depth of moving average filter for distance

IO_TRIG=17           #IO Pin to put out echo impuls
IO_ECHO=18           #IO Pin to measure echo impuls

class Cas(object):
    'Collision avoidannce system'

    def __init__(self):
        GPIO.setup(IO_TRIG, GPIO.OUT)
        GPIO.setup(IO_ECHO, GPIO.IN)

        #let Distance Sensor settle
        GPIO.output(IO_TRIG, GPIO.LOW)
        
        self._settlestart = time.time()
        self._distance = 0

    def update(self):
        settlestop = time.time()

        if (settlestop - self._settlestart) > TIME_SETTLE:
            # send echo impuls
            GPIO.output(IO_TRIG, GPIO.HIGH)
            time.sleep(TIME_IMPULS)
            GPIO.output(IO_TRIG, GPIO.LOW)

            # measure echo impuls
            nstart = time.time()

            while GPIO.input(IO_ECHO) == 0:
                start = time.time()

            while GPIO.input(IO_ECHO) == 1:
                stop = time.time()

                # obstacle to far to measure
                if stop - start >= DETECT_RANGE:
                    stop = start
                    break

            # calculate obstacle distance
            elapsed = stop - start

            if DETECT_MIN < elapsed:
                self._distance = (elapsed * SOUND_CM_S) / 2

                print "%f %f" % (self._distance, elapsed)

            # start next settle interval while echo is off
            self._settlestart = time.time()


    def get_distance(self):
        return self._distance

    def is_collision_alert(self):
        if self._distance > 0 and self._distance < COLLISION_DIST:
            return True
        else:
            return False

    def clear(self):
        self._distance = 0
