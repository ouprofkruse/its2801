import turtle
# my_turtle = turtle.Turtle()
# my_turtle.circle(50)

class Extend_turtle(turtle.Turtle):
    def __init__(self):
        super().__init__()

    def triangle(self,edge):
        self.down()
        for i in range(3):
            self.forward(edge)
            self.left(120)

my_turtle = Extend_turtle()
my_turtle.triangle(50)


turtle.exitonclick()
