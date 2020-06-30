import RPi.GPIO as GPIO          
from car_logger import log_warning, log_critical, log_error, clear_logs
from speedometer import update_speedometer, check_speedometer

min_speed = 25
max_speed = 75
mid_speed = 50


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
    init_speed = 1
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
    p_a.start(init_speed)
    p_b.start(init_speed)
    update_speedometer(init_speed)
    car_list = [en_a, in1, in2, in3, in4, en_b, min_speed, max_speed, mid_speed, p_a, p_b]
    return car_list
    
def forward(en_a,in1,in2,in3,in4,en_b,p_a,p_b,expected_speed=50):
    log_warning("forwarding a car")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    change_speed(p_a,p_b,expected_speed)

def change_speed(p_a,p_b,expected_speed):
    current_speed = check_speedometer()
    if (expected_speed > max_speed):
        expected_speed = max_speed
    if (current_speed <  expected_speed):
        while (current_speed != expected_speed):
            current_speed = current_speed + 1    
            change_duty_cycle(current_speed,p_a,p_b)
    if (current_speed > expected_speed):
        while (current_speed != expected_speed):
            current_speed = current_speed - 1
            change_duty_cycle(current_speed,p_a,p_b)

def backward(en_a,in1,in2,in3,in4,en_b,p_a,p_b,expected_speed=25):
    immediate_stop_car(en_a,in1,in2,in3,in4,en_b)
    log_warning("backwarding a car")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    current_speed = check_speedometer()
    if (current_speed > expected_speed):
        change_speed(p_a,p_b,expected_speed)
    if (current_speed < expected_speed):
        change_speed(p_a,p_b,expected_speed)

def immediate_stop_car(en_a,in1,in2,in3,in4,en_b):
    log_warning("your car is stopped immediately")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    update_speedometer(0)

def procedural_stop_car(en_a,in1,in2,in3,in4,en_b,p_a,p_b):
    expected_speed = 0
    change_speed(p_a,p_b,expected_speed)
    log_warning("your car is stopped procedurly")

def change_duty_cycle(speed,p_a,p_b):
    log_warning("changing speed to {}".format(speed))
    p_a.ChangeDutyCycle(speed)
    p_b.ChangeDutyCycle(speed)
    update_speedometer(speed) 
 

def licence_cancel():
    log_error("<<<  ERROR : YOUR LICENCE MAY CANCEL   >>>")

def print_menu():
    log_warning("\nS-hand brakes\ns-stop\nf-forward\nb-backward\ne-exit\nl-left_turn\nr-right_turn")

def turn_car(en_a,in1,in2,in3,in4,en_b,p_a,p_b,direction):
    current_speed = check_speedometer()
    if (current_speed > min_speed):
       change_speed(p_a,p_b,min_speed)
    if (direction == "left"):
       GPIO.output(in1,GPIO.LOW)
       GPIO.output(in3,GPIO.HIGH)
       GPIO.output(in2,GPIO.HIGH)
       GPIO.output(in4,GPIO.HIGH)
       log_warning("car is turning left")
    else:
       GPIO.output(in1,GPIO.HIGH)
       GPIO.output(in3,GPIO.LOW)
       GPIO.output(in2,GPIO.HIGH)
       GPIO.output(in4,GPIO.HIGH)
       log_warning("car is turning right")


  
    

