###  "Chase" mini-game - Midterm Project
#
# - At the start of the game, a number of NPCs are placed at the center of the screen,
#   the number of NPCs is controlled by a constant defined at the top of the script.
# - Each NPC moves at a random speed selected from a range set by another constant
# - Each NPC moves diagonally, the direction (up/left, up/right, down/left, or down/right) is
#   selected at random when each NPC is created, it does not change during the game.
# - When an NPC touches the edge of the screen (defined as the center of the NPC 
#   moving past the x or y coordinate defining the screen edge) it becomes invisible
#   and is no longer updated.
#   This is counted as a MISS.

# - The MC (player character) starts at the bottom of the screen, in the center.
# - The MC is moved by WASD key strokes, at a speed that is based on the top NPC speed
#   multiplied by a constant.
# - When the MC overlaps an NPC (using the colliderect function), the NPC becomes invisible
#   and stops being updated, this is counted as a HIT.
#
######
#
# This file contains the basic starting configuration and game loop we have been using, which
# includes closing the game when the window if closed or the Escape key is pressed.
#
######
# NOTE:  You can use the constants as global variables, but all other information
#        must be passed to functions as parameters and returned via the return statment.
#
#        You must use a class to define the NPCs and handle their functions
#        You must use a class to define all MC related data and functions
#
#        This project has 2 "phases" defined below
#
######  Phase I - submitted on the Sunday before Spring Break
#       Phase I can use a lot of your code from the NPCs (Week 7) project
# - Define a class for your NPCs
# -- The __init__ method contains what we have been doing in the "create" function before
#    Load the image (eye64) and retrieve its rectangle
#    Place the NPC (by placing its rectangle)
#    Select the speed and direction for the NPC
# -- Define an "update" method that takes care of:
#    moving the NPC,
#    determining if it hits the screen edge (in that case make it invisible and increment the MISS counter),
#    putting itself on the screen using the "blit" function (if it is visible)
# NOTE: you are going to need an NPC attribute that determines if the NPC is visible.
# - Before the game loop, create and store the required number of NPC objects (you will need to store them in a variable)
# - In the game loop, call the update method for each NPC
#
###### Phase II - submitted a week after we return from Spring Break (Sunday night)
# Phase II (you can "borrow" code from the "pygame-start" (Week 6) project)
# If you submit any Phase II work in Phase I, I will give you feedback w/o any grading impact
#
# - Define an MC class
# -- The __init__ method contains what we used to do in the "create" function
#    Load the MC image (hood64) and retrieve the rectangle for it
#    Place the rectangle at the starting position
#    Set a speed attribute for the MC
# -- Define a "move" method to:
#    move the MC when the w,a,s, and/or d keys are pressed,
#    check whether the MC has collided with any NPC (colliderect function),
#    set any NPC the MC has collided with to be invisible,
#    Extra credit: Increment a HIT counter
# -- Define an "update" method that displays the MC using "blit"
#
# - Before the game loop, define the MC object
# - In the game loop, call the "move" and "update" methods for the MC
#
# - when the game ends, print at least the MISS counter; print the HIT counter for extra credit
#####
# Extra Credit
#
# - Keep track of a HIT counter and print it at the end of the game
# - Keep track of the number of visible NPCs and end the game when no NPCs are left (visible)
#

import pygame
import random

# Constants
SPEED_RANGE = (50,100) # each NPC moves at a random speed selected from this range - modify as you see fit
NUM_NPC = 10 # the number of NPCs
MCV = 2 # The speed of the MC is set to the top NPC speed range times this factor - modify as you see fit.

# Initialization
pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption(" My Game")  # Replace this with a proper window title
clock = pygame.time.Clock()

running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("silver")  # Replace this with a more appropriate color (your choice)
    keys = pygame.key.get_pressed() # dictionary of all keys, True = pressed
    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000
