import random
from time import sleep
import os
import msvcrt
import serial

from transitions import Machine
import random



class game(object):

    states = ['introduction', 'gamePlay', 'success', 'gameOver']

    def __init__(self, name):

        self.name = name

        self.gameLevel = 0

        # Initialize the state machine
        self.machine = Machine(model=self, states=game.states, initial='introduction')

        self.machine.add_transition(trigger='start', source='introduction', dest='gamePlay')

        self.machine.add_transition('win', 'gamePlay', 'success', after='update_level')

        self.machine.add_transition('nextLevel', 'success', 'gamePlay')                

        self.machine.add_transition('lose', 'gamePlay', 'gameOver')

        self.machine.add_transition('reset', 'gameOver', 'gamePlay')

        self.machine.add_transition('complete_mission', 'saving the world', 'sweaty',
                        after='update_level')



        self.machine.add_transition('clean_up', 'sweaty', 'asleep', conditions=['is_exhausted'])
        self.machine.add_transition('clean_up', 'sweaty', 'hanging out')

        # Our NarcolepticSuperhero can fall asleep at pretty much any time.
        self.machine.add_transition('nap', '*', 'asleep')
    
    def update_level(self):
        """ Dear Diary, today I saved Mr. Whiskers. Again. """
        self.gameLevel += 1
        print("Great Job! Keep going!")

    @property
    def is_exhausted(self):
        """ Basically a coin toss. """
        return random.random() < 0.5

    def change_into_super_secret_costume(self):
        print("Beauty, eh?")


memory=game("Memory")

while memory.state == 'introduction':
    print('We are in introduction')
    playerInput = input('play? Hit Enter') 
    memory.start()

while memory.state == 'gamePlay':
    print('We are in Game Play')
    playerInput = input('Enter Value: ')     
    if playerInput == '1':
        memory.win()
        memory.nextLevel()
    
    if playerInput == '2':
        memory.lose()

while memory.state == 'gameOver':
    print('Game Over')
    print("Player Score:",memory.gameLevel)
    inputPlayer = input('Want to restart')
    memory.rest()