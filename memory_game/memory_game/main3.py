import random
from time import sleep
import os
import msvcrt
import serial
from mqtt_messages import button_pressed 

button_pressed()

displayTime = .5

lights = ['yellow','red','green','blue']

print('Display the current button pressed:')
print(buttonPressed)
print('That was from the MQTT Messages script')

userInput = input("blabla enter")

if userInput == '1':
    print('This is the updated Button Press')
    print(buttonPressed)


    



