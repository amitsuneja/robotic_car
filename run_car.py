import RPi.GPIO as GPIO
from clearscr import clear_screen
from car_logger import log_warning, log_critical, log_error, clear_logs
from car_moves import forward,  backward, immediate_stop_car, change_duty_cycle, licence_cancel, init_car, procedural_stop_car, print_menu

if __name__ == "__main__":
    clear_screen()
    en_a, in1, in2, in3, in4, en_b, min_speed, max_speed, mid_speed, p_a, p_b = init_car()
    log_warning("The default speed is 1 & Forward.....")
    print_menu()
    while(1):
        x=input()
        if x=='S':
            immediate_stop_car(en_a,in1,in2,in3,in4,en_b)
            x='z'
            print_menu()
        elif x=='s':
            procedural_stop_car(en_a,in1,in2,in3,in4,en_b,p_a,p_b)
            print_menu()
        elif x=='f':
            forward(en_a,in1,in2,in3,in4,en_b,p_a,p_b)
            x='z'
            print_menu()
        elif x=='b':
            backward(en_a,in1,in2,in3,in4,en_b,p_a,p_b)
            x='z'
            print_menu()
        elif x=='e':
            GPIO.cleanup()
            break
        else:
            licence_cancel()
            x='z'
            print_menu()
