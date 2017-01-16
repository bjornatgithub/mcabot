import track
import motor


# Tracking settings
TRACK_SPEED  = motor.MOTOR_GEAR2   # Speed during tracking in duty cycles {0 to 100}

# PID constants
KP = 1
KI = 0
KD = 0

class Tracking(object):
    '''tracking algorithm'''
    def __init__(self, trackingsensor, motoractor):
        self._tracksensor          = trackingsensor
        self._motoractor           = motoractor
        self._track_I              = 0
        self._track_old_correction = 100

def track(self, tracksensor, motoractor):
    # get track status from tracking sensors...
    sensor_array = tracksensor.update()
    print sensor_array

    # correct based on tracking sensor input
    correction = 100

    #Note: order checking sensors is important, because outer sensors
    #weightening is higher...

    # check center sensor
    if track.ON_TRACK == sensor_array[2]:
        correction = self._calc_pid(0, 0)

    # check inner left and right sensors
    if track.ON_TRACK == sensor_array[1]:
        correction = self._calc_pid(0, 15)

    if track.ON_TRACK == sensor_array[3]:
        correction = self._calc_pid(0, -15)

    # check outer left and right sensors
    if track.ON_TRACK == sensor_array[0]:
        correction = self._calc_pid(0, 30)

    if track.ON_TRACK == sensor_array[4]:
        correction = self._calc_pid(0, -30)

    if (100 != correction) and (correction != self._track_old_correction):
        duty_offset = correction
                                
    if 0 > correction:
                                
        print "left: %i %i %i" % (correction, duty_offset, (TRACK_SPEED + duty_offset))
                                
        # left sensor array steer left                                
        motoractor.forward_left_wheel(TRACK_SPEED + duty_offset)
        motoractor.forward_right_wheel(TRACK_SPEED - duty_offset)
    else:
        print "right: %i %i %i" % (correction, duty_offset, (TRACK_SPEED + duty_offset))
                                
        # right sensor array steer right
        motoractor.forward_left_wheel(TRACK_SPEED + duty_offset)
        motoractor.forward_right_wheel(TRACK_SPEED - duty_offset)

    self._track_old_correction = correction



        def _calc_pid(self, target_pos, current_pos):
                # calculate error
                error = target_pos - current_pos

                # current error
                P = error * KP

                # accumulated error
                self._track_I = (self._track_I * error) * KI

                # error deviation
                D = (error - self._track_err) * KD

                return P + self._track_I + D
