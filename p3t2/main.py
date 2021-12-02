#CTI110
#P3T2 - Nested Ifs
#Lourdes Linares
#10.5.2021


#To qualify:
#     - must have salary > 30 000
#     - must have worked current job 2+ years

#Ask user for salary and time worked at job
#Check if salary qualifies
#     If it does...
#     Check if years_worked >= 2
#         If both are true, they qualify

#Ask user for salary and time worked at job
salary = float(input('Enter salary: '))
years_worked = float(input('Enter years at current job: '))

#Check if salary qualifies
if salary >= 30000:
  #print('Salary is high enough.')
    #If it does...
    #Check if years_worked >=2
  if years_worked >=2:
      print('Congratulations! You qualify for the loan!')
  else:
      print('Sorry, your time at current job does not qualify for a loan.')

else:
  print('Sorry, salary does not qualify for this loan.')