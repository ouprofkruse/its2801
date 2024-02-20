# BEFORE YOU START
#
# We need the python package manager "pip"
# Use:  sudo apt install python3-pip
# 
# Now we need the "pygame" python module
# Use:  python3 -m pip install pygame
# You should see:  Successfully installed pygame-2.5.2
###
# DON'T PROCEED UNTIL THE STEPS ABOVE WORKED
#
# Your Tasks:
# 1) make sure this script runs as-is (and the MC moves up with the "w" key)
# 2) experiment with the window size and the MC movement speed - pick something you like
# 3) add the remaining movement keys, using the "w" as a template
#    "a" = left, "s" = down, "d" = right
#
import pygame  # Our freshly installed pygame package
import random  # Can't have a game without RNG...
#
# The constant below point to where the images are relative to
# the working folder in VS code. The value below works for the
# 2801 repo, but you may need to change it in your work area.
IMAGE_FOLDER = "Week6/Images/"
# Now we can create a string pointing to the image(s) themselves
MC_IMAGE = IMAGE_FOLDER + "hood64.png"
#
#############################################################
# Function Definitions
#############################################################
#
def place_mc():   # initialize the MC
    image = pygame.image.load(MC_IMAGE)
    rect = image.get_rect()
    rect.center = (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2)
    return [image,rect]

def show_mc(image,rect):   # display the MC
    screen.blit(image,rect)

def move_mc(rect,keys,time):
    # "w" moves the player forward
    if keys[pygame.K_w]:
        rect.y -= time * 200


##############################################################
# Start of the main script
##############################################################
# Setting up pygame
pygame.init()
# Set the window size, called "screen" in pygame. 
# I think these values should work everywhere,
# but if the screen is too large you can make the values smaller
screen = pygame.display.set_mode((1600,800))
# The next statement sets the title of the window
pygame.display.set_caption("ITS 2801")
# Finally we get a clock running
clock = pygame.time.Clock()
# we grab the actual screen dimensions here
# normally we would do this dynamically in case the window is resized
SCREEN_SIZE = screen.get_size()  
# Place the Main Character
mc_id = place_mc()
# "dt" will be the elapsed time between frames
dt=0
# Every game action happens in an infite loop
running = True
while running:
    # this is a "polling" loop.  Here we get a list of all pending events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("silver") # set the window background color
    keys = pygame.key.get_pressed() # dictionary of all keys, True = pressed
    # quit if the Escape key is pressed
    if keys[pygame.K_ESCAPE]:
        running = False

    move_mc(mc_id[1],keys,dt)  # move the MC

    show_mc(mc_id[0],mc_id[1])  # display the MC
    dt = clock.tick(60) / 1000  # lock the game to 60fps and get the elapsed time

    pygame.display.flip() # Last step in the loop - display all changes

pygame.quit() # close out the game engine before exiting
