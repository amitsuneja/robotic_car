import RPi.GPIO as GPIO
from clearscr import clear_screen
from car_logger import log_warning, log_critical, log_error, clear_logs
from car_moves import forward,  backward, immediate_stop_car, change_duty_cycle, licence_cancel, init_car, procedural_stop_car, turn_car
from ultrasonic import check_distance

def print_menu():
    log_warning("\nS-hand brakes\ns-stop\nf-forward\nb-backward\ne-exit\nl-left_turn\nr-right_turn\nd-check back distance")



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
        elif x=='l':
            turn_car(en_a,in1,in2,in3,in4,en_b,p_a,p_b,direction="left")
            x='z'
            print_menu()
        elif x=='r':
            turn_car(en_a,in1,in2,in3,in4,en_b,p_a,p_b,direction="right")
            x='z'
            print_menu()
        elif x=='d':
            distance=check_distance()
            print(distance)
            x='z'
        elif x=='e':
            GPIO.cleanup()
            break
        else:
            licence_cancel()
            x='z'
            print_menu()
