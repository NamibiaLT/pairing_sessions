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

boolean buttonYellowPreviousState = LOW;


void setup() {
  Serial.begin(115200);
  Serial.println("Begin Simon Box button test...");

  buttonYellow.begin();
  buttonRed.begin();
  buttonGreen.begin();
  buttonBlue.begin();

  pinMode(LIGHT_YELLOW_PIN, OUTPUT);
  pinMode(LIGHT_RED_PIN,OUTPUT);
  pinMode(LIGHT_GREEN_PIN,OUTPUT);
  pinMode(LIGHT_BLUE_PIN,OUTPUT);
}

void loop() {
  
  // check if the pushbutton is pressed.
  if (buttonYellow.pressed()) {
    digitalWrite(LIGHT_YELLOW_PIN, HIGH);
    Serial.println("Yellow button pressed");
  } 
  if(buttonYellow.released()) {
    digitalWrite(LIGHT_YELLOW_PIN, LOW);
    Serial.println("Yellow button released");
  }

  if (buttonRed.pressed()) {
    digitalWrite(LIGHT_RED_PIN, HIGH);
    Serial.println("Red button pressed");
  } 
  if(buttonRed.released()) {
    digitalWrite(LIGHT_RED_PIN, LOW);
    Serial.println("Red button released");
  }

    if (buttonGreen.pressed()) {
    digitalWrite(LIGHT_GREEN_PIN, HIGH);
    Serial.println("Green button pressed");
  } 
  if(buttonGreen.released()) {
    digitalWrite(LIGHT_GREEN_PIN, LOW);
    Serial.println("Green button released");
  }

    if (buttonBlue.pressed()) {
    digitalWrite(LIGHT_BLUE_PIN, HIGH);
    Serial.println("Blue button pressed");
  } 
  if(buttonBlue.released()) {
    digitalWrite(LIGHT_BLUE_PIN, LOW);
    Serial.println("Blue button released");
  }
}
