# Used for testing of small code snippets
import turtle

def f():
    turtle.forward(50)
def l():
    turtle.left(90)

turtle.onkeypress(f,"w")
turtle.onkeypress(l,"a")

turtle.listen()
turtle.mainloop()

# data = input_file.read()
# for i in range(4):
# input_file = open("Demos/sample.txt")
# while True:
#     data = input_file.readline()
#     if data == '':
#         break
#     print(">",data.strip())
# for data in input_file:
#     print(">",data.strip())

# input_file.close()

# output_file = open("Demos/temp.txt",'a')
# output_file.write("\nThis is yet another test")
# output_file.write(["one","two","three"])

# output_file.close()

# x = 55.9
# y = 3.1234567
# s = f" x = {x:10.3f} \n y = {y:10.3f} "
# print(s)