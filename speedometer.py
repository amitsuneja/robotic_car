def update_speedometer(speed):
    with open('speedometer.log','w') as writer_handler:
         writer_handler.write(str(speed))

def check_speedometer():
    with open('speedometer.log','r') as reader_handler:
        for line in reader_handler:
            speed = line
    return speed
