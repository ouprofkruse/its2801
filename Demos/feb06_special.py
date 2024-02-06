import turtle
height = turtle.window_height()
width = turtle.window_width()

while True:
    answer = input("> ")
    if answer.lower() == "q":
        break
    else:
        turtle.forward(float(answer))
        turtle.left(22.5)

        