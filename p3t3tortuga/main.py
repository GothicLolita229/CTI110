#CTI 110
#P3T3_Tortuga
#Lourdes Linares
#10.5.2021
# https://docs.python.org/3/library/turtle.html

#we use import to activate turtle
import turtle

turtle.pensize(3)
turtle.color("dark green")

#Square
#forward, right, left
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
#square end
# begin triangle
# moving higher on page
turtle.left(360)
turtle.penup()
turtle.forward(50)
turtle.pendown()
#in position
turtle.right(30)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
# end triangle
# begin circle

turtle.left(90)
turtle.penup()
turtle.forward(35)
turtle.pendown()
turtle.hideturtle()
turtle.write('L M C', font=(18))
