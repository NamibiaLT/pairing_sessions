#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#include <Button.h>

Button buttonYellow(D5);
Button buttonRed(D6);
Button buttonGreen(D7);
Button buttonBlue(D4);

const int LIGHT_YELLOW_PIN = D1;
const int LIGHT_RED_PIN = D2;
const int LIGHT_GREEN_PIN = D3;
const int LIGHT_BLUE_PIN = D8;

boolean buttonYellowState = 0;
boolean buttonRedState = 0;
boolean buttonGreenState = 0;
boolean buttonBlueState = 0;

const char* ssid = "HideYoKidsHideYoWifi";
const char* password = "15porternamibiajames";
const char* mqtt_server = "192.168.0.109";

const char* topic_simonbox_buttons_yellow = "simonbox/buttons/yellow";
const char* topic_simonbox_buttons_red = "simonbox/buttons/red";
const char* topic_simonbox_buttons_green = "simonbox/buttons/green";
const char* topic_simonbox_buttons_blue = "simonbox/buttons/blue";

const char* topic_simonbox_lights_yellow = "simonbox/lights/yellow";
const char* topic_simonbox_lights_red = "simonbox/lights/red";
const char* topic_simonbox_lights_green = "simonbox/lights/green";
const char* topic_simonbox_lights_blue = "simonbox/lights/blue";

const char* PAYLOAD_PRESSED = "pressed";
const char* PAYLOAD_RELEASED = "released";

const char* PAYLOAD_ON = "on";
const char* PAYLOAD_OFF = "off";

int sendDelay = 200;

// If your MQTT Broker requires a username and password, uncomment and fill in the section below
// const char* mqttUser = "MqttUser";
// const char* mqttPassword = "MqttPassword";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;

void setup_wifi() {
   delay(100);
  // Connecting to a WiFi network
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) 
    {
      delay(500);
      Serial.print(".");
    }
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

// Recieve messages from subscribed topics here and do something with them.
void callback(char* topic, byte* payload, unsigned int length) 
{
  Serial.println("Message arrived!");
  
  if (strcmp(topic,topic_simonbox_lights_yellow)==0){
      if (!strncmp((char *)payload, PAYLOAD_ON,length)){
        digitalWrite(LIGHT_YELLOW_PIN, HIGH);
      }   
      if (!strncmp((char *)payload, PAYLOAD_OFF,length)){
        digitalWrite(LIGHT_YELLOW_PIN, LOW); 
      }
  }
  
  if (strcmp(topic,topic_simonbox_lights_red)==0){
    if (!strncmp((char *)payload, PAYLOAD_ON,length)){
      digitalWrite(LIGHT_RED_PIN, HIGH);
    }   
    if (!strncmp((char *)payload, PAYLOAD_OFF,length)){
      digitalWrite(LIGHT_RED_PIN, LOW); 
    }
  }

  if (strcmp(topic,topic_simonbox_lights_green)==0){
    if (!strncmp((char *)payload, PAYLOAD_ON,length)){
      digitalWrite(LIGHT_GREEN_PIN, HIGH);
    }   
    if (!strncmp((char *)payload, PAYLOAD_OFF,length)){
      digitalWrite(LIGHT_GREEN_PIN, LOW); 
    }
  }
  
  if (strcmp(topic,topic_simonbox_lights_blue)==0){
    if (!strncmp((char *)payload, PAYLOAD_ON,length)){
      digitalWrite(LIGHT_BLUE_PIN, HIGH);
    }   
    if (!strncmp((char *)payload, PAYLOAD_OFF,length)){
      digitalWrite(LIGHT_BLUE_PIN, LOW); 
    }
  }
  
} // End callback

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    //if you MQTT broker has clientID,username and password
    //please change following line to    if (client.connect(clientId.c_str,MqttUser,MqttPassword))
    if (client.connect(clientId.c_str())){
      Serial.println("connected");

    // Blink light twice if connected
    for (int j=1; j<=5; j++) {
      digitalWrite(LIGHT_GREEN_PIN,HIGH);
      delay(200);
      digitalWrite(LIGHT_GREEN_PIN,LOW);
      delay(200);
    }
              
     //once connected to MQTT broker, subscribe command if any
     client.subscribe(topic_simonbox_buttons_yellow);
     client.subscribe(topic_simonbox_buttons_red);
     client.subscribe(topic_simonbox_buttons_green);
     client.subscribe(topic_simonbox_buttons_blue);
     
     client.subscribe(topic_simonbox_lights_yellow);
     client.subscribe(topic_simonbox_lights_red);
     client.subscribe(topic_simonbox_lights_green);
     client.subscribe(topic_simonbox_lights_blue);  
    } 
    
    else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      
      // Blink light thrice if not connected
      for (int j=1; j<=5; j++) {
        digitalWrite(LIGHT_RED_PIN,HIGH);
        delay(200);
        digitalWrite(LIGHT_RED_PIN,LOW);
        delay(200);
      }
      
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
} // End reconnect()

void setup() {
  Serial.begin(115200);
 
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  
  buttonYellow.begin();
  buttonRed.begin();
  buttonGreen.begin();
  buttonBlue.begin();

  pinMode(LIGHT_YELLOW_PIN, OUTPUT);
  pinMode(LIGHT_RED_PIN,OUTPUT);
  pinMode(LIGHT_GREEN_PIN,OUTPUT);
  pinMode(LIGHT_BLUE_PIN,OUTPUT);
  
} // End setup()

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // check if the pushbutton is pressed.
  if (buttonYellow.pressed()) {
    digitalWrite(LIGHT_YELLOW_PIN, HIGH);
    Serial.println("Yellow button pressed");
    
    //publish data to MQTT broker
    client.publish(topic_simonbox_buttons_yellow, PAYLOAD_PRESSED);
    delay(sendDelay);   
  }
   
  if(buttonYellow.released()) {
    digitalWrite(LIGHT_YELLOW_PIN, LOW);
    Serial.println("Yellow button released");
    client.publish(topic_simonbox_buttons_yellow, PAYLOAD_RELEASED);
    delay(sendDelay);   
  }

  if (buttonRed.pressed()) {
    digitalWrite(LIGHT_RED_PIN, HIGH);
    Serial.println("Red button pressed");
    client.publish(topic_simonbox_buttons_red, PAYLOAD_PRESSED);
    delay(sendDelay);   
  } 
  
  if(buttonRed.released()) {
    digitalWrite(LIGHT_RED_PIN, LOW);
    Serial.println("Red button released");
    client.publish(topic_simonbox_buttons_red, PAYLOAD_RELEASED);
    delay(sendDelay);       
  }

  if (buttonGreen.pressed()) {
    digitalWrite(LIGHT_GREEN_PIN, HIGH);
    Serial.println("Green button pressed");
    client.publish(topic_simonbox_buttons_green, PAYLOAD_PRESSED);
    delay(sendDelay);   
  } 
  
  if(buttonGreen.released()) {
    digitalWrite(LIGHT_GREEN_PIN, LOW);
    Serial.println("Green button released");
    client.publish(topic_simonbox_buttons_green, PAYLOAD_RELEASED);
    delay(sendDelay);       
  }

  if (buttonBlue.pressed()) {
    digitalWrite(LIGHT_BLUE_PIN, HIGH);
    Serial.println("Blue button pressed");
    client.publish(topic_simonbox_buttons_blue, PAYLOAD_PRESSED);
    delay(sendDelay);   
  } 
  
  if(buttonBlue.released()) {
    digitalWrite(LIGHT_BLUE_PIN, LOW);
    Serial.println("Blue button released");
    client.publish(topic_simonbox_buttons_blue, PAYLOAD_RELEASED);
    delay(sendDelay);       
  } 
} // End of loop()
