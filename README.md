# robotic_car
This repo is creating a auto driven car

# CABLING CONNECTION Details
 NOTE - ENA and ENB only required if you want to control speed .

 NOTE - Cell supply should be more then 12V ( 2Cell*9V)

 NOTE - Powerbank is required to supply power to raspberry pi

 NOTE - GPIO_PIN_4_5V - FAN_RED_CABLE , GPIO_PIN_4_GRD - FAN_BLACK_CABLE

 NOTE -  Motor Driver can controll 2 motors at a time.

Motor driver :
-------------

 Motor driver have 3 main pins named as: 12V, grd and 5v.

 12V to cell +ve (9V*2Cells) - RED CABLE

 grd to cell -ve(9V*2Cells)- BLACK CABLE

 grd to GPIO_PIN_14 - BLACK CABLE
 
 5V to GPIO_PIN_2 - RED CABLE
 
 Motor Driver have 6 main ports : ENA, IN1, IN2, IN3, IN4, ENB

 ENA - GPIO_PIN_22 - Green Cable

 IN1 - GPIO_PIN_16 - white Cable

 IN2 - GPIO_PIN_18 - Yellow Cable

 IN3 - GPIO_PIN_11 - voilet Cable

 IN4 - GPIO_PIN_13 - Grey Cable

 ENB - GPIO_PIN_15 - Blue Cable


GPS MODULE 
-----------

It has 4 main ports named as VCC , RX, TX , GRD

VCC  - connected to 5V motor driver - RED COLOR CABLE 

RX   - Connected to GPIO_PIN_29 - White Cable - This is not required , cab be skipped . We connected it for future purpose.

TX   - Connected to GPIO_PIN_31 - GREY Cable

GRD - connected to GRD motor driver - BLACK COLOR CABLE 

HC-SR04 Module
-------------
it has 4 main ports named as VCC ,Trig , ECHo , GRD

VCC - connected to 5V motor driver - RED COLOR CABLE 

TRIG - Connected to GPIO_PIN_36 - Orange Color Cable 

ECHO - Connected to GPIO_PIN_38 - YELLOW COLOR cable - 1 Kilo oms Register is connected to it to reduce the current as it send back 5v signal which may harm GPIO pins .to prevent the same we used register.

GRD - - connected to GRD motor driver - BLACK COLOR CABLE 


PCA9685 - 16 Channel Module 
---------------------------
Note - you can connect 16 servo motors to raspberry pi via this channel , I have used 2 servo motors to move camera up,down and left,right.

it has 2 ports and then 6 main ports.

2 Ports - VCC and GRD - VCC goes to 12V Motor Driver side and GRD connected to GPIO_PIN_34

6 ports are named as -  V+ , VCC , SDA, SCL ,OE and GRD

V+ -> not in use/ not connected 

VCC - COnnected to 5V Motor driver. RED Cable

SDA - Connected to GPIO_PIN_3 - White color cable (This cant be changed with any other GPIO PIN)

SCL - Connected to GPIO_PIN_5 - GREEN COLOR Cable (This cant be changed with any other GPIO PIN)

OE - Not connected

GRD - COnneced to GPIO_PIN_34 -Black Cable

Servo Motor 
-----------
Each Servo motor have 3 cables . Brown , red and orange .
Brown is ground , Red is power volt and Orange is for signal. 
Servos are connected to PCA9685 16 Channel Module

