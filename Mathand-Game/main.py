# program that gives simple math quizzes
# 11.29.2021
# CTI-110 P5HW2 - Math Quiz
# Lourdes Linares
#
# P5HW2_MathQuiz _LinaresLourdes.py

import random

def nums():
  num = random.randint(1, 99)

  return num

def addingNumbers():
  print("Did you learn addition in school? We'll see...")
  addend1 = nums()
  addend2 = nums()
  print(" ", addend1)
  print("+", addend2)
  sum = addend1 + addend2
  #print("Enter answer:")
  guess = int(input("Enter answer: "))
  count = 1

  while guess != sum:
    count += 1
    if guess > sum:
      print("Sorry, your guess is too high.")
      
    elif guess < sum:
      print("Sorry, your guess is too low.")
    guess = int(input("Try again: "))
       
  else:
    print("Congratulations! Your answer is correct!")
    print("Number of guesses: ", count)


def subNumbers():
  print("Subtracting... fun....")
  minuend = nums()
  subtrahend = nums()
  print(" ", minuend)
  print("-", subtrahend)
  difference = minuend - subtrahend
  #print("Enter answer:")
  guess = int(input("Enter answer: "))
  count = 1

  while guess != difference:
    count += 1
    if guess > difference:
      print("Sorry, your guess is too high.")
      
    elif guess < difference:
      print("Sorry, your guess is too low.")
    guess = int(input("Try again: "))
       
  else:
    print("Congratulations! Your answer is correct!")
    print("Number of guesses: ", count)


def main():
  repeat = True
  selection = 0

  while repeat == True:
    print("MAIN MENU")
    print("-" * 30)
    print("1 - Adding Random Numbers Game")
    print("2 - Subtracting Random Numbers Game")
    print("3 - Exit")
    print()
    try:
      selection = int(input("Choose option: "))
    except:
      print("That is not a valid option. Choose 1, 2, or 3")
    if selection == 1:
      print("Adding game it is!")
      addingNumbers()
      print()

    elif selection == 2:
      print("You chose subtraction. My least favorite math problem...")
      subNumbers()
      print()

    elif selection == 3:
      repeat = False
      print("Thank you for playing...")
      print("Byyyeee!!")

    else: #anything else
      print(selection, "is not an option. Use 1-3")


main()