import pygame
import random

BLUE = ("purple","darkblue","lightblue")
SIZE = 20

class Color_npc():
    def __init__(self,colors,screen,size):
        self.screen = screen
        self.colors = colors
        (x,y) = screen.get_size()
        self.rect = pygame.Rect(random.randint(size,x-size),random.randint(size,y-size),size,size)
    def update(self):
        c = self.colors[random.randrange(len(self.colors))]
        self.screen.fill(c,self.rect)



pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("ITS 2801")
clock = pygame.time.Clock()
npc = Color_npc(BLUE,screen,SIZE)

running = True
dt = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#
    screen.fill("silver")
    npc.update()

    pygame.display.flip()
    dt = clock.tick(5) / 1000
