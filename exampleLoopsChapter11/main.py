'''i1 = 1
while i1 < 19:
  i2 = 3
  while i2 <= 9:
    print('{}{}'.format(i1, i2), end=' ')
    i2 = i2 + 3
  i1 = i1 + 10'''

'''x = 0
y = 5
z = 10
while x < y:
    if x == z:
        print('x == z')
        break
    x += 1 
else:
    print('x == y')'''


'''print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)'''


'''#void function
def printSumOf(num1, num2):
  print(num1, "+", num2, "=", num1 + num2)
  return # assumed if it's left off

#value returning function
def findSumOf(num1, num2):
  answer = num1 + num2
  return answer

def main():
  first = 2
  second = 3

  printSumOf(first, second)

  sum = findSumOf(first, second)
  print("The answer is: ", format(sum, ".2f"))

main()'''


# Define your function here 

def miles_to_laps(user_miles):
  """converts miles to laps (Which are quarter mile long)
  Input: number of miles 
  return: number of laps
  
  """
  lap_count = user_miles * 4
  return lap_count

def main():
  miles = float

  laps = miles_to_laps(miles)

  print('{:.2f}'.format(laps))


if __name__ == '__main__':
    # Type your code here. Your code must call the function.