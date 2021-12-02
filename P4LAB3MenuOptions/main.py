#CTI 110
#P4LAB3
#Linares
#10.28.2021


# import could be here
# A simple menu, which can be expanded
# For this program, we'll be making a menu with 4 or more options. One of the options should be "Quit".
# The program should print the menu and then ask the user to make a choice. If the user makes a choice other than those listed, they are asked to make the choice again.
# Once the user picks a menu option, print a message specific to that choice, and then return to the main menu.
# This basic structure combines if statements with loops, and will be useful for us as we make more complex programs.


def fishOption(sponsor):

  print("This meal brought to you by:", sponsor)
  cooked = input("Do you you want it cooked (yes/no)? ")
  if cooked != "yes":
    print("You're having sushi. Hope raw fish doesn't gross you out.")
  else:
    print("You can have baked salmon. Still good. Just not as fancy.")

def poultry(sponsor):

  print("Wings from ", sponsor)

  bottomlessWings = "no"
  while bottomlessWings != "yes" and bottomlessWings != "y":
    print("You're eating spicy chicken wings.")
    bottomlessWings = input("Is that spicy enough (yes/no)? ")

  print("Okay, you're right. It's spicy enough. Sorry, there are no options for milk. *maniacal robot laughter*")

def redMeat(sponsor):
  
  print("Your butcher is ", sponsor)
  #offer options of steak tartare, ribeye, or steak fajitas
  print("a) Steak Tartare")
  print("b) Ribeye")
  print("c) Steak fajitas")
  # ex of returning a Value 
  option = None # no value

  choice = input("Choose: ")
  if choice == "a"  or choice == "A":
    option = "a"
    print("Steak Tartare")
    print("You must be eating this just to be fancy. Who likes raw meat AND raw egg?! EUUCKKK")
  if choice.lower() == "b":
    option = "b"
    print("Ribeye")
    print("Did you want to go to Outback instead?")
  if choice.lower() == "c":
    option = "c"
    print("Steak Fajitas")
    print("Stop pretending to be Mexican. Side note: I'm Latinx but I did not know what these were until some white friends made them with crepes instead of tortillas")
  return option

  '''try:
    selection = str(input("Choose option: "))
  except:
      print("This is not a valid choice. Please try again.")'''


def surprise():
  print("WTHEver you want.")

def main():
  print("testing")

  #declare variables
  repeat = True
  selection = 0 # so we don't pick the previous menu option

  while repeat == True:
    #print the menu, ask user to make choice 
    print("Menu: ")
    print("_" * 10)
    print("1. Option 1: Fish")
    print("2. Option 2: Poultry")
    print("3. Option 3: Red Meat")
    print("4. Surprise!")
    print("5. Nothing")
    # this fixes if user inputs invalid entry
    try:
      selection = int(input("Choose option: "))
    except:
      print("That is not a valid choice. Please try again.")
    # either pick a branch based on the selection
    # or print error and repeat (in not from listed options)
    if selection == 1:
      print("You chose Fish") # for testing
      fishOption("Gordon Ramsey") #sponsor = Gordon Ramsey
    elif selection ==2:
      print("You chose Poultry") # for testing
      poultry("Hooters!")
    elif selection == 3:
      print("You chose Red Man Meat") # for testing
      print("Who are you? Hannibal?")
      #redMeat("Dr. Lecter")
      option = redMeat("Dr. Lecter")
      print("Back in Menu: You picked", option)
    elif selection == 4:
      print("You chose to be surprised!") #add menu that pulls random surprise option
      surprise()
    elif selection == 5:
      print("Exiting....")
      repeat = False # next time through we won't loop
    else: #anything else
      print(selection, "is not a number option. Use 1-3")

  #end of while loop 
  print("Goodbye.")

#program starts here
main()

#the complex version (this is optional for now)
#TLDR: prevents mulitple main() from running at open
"""
if __name__ == "__main__":
  main()
"""

