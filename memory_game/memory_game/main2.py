import random
from time import sleep
import os
import msvcrt
import serial
import mqtt_messages


displayTime = .5
lights = ['yellow','red','green','blue']

print(buttonPressed)

User = input("blabla enter")

if User == '1':
    print(buttonPressed)

tempo = .5  
             
def introduction():
    global gameContinue
    inputPlayer = input('Press ENTER to start.')
    
    sleep(tempo)
    os.system('cls') 
    
    print(' \nBegin!')
    sleep(displayTime)
    os.system('cls')   
    gameContinue = True

def player_reward():
    global gameContinue
    
    if gameContinue:
        print('\nSuccess. \nNext round.')
        sleep(displayTime)
        os.system('cls')  

def game_play():
    global gameContinue
    global playerScore
    
    pattern = []
    patternPlayer = []
    playerScore = 0 
    currentLevel = 1

    while gameContinue:            
        # Add new pattern number
        currentlight = random.choice(lights)
        pattern.append(currentlight)

        # Display new pattern numbers
        for count in range(0,currentLevel):
            print('\n',pattern[count])
            LED_blink(pattern[count])
            simonbox_light_display(pattern[count])
            sleep(tempo)
            os.system('cls')
            sleep(tempo)   

        print('\nGO!')
        sleep(tempo) 
        os.system('cls')  

        # Obtain players input
        patternPlayer = []
        for count in range(0,currentLevel):
            print('\n')
            guess = None
            while guess == None:
                inputPlayer = 'taco'
            #inputPlayer = int(msvcrt.getch())
            patternPlayer.append(inputPlayer)
            print(inputPlayer)
            LED_blink(inputPlayer)
            sleep(0.1) 
            os.system('cls')
            
            if(patternPlayer[count] != pattern[count]):
                gameContinue = False          
                break   
        
        player_reward()
        
        currentLevel += 1  
        playerScore = currentLevel - 2

def game_over():
    global gameContinue
    global playerScore

    if not gameContinue:
        print('Better luck next time...')
        LED_raw(1,255) 
        LED_raw(2,255)
        LED_raw(5,255)
        sleep(2)
        LED_raw(2,0)
        LED_raw(5,0) 
        print('Player Score:', playerScore) 
        gameContinue = True

# Main game loop
while True: 
 
    introduction()
     
    game_play()   

    game_over()
    



