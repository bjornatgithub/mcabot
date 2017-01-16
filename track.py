import RPi.GPIO as GPIO

# track sensor array
IO_SENSOR_1 = 25 # left sensor
IO_SENSOR_2 = 22  
IO_SENSOR_3 = 23 # center sensor
IO_SENSOR_4 = 27  
IO_SENSOR_5 = 24 # right sensor

ON_TRACK  = 0
OFF_TRACK = 1

class Track(object):

    def __init__(self):
        GPIO.setup(IO_SENSOR_1, GPIO.IN)
        GPIO.setup(IO_SENSOR_2, GPIO.IN)
        GPIO.setup(IO_SENSOR_3, GPIO.IN)
        GPIO.setup(IO_SENSOR_4, GPIO.IN)
        GPIO.setup(IO_SENSOR_5, GPIO.IN)

    def update(self):
        values = []
        values.append(GPIO.input(IO_SENSOR_1))
        values.append(GPIO.input(IO_SENSOR_2))
        values.append(GPIO.input(IO_SENSOR_3))
        values.append(GPIO.input(IO_SENSOR_4))
        values.append(GPIO.input(IO_SENSOR_5))
        
        return values
