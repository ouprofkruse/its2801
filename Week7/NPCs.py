####  PLEASE NOTE CAREFULLY:
# You will complete this project using an approach that is not very efficient.
# The point is to set the script up in this (inefficient) way once, and next week
#  transition to the better way of solving the problem.
# You are NOT to use class definitions in this submission (we will get there next week), even
#  though Google and your favorite chatbot will tell you to do so.
# One exception: if you have practiced defining custom classes in python in a previous COURSE
#  you are free to go that route (using a class definition).
#  *** YOU MUST PUT A NOTE AT THE TOP OF THE SCRIPT IDENTIFYING THAT COURSE ***
####
#
# Requirements:
# - Display three (3) NPCs using the "eye64.png" image
# - Each NPC starts at y=100 near the top of the screen
# - Each NPC starts at a random x coordinate which must be inside the screen (visible)
# - During each frame, each NPC moves down by a random amount
# ---
# - You must write functions (most likely 3 of them) to create the initial NPCs and
#   call these functions before the game loop starts
# - You must write functions (again most likely 3) to update each NPC by moving is
#   a random amount and displaying it. You must call these functions in the game loop
# ---
# Extra Credit
# When an NPC hits the bottom of the screen, have it "loop around", 
#         i.e. appear at the top of the screen
#
# ***
# Some hints/resources: You will find examples of pretty much everything you need in 
# - the last project (even the starting point)
# - The "Agenda" aka the class notes
# - The files in the Demos folder (especially "blink_squares.py")
######
import pygame
import random

# Write your functions here

pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("NPCs")
clock = pygame.time.Clock()

# Call your functions that create the NPCs here

running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("silver")

# Call your functions that update the NPCs here

    pygame.display.flip()
    dt = clock.tick(60) / 1000
