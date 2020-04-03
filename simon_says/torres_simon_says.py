import random
import time


def introduction():
    print("Simon Says is a game where the user will type in their command line commands that the Simon app instructs, starting with 'Simon says' followed by the command")
    time.sleep(1)
    print("If the command does not start with Simon says hit the Space Bar and then hit ENTER")
    time.sleep(1)
    # simonSays(game_prompts)

# Conditions to keep game running:
# The user types the correct thing

# Condition to end game:
# User types the wrong thing
# User doesn't type  SPACE BAR if the command doesn't start with Simon says


game_prompts = [
    "Simon says enter 1",
    "enter 1",
    "Simon says enter 2",
    "enter 2",
    "Simon says enter 3",
    "enter 3"
]


def simonSays(game_prompts):
    random.shuffle(game_prompts)
    pick = game_prompts[0]

    while pick:
        print(pick)
        if pick.startswith("Simon says ") and input() == int(pick[-1]):
            print("Success!")
            game_prompts.pop(0)

        elif not pick.startswith("Simon says ") and input() == " ":
            game_prompts.pop(0)

        elif not pick.startswith("Simon says ") and input() != " ":
            print("FAILURE! You have failed the game")
            break

        elif game_prompts == []:
            print("You win the game!")
            break

    # while pick.startswith("Simon says ") and input() == int(pick[-1]):
    #     print("Success!")
    #     game_prompts.pop(0)
    #     if game_prompts == []:
    #         print("You win the game!")
    #         break

    # while not pick.startswith("Simon says ") and input() == " ":
    #     game_prompts.pop(0)
    #     if game_prompts == []:
    #         print("You win the game!")
    #         break

    # while not pick.startswith("Simon says ") and input() != " ":
    #     print("FAILURE! You have failed the game")
    #     break


introduction()
simonSays(game_prompts)
