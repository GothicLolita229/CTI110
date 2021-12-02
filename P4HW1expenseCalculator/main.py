#CTI 110
#P4HW2 - Expense Calculator
#Lourdes Linares
#10.28.2021


#this program will calculate the total monthly expenses and subtract them from total funds

'''Prompt user to enter amount in account in which money will be withdrawn from.
Prompt user to enter amount of first expense
Subtract expense from account
Ask user if he/she would like to enter another expense. Program DOES NOT move on to next step unless user chooses NOT to enter another expense.
4.IF user chooses NOT to enter another expense, display the following info
Amount in account BEFORE expenses subtracted
Number of expenses entered
Amount in account AFTER expenses subtracted'''


#print("Enter starting amount in account $")
#input and variables

maxBalance = float(input("Enter starting amount in account $"))
keepGoing = "y" # yes
expenseCount = 0
currentBalance = maxBalance


while keepGoing == "y":
  expenseCount += 1
  print("Enter expense", expenseCount, ":", end=" ")
  expense = float(input())
  print("Do you want to enter another expense? (y/n)")
  keepGoing = input()
  currentBalance -= expense



print("Amount in account before expenses subtracted: ", format(maxBalance, ".2f"))
print("Number of expenses entered: ", expenseCount)
print("Amount in account after expense subtracted: ", format(currentBalance, ".2f"))



#calculations

#output