# Used for testing of small code snippets

#from turtle import *
import turtle

height = turtle.window_height()
width = turtle.window_width()
print(width,height)

turtle.up()
turtle.setposition(-width/2,0)
turtle.down()
turtle.forward(width/2)

turtle.color("red")
turtle.up()
turtle.setposition(-width/2,height/2)
#turtle.right(45)
turtle.down()
turtle.goto(0,0)

turtle.exitonclick()
