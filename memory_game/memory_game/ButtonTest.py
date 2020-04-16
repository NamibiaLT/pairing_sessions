# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from time import sleep
import serial

displayTime = 2
arduinoData = serial.Serial('COM10', 9600)
sleep(3)

def LED_raw(channel, value):
    message = '{"channels":[{"channel":%s,"value":%s}]}' % (channel, value)
    arduinoData.write(message.encode())

def LED(brightness, red, blue, green):
    message = '{"channels":[{"channel":1,"value":%s},{"channel":2,"value":%s},{"channel":3,"value":%s},{"channel":4,"value":%s}]}' % (brightness, red, blue, green)
    arduinoData.write(message.encode())

def LED_blink(color):
    
    if color == 1:
        message = '{"channels":[{"channel":1,"value":255},{"channel":2,"value":255},{"channel":3,"value":0},{"channel":4,"value":0}]}'
        arduinoData.write(message.encode())    
    if color == 3:
        message = '{"channels":[{"channel":1,"value":255},{"channel":2,"value":0},{"channel":3,"value":0},{"channel":4,"value":255}]}'
        arduinoData.write(message.encode())    
    if color == 2:       
        message = '{"channels":[{"channel":1,"value":255},{"channel":2,"value":0},{"channel":3,"value":255},{"channel":4,"value":0}]}'
        arduinoData.write(message.encode()) 
    sleep(0.2)
    message = '{"channels":[{"channel":1,"value":0},{"channel":2,"value":0},{"channel":3,"value":0},{"channel":4,"value":0}]}'
    arduinoData.write(message.encode())                


LED_blink(1)
sleep(0.2)
LED_blink(2)
sleep(0.2)
LED_blink(3)

def light_test():
    print('Simon box light test begin.')
    lights = ['yellow','red','green','blue']
    
    for x in range(0,2):
        for color in lights:
            topicNow = "simonbox/lights/" + color
            publish.single(topicNow,"on",hostname='192.168.0.109') 
            sleep(.3)
            publish.single(topicNow,"off",hostname='192.168.0.109')
            sleep(.3)
    
    print('Simon box light test end.')    

button = 'black'
def button_pressed(color):
    global button
    button = str(color)



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("simonbox/buttons/yellow")
    client.subscribe("simonbox/buttons/red") 
    client.subscribe("simonbox/buttons/green") 
    client.subscribe("simonbox/buttons/blue") 
    client.subscribe("onebox/button")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload.decode("utf-8")))

    if msg.topic == 'simonbox/buttons/yellow':
        if msg.payload.decode("utf-8") == 'pressed':
            print("I heard yellow button pressed.")
            LED(255,255,255,0)
            sleep(0.2)
            LED(0,0,0,0)
            button_pressed('yellow')    

    if msg.topic == "simonbox/buttons/red":    
        if msg.payload.decode("utf-8") == 'pressed':
            print("I heard red button pressed.")
            LED_blink(1)
            light_test()

    if msg.topic == "simonbox/buttons/green":       
        if msg.payload.decode("utf-8") == 'pressed':
            print("I heard green button pressed.")
            LED_blink(3)

    if msg.topic == "simonbox/buttons/blue": 
        if msg.payload.decode("utf-8") == 'pressed':
            print("I heard blue button pressed.")
            LED_blink(2)

    if msg.topic == "onebox/button": 
        if msg.payload.decode("utf-8") == "pressed":
            print("I heard button from button box 1 was pressed")
            LED_blink(1)
            sleep(0.1)
            LED_blink(2)
            sleep(0.1)
            LED_blink(3)
            LED_blink(1)
            sleep(0.1)
            LED_blink(2)
            sleep(0.1)
            LED_blink(3)    


    userInput = input('Enter Value:')    
    if userInput == '1':
        print("Yes it worked")
        print(button)       
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect('192.168.0.109', 1883, 60)

print (on_message)
if on_message == 'Yellow':
    print('WOOOHOOO')

print(button_pressed)




# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()