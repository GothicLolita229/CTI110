#CTI 110
#P4t2
#Time Card
#Lourdes Linares
#10.21.21

#This program will act like a time card
#reader, adding up each day's hours to get
#the total

#Version 1 - uses numbers for days
#change line below if it's a 7 day week

DAYS_IN_WEEK = 5
totalHours = 0 # the total starts at zero

print("Please enter your hours worked.")

for day in range(DAYS_IN_WEEK):
  print("Hours for day", day+1, ": ", end="")
  hoursToday = float(input())
  totalHours = totalHours + hoursToday # add to running total

#print the total
print("You worked a total of", totalHours, "hours this week.")

#print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")



# Version 2 - using names of days 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
totalHours = 0 # the total starts at zero

print("Please enter the hours worked.")

for day in days:
  print("Hours for", day, ": ", end="")
  hoursToday = float(input())
  totalHours = totalHours + hoursToday #add  to running total

#print the total
print("You worked a total of", totalHours, "hours this week.")

#print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")