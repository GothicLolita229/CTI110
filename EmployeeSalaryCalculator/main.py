#CTI 110
#P3HW2 - Salary
#Lourdes Linares
#10.18.21
#

'''Ask user name of employee
Ask user to enter number of hours the employee worked this week
Ask user to enter employee's pay rate
Evaluate if employee has worked overtime. If yes calcuate amount owed
to employee for overtime hours
Calculate total employee pay for regular hours worked.
Display gross pay (total amount that should be paid to employee)
Display Employee name, pay rate,
number of hours worked, overtime hours, overtime pay , pay for regular
hours and gross pay
'''

name = str(input("Enter employee's name: "))
weeklyHours = float(input("Enter number of hours worked: "))
indvPayRate = float(input("Enter employee's pay rate: "))
overtimeRate = indvPayRate * 1.5
totalRegPay = indvPayRate * weeklyHours
#grossPay = totalRegPay + (overtime * overtimeRate)
#overtime = 
print("-" * 35)
print("Employee name: ", name)
print()

#full work week is 40 hours
if weeklyHours <= 40:
    overtime = 0
else:
    overtime = weeklyHours - 40
#calculations for overtime and total pay
grossPay = totalRegPay + (overtime * overtimeRate)
overtimePay = (overtime * overtimeRate)
"""print(overtimeRate)
print(O)"""
#table 
#format(taxTotal, "10.2f")
'''print("Hours Worked      Pay Rate     Overtime   Overtime Pay     RegHour Pay       Gross Pay")
print("-" * 100)
print(weeklyHours, "            ", indvPayRate, "       ",    overtime, "     ", format(overtimePay, "10.2f"), "    ",  format(totalRegPay, "10.2f"), "      ", format(grossPay, "10.2f"))'''

print("Hours Worked\tPay Rate\tOvertime\tOvertime Pay\tRegHour Pay\tGross Pay")
print("-" * 100)
print("$", format(weeklyHours, ".2f"), "\t  $", format(indvPayRate, ".2f"), "\t",    overtime, "\t\t  $", format(overtimePay, ".2f"), "\t  $", format(totalRegPay, ".2f"), "\t $", format(grossPay, ".2f"))
print()

#OR

print("OR")
print("-" * 100)
print("Hours Worked: $", format(weeklyHours, ".2f"))
print("-" * 30)
print("Pay Rate: $", format(indvPayRate, ".2f"))
print("-" * 30)
print("Overtime: ", format(overtime, ".2f"))
print("-" * 30)
print("Overtime Pay: $", format(overtimePay, ".2f"))
print("-" * 30)
print("Regular Hour Pay: $", format(totalRegPay, ".2f"))
print("-" * 30)
print("Gross Pay: $", format(grossPay, ".2f"))

