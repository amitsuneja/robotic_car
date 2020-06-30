# robotic_car
This repo is creating a auto driven car

# CABLING CONNECTION Details

 Motor driver have 3 main pins : 12V, grd and 5v.

 12V to cell +ve

 grd to cell -ve

 grd to GPIOPIN14

 5V to GPIOPIN2

 Motor Drviver can controll 2 motors at a time.

 Motor Drviver have 6 main ports : ENA, IN1, IN2, IN3, IN4, ENB

 ENA - GPIO_PIN_22 - Green Cable

 IN1 - GPIO_PIN_16 - white Cable

 IN2 - GPIO_PIN_18 - Yellow Cable

 IN3 - GPIO_PIN_11 - voilet Cable

 IN4 - GPIO_PIN_13 - Grey Cable

 ENB - GPIO_PIN_15 - Blue Cable

 ENA and ENB only required if you want to control speed .

 Cell supply should be more then 12V ( 2Cell*9V)

 Powerbank is required to supply power to raspberry pi
