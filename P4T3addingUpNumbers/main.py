#CTI 110
#P4T3 - Running Total
#Lourdes Linares
#10.21.21

#For this program we're adding up the numbers
currentNumber = 0 # we'll store each number here before adding
total = 0
numEntries = 0 # Ask user how many times to loop
count = 0 # Used to keep track of our loop

# Ask user how many
numEntries = int(input("How many numbers to add? "))
while numEntries <= 0:
  print("Please enter a value greater than zero.")
  numEntries = int(input("How many numbers to add? "))

# then loop and enter each number
while count < numEntries:
  print("*count=", count, "numEntries =", numEntries) #debugging
  #enter each number
  #print("\t the count is", count) #test
  currentNumber = int(input("Enter number: "))
  total = total + currentNumber
  count = count + 1

#print total
print("The total is:", total)

#Can we find the average?
if numEntries > 0:
  average = total / numEntries
  print("The average is:", average)






