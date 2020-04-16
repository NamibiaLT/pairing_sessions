const int BUTTON_YELLOW_PIN = D5;
const int BUTTON_RED_PIN = D6;
const int BUTTON_GREEN_PIN = D7;
const int BUTTON_BLUE_PIN = D4; //D8 has no pullup resistor


const int LIGHT_YELLOW_PIN = D1;
const int LIGHT_RED_PIN = D2;
const int LIGHT_GREEN_PIN = D3;
const int LIGHT_BLUE_PIN = D8;

boolean buttonYellowState = 0;
boolean buttonRedState = 0;
boolean buttonGreenState = 0;
boolean buttonBlueState = 0;

boolean buttonYellowPreviousState = LOW;


void setup() {
  Serial.begin(115200);
  Serial.println("Begin Simon Box button test...");
  
  pinMode(BUTTON_YELLOW_PIN,INPUT_PULLUP);
  pinMode(BUTTON_RED_PIN,INPUT_PULLUP);
  pinMode(BUTTON_GREEN_PIN,INPUT_PULLUP);
  pinMode(BUTTON_BLUE_PIN,INPUT_PULLUP);

  pinMode(LIGHT_YELLOW_PIN, OUTPUT);
  pinMode(LIGHT_RED_PIN,OUTPUT);
  pinMode(LIGHT_GREEN_PIN,OUTPUT);
  pinMode(LIGHT_BLUE_PIN,OUTPUT);



////Light Test
//const int lightArray[] = {LIGHT_YELLOW_PIN, LIGHT_RED_PIN, LIGHT_GREEN_PIN, LIGHT_BLUE_PIN};
//int timer = 100;
//int count = 4;
//for(int thisLight = 0; thisLight < count; thisLight++) {
//  digitalWrite(lightArray, HIGH);
//  delay(timer);
//  digitalWrite(lightArray, LOW);
//  delay(timer);
//}

}

void loop() {
  
  // read the state of the pushbutton value:
  buttonYellowState = digitalRead(BUTTON_YELLOW_PIN);
  buttonRedState = digitalRead(BUTTON_RED_PIN);
  buttonGreenState = digitalRead(BUTTON_GREEN_PIN);
  buttonBlueState = digitalRead(BUTTON_BLUE_PIN);


  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if ((buttonYellowState = LOW) && (buttonYellowPreviousState = HIGH)) {
    digitalWrite(LIGHT_YELLOW_PIN, HIGH);
    Serial.println("Yellow button pressed");
  } 
  else if ((buttonYellowState = HIGH) && (buttonYellowPreviousState = LOW)) {
    digitalWrite(LIGHT_YELLOW_PIN, LOW);
  }

  if (buttonRedState == LOW) {
    digitalWrite(LIGHT_RED_PIN, HIGH);
    Serial.println("Red button pressed");
  } 
  else {
    digitalWrite(LIGHT_RED_PIN, LOW);
  }

  if (buttonGreenState == LOW) {
    digitalWrite(LIGHT_GREEN_PIN, HIGH);
    Serial.println("Green button pressed");    
  } 
  else {
    digitalWrite(LIGHT_GREEN_PIN, LOW);
  }
 
  if (buttonBlueState == LOW) {
    digitalWrite(LIGHT_BLUE_PIN, HIGH);
    Serial.println("Blue button pressed");    
  } 
  else {
    digitalWrite(LIGHT_BLUE_PIN, LOW);
  }


buttonYellowPreviousState = buttonYellowState;

}
