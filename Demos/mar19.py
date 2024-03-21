import turtle

class Extend_turtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
    def triangle(self,size):
        self.down
        for i in range(3):
            self.forward(size)
            self.left(120)

# my_turtle = turtle.Turtle()
my_turtle = Extend_turtle()
# my_turtle.circle(75)
my_turtle.triangle(75)

turtle.exitonclick()