# In this script we "manually" control the turtle
# Your script takes input from the user in an infinite loop
# Input from the user is in the form 
# code,value
# for example "f,100" means forward 100, "r,22.5" means right 22.5 degrees, etc.
###
# Your script must handle:
# f,number -- forward by that number
# l,number -- turn left by that number
# r,number -- turn right by that number
# c,color -- switch to the named color
# u -- pen up
# d -- pen down
# q -- quit
###
# The code must be accepted in upper and lower case
# User errors must not cause the script to crash or the loop to exit. Use try/except as needed.
#
# *** Extra credit: when the user type an unrecognized code, print a help message with the allowed codes
###
# Setup (we don;t need the screen dimensions, just good practice)
import turtle
height = turtle.window_height()
width = turtle.window_width()
#
# The input loop as we set it up in class
# 
while True:
    answer = input("> ")
    tokens = answer.split(",")
    if tokens[0].lower() == "q":
        break
# Fill in the remainder of the loop
# Note - we do NOT need exitonclick, the loop holds the graphics until exit