import grovepi
import time
from grove_rgb_lcd import *

potentiometer = 0
ultrasonic_ranger = 6

while True:
   sensor_value = grovepi.analogRead(potentiometer)
   ultrasonic_value = grovepi.ultrasonicRead(ultrasonic_ranger)
   if(sensor_value > ultrasonic_value):
      setText(f"{sensor_value}cm OBJ PRES \n {ultrasonic_value}cm")
   else:
      setText(f"{sensor_value}cm \n {ultrasonic_value}cm")
   time.sleep(0.2)
