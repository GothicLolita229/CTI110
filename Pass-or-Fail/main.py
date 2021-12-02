#P3T1 - Pass or Fail?

#For this program, we'll start off with another simple if statement.

#Ask the user to enter a number grade (this should be between 0 and 100, although you don't have to test for this).

#Then either inform the user that it's a passing grade, or a failing grade. (As a reminder, the cutoff is 60, which is the lowest possible score for a D.)

grade = int(input('Enter number grade: '))

if grade >= 60 and grade <= 100:
  print('Passing grade!')

else:
  print('That is a failing grade. Study harder!')