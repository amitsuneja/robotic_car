import RPi.GPIO as GPIO          
from car_logger import log_warning, log_critical, log_error, clear_logs



#######################################################################################################
# CABLING CONNECTIONS
#######################################################################################################
# Motor driver have 3 main pins : 12V, grd and 5v.
# 12V to cell +ve
# grd to cell -ve
# grd to GPIOPIN14
# 5V to GPIOPIN2 
# Motor Drviver can controll 2 motors at a time.
# Motor Drviver have 6 main ports : ENA, IN1, IN2, IN3, IN4, ENB
# ENA - GPIO_PIN_22 - Green Cable
# IN1 - GPIO_PIN_16 - white Cable
# IN2 - GPIO_PIN_18 - Yellow Cable
# IN3 - GPIO_PIN_11 - voilet Cable
# IN4 - GPIO_PIN_13 - Grey Cable
# ENB - GPIO_PIN_15 - Blue Cable
# ENA and ENB only required if you want to control speed .
# Cell supply should be more then 12V ( 2Cell*9V)
# Powerbank is required to supply power to raspberry pi
#######################################################################################################
def init_car():
    en_a = 22
    in1 = 16
    in2 = 18
    in3 = 11
    in4 = 13
    en_b = 15
    min_speed = 25
    max_speed = 75
    mid_speed = 50
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(en_a,GPIO.OUT)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en_b,GPIO.OUT)
    immediate_stop_car(en_a,in1,in2,in3,in4,en_b)
    p_a=GPIO.PWM(en_a,1000)
    p_b=GPIO.PWM(en_b,1000)
    p_a.start(25)
    p_b.start(25)
    car_list = [en_a, in1, in2, in3, in4, en_b, min_speed, max_speed, mid_speed, p_a, p_b]
    return car_list
    
def forward(en_a,in1,in2,in3,in4,en_b):
    log_warning("forwarding a car")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def backward(en_a,in1,in2,in3,in4,en_b):
    log_warning("backwarding a car")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)

def immediate_stop_car(en_a,in1,in2,in3,in4,en_b):
    log_warning("your car is stopped")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def procedural_stop_car(en_a,in1,in2,in3,in4,en_b):
    pass

def change_duty_cycle(speed,p_a,p_b):
    log_warning("changing speed to {}".format(speed))
    p_a.ChangeDutyCycle(speed)
    p_b.ChangeDutyCycle(speed)

def licence_cancel():
    log_error("<<<  ERROR : YOUR LICENCE MAY CANCEL   >>>")
    log_warning("please enter the defined data to continue.....")
