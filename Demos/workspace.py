# Used for testing of small code snippets
import turtle
COLORS = ("red","lightblue","green","yellow","brown","cyan")

def draw_dots(my_size,my_position):
    # size=999
    # print (size)
    turtle.up()
    turtle.goto(my_position)
    turtle.dot(my_size,"red")
    turtle.setheading(90)
    turtle.forward(my_size)
    turtle.dot(my_size,"lightblue")
    return turtle.position()
    # my_size=999
    # my_position[0]=123

size = 20
pos=[0,0]
last = draw_dots(size,pos)
print(last)
# pos=[50,100]
# draw_dots(size,pos)

turtle.exitonclick()