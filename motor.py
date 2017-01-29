import RPi.GPIO as GPIO
import syslog

MOTOR_GEAR1 = 30
MOTOR_GEAR2 = 50
MOTOR_GEAR3 = 60
MOTOT_GEAR4 = 70

# Motor control IO Pins...
IO_MOTOR_A_FWD =  9 #Right Motor A forward
IO_MOTOR_A_BWD = 10 #Right Motor A backward
IO_MOTOR_B_FWD =  8 #Left Motor B backward
IO_MOTOR_B_BWD =  7 #Left Motor B backward

# PWM settings
PWM_FREQ  = 400
PWM_ADJ_A = 1
PWM_ADJ_B = 1
PWM_STOP  = 0

class Motor(object):
    'Motor conrtoler'

    def __init__(self):
        GPIO.setup(IO_MOTOR_A_FWD, GPIO.OUT)
        GPIO.setup(IO_MOTOR_A_BWD, GPIO.OUT)
        GPIO.setup(IO_MOTOR_B_FWD, GPIO.OUT)
        GPIO.setup(IO_MOTOR_B_BWD, GPIO.OUT)
        
        self._pwm_a_fwd = GPIO.PWM(IO_MOTOR_A_FWD, PWM_FREQ)
        self._pwm_a_bwd = GPIO.PWM(IO_MOTOR_A_BWD, PWM_FREQ)
        self._pwm_b_fwd = GPIO.PWM(IO_MOTOR_B_FWD, PWM_FREQ)
        self._pwm_b_bwd = GPIO.PWM(IO_MOTOR_B_BWD, PWM_FREQ)

        self._pwm_a_fwd.start(PWM_STOP)
        self._pwm_a_bwd.start(PWM_STOP)
        self._pwm_b_fwd.start(PWM_STOP)
        self._pwm_b_bwd.start(PWM_STOP)


    # stop left and right wheel (setting all PWM duty cycles zero)
    def stop(self):
        self._pwm_a_fwd.ChangeDutyCycle(PWM_STOP)
        self._pwm_a_bwd.ChangeDutyCycle(PWM_STOP)
        self._pwm_b_fwd.ChangeDutyCycle(PWM_STOP)
        self._pwm_b_bwd.ChangeDutyCycle(PWM_STOP)
        

    # move forward 
    # input duty - duty cycle PWM {30 to 100}        
    def forward(self, duty):
        self.forward_left_wheel(duty)
        self.forward_right_wheel(duty)
    
    # move forward 
    # input duty - duty cycle PWM {30 to 100}        
    def backward(self, duty):
        self.backward_left_wheel(duty)
        self.backward_right_wheel(duty)

        
    # move left
    # input duty - duty cycle PWM {15 to 85}
    def left(self, duty):
        if (duty < 15) or (duty > 85):
            syslog.syslog("invalid duty for left turn")
            return
            
        self.forward_left_wheel(duty - 15)
        self.forward_right_wheel(duty + 15)
        

    # move right
    # input duty - duty cycle PWM {15 to 85}
    def right(self, duty):
        if (duty < 15) or (duty > 85):
            syslog.syslog("invalid duty for right turn")
            return
        
        self.forward_left_wheel(duty + 15)
        self.forward_right_wheel(duty - 15)


    # move soft left
    # input duty - duty cycle PWM {15 to 100}
    def softleft(self, duty):
        if (duty < 15) or (duty > 100):
            syslog.syslog("invalid duty for left turn")
            return
            
        self.forward_left_wheel(duty - 15)
        self.forward_right_wheel(duty)
        

    # move soft right
    # input duty - duty cycle PWM {15 to 100}                
    def softright(self, duty):
        if (duty < 15) or (duty > 100):
            syslog.syslog("invalid duty for right turn")
            return
        
        self.forward_left_wheel(duty)
        self.forward_right_wheel(duty - 15)        
        

    # move hard left (left wheel: duty + 30, right wheel duty - 30)
    # input duty - duty cycle PWM {30 to 70}                
    def hardleft(self, duty):
        if (duty < 30) or (duty > 70):
            syslog.syslog("invalid duty for hard left turn")
            return
        
        self.forward_left_wheel(duty - 30)
        self.forward_right_wheel(duty + 30)        

        
    # move left (left wheel: duty - 30, right wheel duty + 30)
    # input duty - duty cycle PWM {30 to 70}
    def hardright(self, duty):
        if (duty < 30) or (duty > 70):
            syslog.syslog("invalid duty for hard right turn")
            return
        
        self.forward_left_wheel(duty + 30)
        self.forward_right_wheel(duty - 30)


    # control forward speed of left wheel
    # input duty - duty cycle PWM {0 to 100}
    def forward_right_wheel(self, duty):
        duty = self._adjust_duty_range(duty * PWM_ADJ_A)
        self._pwm_a_fwd.ChangeDutyCycle(duty)
        

    # control forward speed of right wheel
    # input duty - duty cycle PWM {0 to 100}
    def forward_left_wheel(self, duty):        
        duty = self._adjust_duty_range(duty * PWM_ADJ_B)        
        self._pwm_b_fwd.ChangeDutyCycle(duty)
        

    # control backward speed of left wheel
    # input duty - duty cycle PWM {0 to 100}        
    def backward_right_wheel(self, duty):        
        duty = self._adjust_duty_range(duty * PWM_ADJ_B)                
        self._pwm_b_bwd.ChangeDutyCycle(duty)
        

    # control backward speed of right wheel
    # input duty - duty cycle PWM {0 to 100}        
    def backward_left_wheel(self, duty):        
        duty = self._adjust_duty_range(duty * PWM_ADJ_A)        
        self._pwm_a_bwd.ChangeDutyCycle(duty)

        
    def _adjust_duty_range(self, duty):
        new_duty = duty
        
        if duty > 100:
            new_duty = 100

        if duty < 0:
            new_duty = 0

        return new_duty
