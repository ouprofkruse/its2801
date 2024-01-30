#class notes

import turtle

def draw_dots(my_size,my_position):
    turtle.up()
    turtle.goto(my_position)
    turtle.dot(my_size,"red")
    turtle.setheading(90)
    turtle.forward(my_size)
    turtle.dot(my_size,"lightblue")
    return turtle.position()
    # DON'T DO THIS
    # my_size =800
    # my_position[0] = -500

size = 110
# x = -200
# y = -200
position = [-200,-200]
# turtle.goto(x,y)
for n in range(4):
    final_position = draw_dots(size,position)
    # print(size,position)
    # print(type(final_position))
    position[0] = final_position[0] + 100
    position[1] = final_position[1] + 100
    # x = x + 100
    # y += 100
    # turtle.goto(x,y)

# turtle.up()
# turtle.setheading(0)
# turtle.forward(100)
# draw_dots()

turtle.exitonclick()
