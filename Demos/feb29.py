class Npc_obj():
    def __init__(self,colors,initial_size):
        self.color_list = colors
        self.size = initial_size
    def add_color(self,color):
        self.color_list.append(color)

blue = Npc_obj(["darkblue","purple"],50)
red = Npc_obj(["red"],100)
# blue.color_list = ["darkblue","purple"]
# blue.size = 50
blue.add_color("lightblue")
print(blue.size,blue.color_list)
print(red.size,red.color_list)









# import turtle

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# t1.color("red")
# t2.color("blue")

# t1.left(45)
# t2.right(45)

# t1.forward(100)
# t2.forward(100)

# print(t1.position())
# print(t2.position())

# turtle.exitonclick()