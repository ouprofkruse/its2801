import turtle

height = turtle.window_height()
width = turtle.window_width()
print(width,height)

# turtle.color("red")
# turtle.backward(100)
# turtle.down()
turtle.color("blue")
turtle.forward(width/3)
turtle.left(130)
turtle.color("red")
turtle.forward(height/3)



turtle.exitonclick()