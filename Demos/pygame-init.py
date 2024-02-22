
import pygame  # Our freshly installed pygame package
import random  # Can't have a game without RNG...
MC_IMAGE = "/home/itsvm/src/its2801/Week6/Images/hood64.png"
V = 150

def place_mc():
    image = pygame.image.load(MC_IMAGE)
    rect = image.get_rect()
    rect.center = (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2)
    return [image,rect]

def show_mc(image,rect):
    screen.blit(image,rect)

def move_mc(keys,rect,time):
    if keys[pygame.K_w]:
        rect.y -= time * V

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600,800))
SCREEN_SIZE = screen.get_size()
mc_id = place_mc()
# Every game action happens in an infite loop
dt = 0
running = True
while running:
    dt_sec = dt/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
            
    move_mc(keys,mc_id[1],dt_sec)
        
    screen.fill("silver")
    show_mc(mc_id[0],mc_id[1])
    dt = clock.tick(30)

    pygame.display.flip()

pygame.quit()