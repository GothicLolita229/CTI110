#CTI 110
#P2T2 - Age Checker
#Lourdes Linares
#9.30.2021

# Ask the user for their age

CURRENT_YEAR = 2021
birthYear = int(input("What is the customer's birth year? "))

age = CURRENT_YEAR - birthYear
print(age)

#age = int(input("How old is the customer? "))
#Are they over 21, or not?
if age > 21:
  print("Purchase is allowed.")
elif age < 21:
  print("Purchase is prohibited.")
else:
  print("Customer is exactly 21 - check birth date against today's date.")

