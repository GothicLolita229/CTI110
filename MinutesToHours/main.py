minutes = int(input('Enter minutes:\n'))
hours = minutes // 60
minutes_remaining = minutes % 60

print(minutes, 'minutes is', end=' ')
print(hours, 'hours and', end=' ')
print(minutes_remaining, 'minutes.\n', end=' ')

#do the reverse
hours = int(input("Enter hours: \n"))
minutes = int(input("Enter minutes: \n"))

minutes_total = hours * 60 + minutes
print(hours, "hours and", minutes, " minutes is:")
print(minutes_total, "minutes long.")