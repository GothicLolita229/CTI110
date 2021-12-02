#CTI 110
#Lourdes Linares
#11.19.2021
#RNG generator 
#

'''
For P5LAB3 (due 11/22) we'll be using our random number functions to start building a simple game or two.
For now we'll start with "rock paper scissors" (in a future assignment, if time permits we'll try out "craps".)
For Lab 3, just turn in your "Coin Flip" version.
'''
import random


def RPS():
  choice = random.randint(1, 3)
  hand = None
  if choice == 1:
    hand = "rock"
  elif choice == 2:
    hand = "paper"
  elif choice == 3:
    hand = "scissors"
  return hand 

def userRPS():
    #print("Your choices are rock, paper, or scissors. May the best mathematician win (That's me).")
    yourHand = str(input("Enter your choice: "))

    return yourHand


def RPSstart():
  again = 'y'
  while again.lower() == 'y':
    
    print("Playing rock, paper, scissors...")
    print("Your choices are rock, paper, or scissors. May the best mathematician win (That's me).")
    for num in range(3):
    # "Me" is computer, "you" is user
      yourHand = userRPS()
      myHand = RPS()
    # yourHand = RPS()
      output = "Me: "+ myHand + " VS You: "+ yourHand
      print()
      print(output.upper())
      print()

    again = str(input("Would you like to play again?(y/n) "))

def coinFlip():
  flip = random.randint(0, 1)
  turn = None
  if flip == 0:
    turn = "tails"
  elif flip == 1:
    turn = "head"
    
  return turn

def CFstart():
  again = 'y'
  while again.lower() == 'y':
    print("Flipping a coin...")
    for i in range(5):
      flip = coinFlip()
      print("Result was: ", flip)

    again = str(input("Would you like to play again?(y/n) "))

def main():
  repeat = True
  selection = 0

  while repeat == True:
    print("Game choices: ")
    print("_" * 32)
    print("Option 1: Rock, Paper, Scissors")
    print("Option 2: Coin flip")
    print("Option 3: Exit games")
    
    try:
      selection = int(input("Choose option: "))
    except:
      print("That is not a valid choice. Please try again.")
    
    else:
     if selection == 1:
       print("_" * 32)
       print()
       print("This game has a little more variety :-) ")
       RPSstart()

     elif selection == 2:
       print("_" * 32)
       print()
       print("Total chance here...")
       CFstart()

     elif selection == 3:
       print("Exiting...")
       repeat = False

     else:
      print(selection, "is not a number option. Use 1-3")

main()