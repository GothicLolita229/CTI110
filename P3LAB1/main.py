#CTI 110
#P3LAB1 - Interstates
#Lourdes Linares
#10.7.2021

#Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.

#Ask user for highway number
highway = int(input("Enter highway number: "))

#Given a highway number, indicate whether it is a primary or auxiliary highway.
#Numbers from 1-99 are primary, 100-999 are aux

#one way: nested ifs
"""if highway >= 1:
  if highway <= 99:
    print("I-", highway, " is a primary highway.", sep="")
  else: #highway is 100 or more
    if highway <= 999:
      print("I-", highway, " is an auxiliary highway.", sep="")"""
isPrimary = True # set false if need be below


# another way : logical operators
if highway >= 1 and highway <= 99:
  print("I-", highway, " is a primary highway.", sep="")
  
elif highway >= 100 and highway <= 999:
  print("I-", highway, " is an auxiliary highway.", sep="")
  isPrimary = False
else: 
  print(highway, " is not a valid highway number.", sep="")
  


#If auxiliary, indicate what primary highway it serves.
#This is the last two digits (295 services 95, 301 services 1) 
# Maybe use modulo (%)
if isPrimary == False:
  primary = highway % 100 #divide by 100 and just keep remainder
  print("It serves highway I-", primary, ".", sep="")

#Also indicate if the (primary) highway runs north/south or east/west.
#N/s is odd, E/W is even
#We can determine odd/even with modulo 2

if highway % 2 == 0:
  #it's even
  print("The highway goes East/West.")
else:
  #it's odd
  print ("The highway goes North/South.")



