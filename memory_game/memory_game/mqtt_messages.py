import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

buttonPressed = 'black'
def button_pressed(color):
    global buttonPressed
    buttonPressed = str(color)


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
            #print("I heard yellow button pressed.")
            button_pressed('yellow')    

    if msg.topic == "simonbox/buttons/red":    
        if msg.payload.decode("utf-8") == 'pressed':
            #print("I heard red button pressed.")
            button_pressed('red') 

    if msg.topic == "simonbox/buttons/green":       
        if msg.payload.decode("utf-8") == 'pressed':
            #print("I heard green button pressed.")
            button_pressed('green') 

    if msg.topic == "simonbox/buttons/blue": 
        if msg.payload.decode("utf-8") == 'pressed':
            #print("I heard blue button pressed.")
            button_pressed('blue') 

    if msg.topic == "onebox/button": 
        if msg.payload.decode("utf-8") == "pressed":
            print("I heard button from button box 1 was pressed")
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect('192.168.0.109', 1883, 60)

client.loop_forever()