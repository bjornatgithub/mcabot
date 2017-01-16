import time
import RPi.GPIO as GPIO

IO_CTRL_BUTT=25
IO_STAT_LED=22
IO_COL_LED=23
IO_ALERT_BUZZ=24


class Env(object):
    'Enviroment control'
    def __init__(self):
        self._is_on = False

        GPIO.setup(IO_CTRL_BUTT, GPIO.IN)
        GPIO.setup(IO_STAT_LED, GPIO.OUT)
        GPIO.setup(IO_COL_LED, GPIO.OUT)
        GPIO.setup(IO_ALERT_BUZZ, GPIO.OUT)

        GPIO.output(IO_STAT_LED, GPIO.LOW)
        GPIO.output(IO_COL_LED, GPIO.LOW)
        GPIO.output(IO_ALERT_BUZZ, GPIO.LOW)
        
    def status_on(self):
        GPIO.output(IO_STAT_LED, GPIO.HIGH)

    def status_off(self):
        GPIO.output(IO_STAT_LED, GPIO.LOW)        

    def alert(self):
        GPIO.output(IO_ALERT_BUZZ, GPIO.HIGH)

    def clear_alert(self):
        GPIO.output(IO_ALERT_BUZZ, GPIO.LOW)

    def collision_alert(self):
        GPIO.output(IO_COL_LED, GPIO.HIGH)

    def collision_clear(self):
        GPIO.output(IO_COL_LED, GPIO.LOW)


    def is_ctrl_on(self):
        if False == GPIO.input(IO_CTRL_BUTT):
            if False == self._is_on:
                self._is_on = True
            else:
                time.sleep(0.5)
                if False == GPIO.input(IO_CTRL_BUTT):
                    self._is_on = False
                    time.sleep(0.5)

        return self._is_on

        
