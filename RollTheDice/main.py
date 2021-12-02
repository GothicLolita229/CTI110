#P5T3
#Lourdes Linares
#CTI110
#11.16.2021
#Random Numbers/Dice Rolls

# Write random number generators

import random

def rollD6():
  '''
  input: None
  output: int from 1 to 6
  '''
  roll = random.randint(1, 6)
  return roll

def roll2D6():
  roll = rollD6() + rollD6()
  return roll

def DungeonsNDragons():
  roll = random.randint(1, 20)
  return roll

'''
def coinFlip():
  flip = random.randint(0, 1)
  turn = None
  if flip == 0:
    return "tails"
  elif flip == 1:
    return "heads"
  '''
def coinFlip():
  flip = random.randint(0, 1)
  turn = None
  if flip == 0:
    turn = "tails"
  elif flip == 1:
    turn = "head"
    
  return turn

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

'''def removeDupes(items):
  mySet = set(items)
  noDupeList = list(mySet)

  return noDupeList'''


def main():
  # random.seed(42)
  print("Rolling dice...")
  for num in range(10):
    roll = rollD6()
    print(roll, end=" ")
  print()
  print("Rolling 2 dice....")
  for num in range(10):
    roll = roll2D6()
    print(roll, end=" ")
  print()
  secondRoll = DungeonsNDragons()
  print("Eldritch blast: ", secondRoll)
  print()
  print("Flipping a coin...")
  for i in range(5):
    flip = coinFlip()
    print("Result was: ", flip)
  print()
  print("Playing rock, paper, scissors...")
  for num in range(5):
    myHand = RPS()
    yourHand = RPS()
    print("Me:", myHand, "VS You:", yourHand)

  


#start program
main()