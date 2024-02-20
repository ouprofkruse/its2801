
import pygame  # Our freshly installed pygame package
import random  # Can't have a game without RNG...
MC_IMAGE = "/home/itsvm/src/its2801/Week6/Images/hood64.png"

def place_mc():
    image = pygame.image.load(MC_IMAGE)
    rect = image.get_rect()
    rect.center = (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2)
    return [image,rect]

def show_mc(image,rect):
    screen.blit(image,rect)

pygame.init()

screen = pygame.display.set_mode((1600,800))
SCREEN_SIZE = screen.get_size()
mc_id = place_mc()
# Every game action happens in an infite loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
        
    screen.fill("silver")
    show_mc(mc_id[0],mc_id[1])

    pygame.display.flip()

pygame.quit()