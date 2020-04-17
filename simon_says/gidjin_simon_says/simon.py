#!/bin/env python

from random import randint

game_length = 10

total_prompts = 0

print('Simon says game')
print('  enter correct answer when Simon says or enter a space')
print('  type q or quit to exit')

while True:
    number = randint(0, 99)
    simon_says = True
    if (randint(0, 4) % 2 == 0):
        simon_says = False

    choice = ''
    if (simon_says):
        choice = input(f'Simon says enter {number}: ')
    else:
        choice = input(f'Enter {number}: ')

    if (choice == 'q' or choice == 'quit'):
        print('Goodbye')
        break
    elif (not simon_says and
            choice != ' ' or
            simon_says and
            choice != str(number)):
        print('FAILURE! You have failed the game')
        break

    total_prompts += 1
    if total_prompts == game_length:
        print("Congratulations! You've won the game")
        break
