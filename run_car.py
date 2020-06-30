import RPi.GPIO as GPIO
from clearscr import clear_screen
from car_logger import log_warning, log_critical, log_error, clear_logs
from car_moves import forward,  backward, immediate_stop_car, change_duty_cycle, licence_cancel, init_car

if __name__ == "__main__":
    clear_screen()
    temp_var=1
    en_a, in1, in2, in3, in4, en_b, min_speed, max_speed, mid_speed, p_a, p_b = init_car()
    log_warning("The default speed & direction of motor is LOW & Forward.....")
    log_warning("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    while(1):
        x=input()
        if x=='r':
            print("run")
            if(temp_var==1):
                forward(en_a,in1,in2,in3,in4,en_b)
                x='z'
            else:
                backward(en_a,in1,in2,in3,in4,en_b)
                x='z'
        elif x=='s':
            immediate_stop_car(en_a,in1,in2,in3,in4,en_b)
            x='z'
        elif x=='f':
            forward(en_a,in1,in2,in3,in4,en_b)
            temp_var=1
            x='z'
        elif x=='b':
            backward(en_a,in1,in2,in3,in4,en_b)
            temp_var=0
            x='z'
        elif x=='l':
            change_duty_cycle(min_speed,p_a,p_b)
            x='z'
        elif x=='m':
            change_duty_cycle(min_speed,p_a,p_b)
            x='z'
        elif x=='h':
            change_duty_cycle(max_speed,p_a,p_b)
            x='z'
        elif x=='e':
            GPIO.cleanup()
            break
        else:
            licence_cancel()
