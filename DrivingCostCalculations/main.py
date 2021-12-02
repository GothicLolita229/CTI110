# Define your function here.
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):

    gas_used = driven_miles / miles_per_gallon
    #print(gas_used, "gallons spent.")
    cost = gas_used * dollars_per_gallon
    return cost

if __name__ == '__main__':
    # Type your code here.
    #miles, miles per gallon, dollars per gallon
    #program should auto check for 10, 50, and 400 miles
    #miles = float(input()) #Miles driven:
     
    MPG = float(input("Miles per gallon: ")) #Miles per gallon: 
    DPG = float(input("$ cost per gallon: ")) #$ cost per gallon: 

    milesToTest = [10, 50, 400] # use list to test options

    for miles in milesToTest:

        cost = driving_cost(miles, MPG, DPG)
        #print('{:.2f}'.format(cost))
        print("$", format(cost, ".2f"))