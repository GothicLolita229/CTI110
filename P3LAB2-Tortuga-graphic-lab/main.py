#CTI 110
#P3LAB2
#Lourdes Linares
#10.14.2021

import turtle 
t = turtle.Turtle()
t.pencolor("#003300")
t.pensize(2)
t.speed(10)

#polygon is 360 / #ofSides

#Square
#forward, right, left
for side in [1, 2, 3, 4]:
  t.forward(100)
  t.right(90)

"""t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)"""

#square end
# begin triangle
# moving higher on page
t.left(90)
t.penup()
t.forward(50)
t.pendown()

#in position
t.right(30)
t.forward(100)
for side in [1, 2]:
  t.right(120)
  t.forward(100)

"""t.right(120)
t.forward(100)"""
# end triangle

# C
t.penup()
t.forward(30)
t.right(20)
t.pendown()
t.circle(40, 240)  # draw a semicircle
# M
t.penup()
t.left(147)
t.forward(100)
t.pendown()
t.right(80)
t.forward(80)
t.left(140)
t.forward(80)
t.right(135)
t.forward(80)
t.left(140)
t.forward(80)
# L
t.penup()
t.left(289)
t.forward(50)
t.pendown()
t.forward(50)
t.right(90)
t.forward(80)

