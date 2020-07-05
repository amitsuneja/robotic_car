import serial
ser = serial.Serial('/dev/ttyUSB0', 4800)

while True:
    data = ser.readline()
    if data:
        print(data)
