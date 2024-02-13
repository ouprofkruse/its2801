# Turtle Shapes
# -------------
# This script will read a text file that contains instructions on
# shapes that are to be drawn.
# You have two sample files, week5A.txt is what you should look at first.
# The file contains these lines:
# box: -300 300 -150 200
# triangle: 0 0 50 100 100 0
# line: -225 250 50 50

# === Part 1 ===
# box 
# means draw a rectangle, the first two numbers are the (x,y) coordinates
# of the upper left corner, the last two are the (x,y) coordinates of the bottom right.

# triangle
# draws a triangle, the 6 numbers are 3 (x,y) coordinate pairs for the three corners
# of the triangle.

# line
# draws a line using the first pair of numbers as the (x,y) coordinates of the start
# and the second pair as the (x,y) coordinates of the end of the line

# Your script must draw the shapes as specified in the file -- I will test the
# script with other input files that contain different instructions.

# === Part 2 ===
# Your script must not fail/crash if there are error in the file.  The week5B.txt
# file contains a number of those errors.  
# Add code to the script to make sure your script still runs and draws the
# shapes that are correctly specified. 
# You must provide some output indicating the errors that ocurred.

# === Extra Credit ===
# As you draw each shape, check to see if any part of it will be visible in the window.
# If not, provide a warning to the user that a shape will not be visible, i.e. it is
# entirely outside the window.
# (You will need to modify the input file to test this)
# 
import turtle
height = turtle.window_height()
width = turtle.window_width()
# print(height,width)

# Define a function draw the box.  How you pass values to the function
# is up to you, "params" is a placeholder.
def draw_box(params):
    pass

# Define a function draw the triangle.  How you pass values to the function
# is up to you, "params" is a placeholder.
def draw_tri(params):
    pass
    
# Define a function draw the line.  How you pass values to the function
# is up to you, "params" is a placeholder.
def draw_line(params):
    pass

# These are files you need to test with, one per run
files = ("week5A.txt","week5B.txt")

# Open one of the files

# Loop over all lines in the file

# Inside the loop, parse the line and call the correct function to
# draw the shape

# Hold the screen until clicked
turtle.exitonclick()
