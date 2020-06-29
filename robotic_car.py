import RPi.GPIO as GPIO          
from os import system, name 
from time import sleep
from car_logger import log_warning, log_critical, log_error, clear_logs


#######################################################################################################
# CABLING DETAILS
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
GPIO.setmode(GPIO.BOARD)
en_a = 22
in1 = 16
in2 = 18
in3 = 11
in4 = 13
en_b = 15
temp1=1
min_duty_cycle = 25

def clear_screen():
    if name == 'nt':      # for windows
        _ = system('cls')
    else:                 # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

def forward():
    log_warning("forwarding a car")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def backward():
    log_warning("backwarding a car")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)

def stop():
    log_warning("your car is stopped")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def change_duty_cycle(duty_cycle):
    log_warning("changing speed to {}".format(duty_cycle))
    p_a.ChangeDutyCycle(duty_cycle)
    p_b.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    clear_screen()
    en_a = 22
    in1 = 16
    in2 = 18
    in3 = 11
    in4 = 13
    en_b = 15
    temp1=1
    min_duty_cycle = 25
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(en_a,GPIO.OUT)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en_b,GPIO.OUT)
    stop()
    p_a=GPIO.PWM(en_a,1000)
    p_b=GPIO.PWM(en_b,1000)
    p_a.start(25)
    p_b.start(25)
    log_warning("The default speed & direction of motor is LOW & Forward.....")
    log_warning("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    while(1):
        x=input()
        if x=='r':
            print("run")
            if(temp1==1):
                forward()
                x='z'
            else:
                backward()
                x='z'
        elif x=='s':
            stop()
            x='z'
        elif x=='f':
            forward()
            temp1=1
            x='z'
        elif x=='b':
            backward()
            temp1=0
            x='z'
        elif x=='l':
            change_duty_cycle(25)
            x='z'
        elif x=='m':
            change_duty_cycle(50)
            x='z'
        elif x=='h':
            change_duty_cycle(75)
            x='z'
        elif x=='e':
            GPIO.cleanup()
            break
        else:
            log_error("<<<  ERROR : YOUR LICENCE MAY CANCEL   >>>")
            log_warning("please enter the defined data to continue.....")
