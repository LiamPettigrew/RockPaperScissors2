import random
import sys


def error1():
    statement_generator("Sorry, that is an invalid answer", "!")
    sys.exit(print("The program will now shut down. Please reboot."))


def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    print()
    return ""


statement_generator("Welcome to the Rock Paper Scissors minigame", "*")
print()

get_name = input("Please input your name. ")
print("Hello there " + get_name + "! Do you wish to view the instructions.")

instructions = input(
    "Type 'no' to proceed, and 'yes' if you wish to view the instructions. ")
print()

if (instructions != "yes") and (instructions != "Yes") and (
        instructions != "no") and (instructions != "No"):
    print(error1())

elif instructions == "yes" or instructions == "Yes":
    print()
    statement_generator("INSTRUCTIONS", "-")
    print()
    print("")
    print()
    valid = False
    while not valid:
      try:
        print("How many rounds do you wish to play?\n")
        print(
          "You can only play up to 10 rounds. For infinite mode, type Infinite"
        )
        mode = input
        if 0 < int(mode()) <= 10:
          print("You have chosen to play " + str(mode()) + " rounds.")
          print("Enter either Rock, Paper, or Scissors:\n")
          break
        elif str(mode()) == "Infinite" or str(mode()) == "infinite":
          print("Success")
        else:
          if 0 > int(mode()) >= 10 or str(mode()) != "Infinite" or str(mode()) != "infinite":
            print(error1())
            valid = True
      except ValueError:
        if str(mode()) == "Infinite" or str(mode()) == "infinite":
          print("You have chosen to play Infinite rounds. This means that the game will not end until you type: End")
          print("Enter either Rock, Paper, or Scissors:\n")
          valid = True
        else:
          print(error1())
          valid = True
          break

elif instructions == "no" or instructions == "No":
    valid = False
    while not valid:
        try:
            print("How many rounds do you wish to play?\n")
            print(
                "You can only play up to 10 rounds. For infinite mode, type Infinite"
            )
            mode = input
            if 0 < int(mode()) <= 10:
                print("You have chosen to play " + str(mode()) + " rounds.")
                print("Enter either Rock, Paper, or Scissors:\n")
                break
            elif str(mode()) == "Infinite" or str(mode()) == "infinite":
                print("Success")
            else:
                if 0 > int(mode()) >= 10 or str(mode()) != "Infinite" or str(mode()) != "infinite":
                    print(error1())
                    valid = True
        except ValueError:
            if str(mode()) == "Infinite" or str(mode()) == "infinite":
              print("You have chosen to play Infinite rounds. This means that the game will not end until you type: End")
              print("Enter either Rock, Paper, or Scissors:\n")
              valid = True
            else:
              print(error1())
              valid = True
              break

### Recycled code below

def choice_checker(question, error):
  valid = False
  while not valid:
    response = input(question).lower()
    if response == "r" or response == "rock":
      return response
    elif response == "p" or response == "paper":
      return response
      