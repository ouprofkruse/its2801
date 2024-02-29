import pygame
import random
BLUE = ("purple","darkblue","lightblue","teal")
RED = ("red","orange","brown")
SIZE_RED = 50
SIZE_BLUE = 30

class Color_npc():
    def __init__(self,colors,size,the_screen):
        self.screen = the_screen
        self.colors = colors
        self.size = size
        (x,y) = self.screen.get_size()

def create_obj(area,size):
    position = []
    for i in range(2):
        position.append(random.randint(size[i],area[i]-size[i]))
    print(position)
    rect = pygame.Rect(position[0],position[1],size[0],size[1])
    return rect

def update_obj(colors,my_rect,my_screen):
    c = colors[random.randrange(0,len(colors))]
    my_screen.fill(c,my_rect)

pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
clock = pygame.time.Clock()

blue_rect = create_obj(screen_size,(SIZE_BLUE,2*SIZE_BLUE))
red_rect = create_obj(screen_size,(SIZE_RED,SIZE_RED))


running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
    screen.fill("silver")
    update_obj(BLUE,blue_rect,screen)
    update_obj(RED,red_rect,screen)

    pygame.display.flip()
    dt = clock.tick(1) / 1000

