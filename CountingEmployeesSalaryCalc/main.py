#CTI 110
#P4HW2 - Salary Calculator multiples
#Lourdes Cortes
#11.9.21
#


totalEmployees = 0
sumOvertime = 0
sumRegHours = 0
sumGross = 0
keepGoing = True

while keepGoing == True:
#while name != "None" and name != "none" and name != "N" and name != "n":
    name = str(input("Enter employee's name or 'None' to terminate: "))
    if name == "None" or name == "none" or name == "n":
        # exit now, we're done
        #print("Oh, we're done!")
        keepGoing = False
        continue
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

    #print("OR")
    #employeeInfo()
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
    print()

    totalEmployees += 1
    sumOvertime += overtimePay #total ovrtme for all employees 
    sumRegHours += totalRegPay #total paid for regular wrk hrs all employees
    sumGross += grossPay #

print("Total number of employees: ", totalEmployees)
print("Total amount payed for overtime: $", format(sumOvertime, ".2f"))
print("Total amount payed for regular hours: $", format(sumRegHours, ".2f"))
print("Total amount payed in gross: $", format(sumGross, ".2f"))

