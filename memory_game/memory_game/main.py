import random
from time import sleep
import os
import msvcrt
import serial

displayTime = .5
#arduinoData = serial.Serial('COM10', 9600)
# sleep(3)


def LED_raw(channel, value):
    try:
        message = '{"channels":[{"channel":%s,"value":%s}]}' % (channel, value)
        arduinoData.write(message.encode())
    except:
        pass

# def LED(brightness, red, blue, green):
#     message = '{"channels":[{"channel":1,"value":%s},{"channel":2,"value":%s},{"channel":3,"value":%s},{"channel":4,"value":%s}]}' % (brightness, red, blue, green)
#     arduinoData.write(message.encode())


def LED_blink(color):
    try:
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
    except:
        pass


LED_blink(1)
sleep(0.2)
LED_blink(2)
sleep(0.2)
LED_blink(3)

tempo = .5


class GameOne():
    def __init__(self):
        self.gameContinue = True
        self.introduction()
        self.playerScore = 0

    def introduction(self):
        inputPlayer = input('Press ENTER to start.')

        sleep(tempo)
        os.system('cls')

        print(' \nBegin!')
        sleep(displayTime)
        os.system('cls')

    def playerReward(self):

        if self.gameContinue:
            LED_raw(1, 255)
            LED_raw(3, 255)
            LED_raw(5, 200)
            sleep(1)
            LED_raw(3, 0)
            LED_raw(5, 0)
            print('\nSuccess. \nNext round.')
            sleep(displayTime)
            os.system('cls')

    def game_play(self):

        pattern = []
        patternPlayer = []
        currentLevel = 1

        while self.gameContinue:
            # Add new pattern number
            currentNumber = random.randint(1, 3)
            pattern.append(currentNumber)

            # Display new pattern numbers
            for count in range(0, currentLevel):
                print('\n', pattern[count])
                LED_blink(pattern[count])
                sleep(tempo)
                os.system('cls')
                sleep(tempo)

            print('\nGO!')
            sleep(tempo)
            os.system('cls')

            # Obtain players input
            patternPlayer = []
            for count in range(0, currentLevel):
                print('\n')
                inputPlayer = int(msvcrt.getch())
                patternPlayer.append(inputPlayer)
                print(inputPlayer)
                LED_blink(inputPlayer)
                sleep(0.1)
                os.system('cls')

                if(patternPlayer[count] != pattern[count]):
                    gameContinue = False
                    break

            playerReward()

            currentLevel += 1
            self.playerScore = currentLevel - 2

    def game_over(self):
        if not self.gameContinue:
            print('Better luck next time...')
            LED_raw(1, 255)
            LED_raw(2, 255)
            LED_raw(5, 255)
            sleep(2)
            LED_raw(2, 0)
            LED_raw(5, 0)
            print('Player Score:', self.playerScore)
            self.gameContinue = True


# Main game loop
while True:

    introduction()

    game_play()

    game_over()
