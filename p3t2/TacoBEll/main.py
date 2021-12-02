#CTI 110
#P1T3 - Receipt
#Lourdes Linares
#9.23.21

#Print a restaurant receipt
#set variables
mealCost = float(input("Cost of meal: "))
taxPct = 0.07
taxCost = mealCost * taxPct

totalCost = mealCost + taxCost

print("Thank you for dining at Grilled Ginger")
print("-" * 40)
print("Meal:  $", format(mealCost, "10.2f"))
print("Tax:   $", format(taxCost, "10.2f"))
print("-" * 40)
print("Total: $", format(totalCost, "10.2f"))