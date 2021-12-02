import turtle

turtle.Screen() 

sam = turtle.Turtle("turtle")

sam.speed(100)

for x in range(5, 150, 1): # first value of x, one before last value of x, step value
  sam.circle(x)
  sam.penup() 
  sam.right(1)
  sam.forward(1)
  sam.pendown()