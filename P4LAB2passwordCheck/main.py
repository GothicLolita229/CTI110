#CTI 110
# P4LAB2 _ Password Strength Checker
# Lourdes Linares
# 10.26.2021

# Part 1 - Password lenth

# Declare variables
MIN_LENGTH = 12
isGoodPassword = False


# until the user gives a good enough password:
while False == isGoodPassword:
  
  # ask user for password
  password = input("Please enter a new password: ")
  # check length
  # if it's at least MIN_LENGTH, it's a good password
  if len(password) >= MIN_LENGTH:
    #isGoodPassword = True

    #require upper and lowercase
    #might add more than length check later
    if password == password.lower() or password == password.upper():
      print("Password should contain a mix of upper and lower case letters.")
    else:
      isGoodPassword = True

  #otherwise try again
  else:
    print("Password must be at least", MIN_LENGTH, "characters.")

print("Your new password is: ", password)
print("I hope nobody is looking over your shoulder...")

# Part 2 - swapping characters
# TODO (see 11.16)
"""
i becomes 1
a becomes @
m becomes M 
B becomes 8
s becomes $
and add ! to the end

"""
print("Now we'll replace some characters to make it harder to guess.")
newPassword = "" #we will add each character one at a time
chars = list(password)

for char in chars:
  #print(char) #test
  #replace chars if they are in list
  if char == "i":
    char = "1"
  if char == "a":
    char = "@"
  if char == "m":
    char = "M"
  if char == "B":
    char = "8"
  if char == "s":
    char = "$"
  #print(char)  
  newPassword += char #add new char to end

newPassword += "!"

print("Your fancy new password is: ", newPassword)