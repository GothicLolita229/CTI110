#CTI 110
#P4T4 - Running Total with Sentinel
#Lourdes Linares
#10.26.2021

#We will add up float - hours worked
#user enter values until they enter -1 or lower
#-1 is sentinel value that means "done"

#set up variables
total = 0
currentHours = 0
keepGoing = True


#Explain
print("Enter each day's hours worked on a different line.")
print("Enter -1 (or any negative number) to finish.")

#Loop until done 

while keepGoing == True:

  #Ask user for number of hours
  currentHours = float(input("Enter the number of hours worked: "))
  #if it's -1 or less, done 
  if currentHours < 0:
    keepGoing = False
  #otherwise, add to Total
  else:
    total += currentHours # total = total + currentHours

print("Total hours entered: ", total)


