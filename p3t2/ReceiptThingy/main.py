# calculation for internet service cost without and with 6% tax
# 9/21/2021
# CTI-110 P1HW2 - Basic Math
# Lourdes
#

# Display "Enter name of expense"
# Input expense.
# Display "Enter montly charge"
# Input monthly cost before tax
# Display "Bill", expense, "Before Tax: $", monthlyCost
# Calculate monthly tax
# Add tax to subtotal
# Calculate total monthly cost
# Calculate annual cost
# Display Monthly Tax
# Display Monthly Charge
# Display Annual Cost


expense = str(input('Enter name of expense: '))
monBill = float(input('Enter montly charge: '))

print("Bill: ", expense, "-" * 9, "Before Tax: $", format(monBill, "10.2f"))
TAXPct = 0.07
taxTotal = monBill * TAXPct
monCost = taxTotal + monBill
annCost = monCost * 12
print("Monthly Tax: ", format(taxTotal, "10.2f"))
print("Monthly Charge: ", format(monCost, "10.2f"))
print("Annual Cost: ", format(annCost, "10.2f"))
if monCost < 80:
    print("Under Budget!")