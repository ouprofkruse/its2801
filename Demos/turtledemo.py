from turtle import Turtle

tg = Turtle()
#tg.goto(100,100)

loops = 60
step = 500 / loops
angle = 360/loops
tg.color('red','blue')
tg.width(5)
tg.begin_fill()
for i in range(loops):
    tg.forward(step)
    tg.left(angle)
tg.end_fill()

# tg.up()
# tg.forward(100)
# tg.left(90)
# tg.down()
# tg.forward(100)
# tg.left(90)
# tg.color('red')
# tg.width(3)
# tg.forward(100)

#tg1 = Turtle()
#tg1.left(90)
#tg1.forward(50)

tg.screen.mainloop()
