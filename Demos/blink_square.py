import pygame
import random

BLUE = ("blue","darkblue","lightblue")
SIZE = 20

def create_blue(area,size):
    position = []
    for i in range(2):
        position.append(random.randint(size[i]+10,area[i]-2*size[i]-10))
    print(position)
    return pygame.Rect(position[0],position[1],size[0],size[1])

def update_blue(my_rect,the_screen):
    c = BLUE[random.randrange(len(BLUE))]
    the_screen.fill(c,my_rect)

pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("ITS 2801")
clock = pygame.time.Clock()

blue_rect = create_blue(screen_size,(SIZE,SIZE))

running = True
dt = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#
    screen.fill("silver")
    update_blue(blue_rect,screen)


    pygame.display.flip()
    dt = clock.tick(5) / 1000
