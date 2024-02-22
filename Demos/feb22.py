import turtle

def f():
    turtle.forward(50)

def lt():
    turtle.left(30)

turtle.onkeypress(f,"w")
turtle.onkeypress(lt,"a")

turtle.listen()
turtle.mainloop()


# t1 = turtle.Turtle()
# t2 = turtle.Turtle()

# t1.color("red")
# t2.color("blue")

# t1.left(45)
# t2.right(45)

# t1.forward(100)
# t2.forward(100)

# turtle.exitonclick()