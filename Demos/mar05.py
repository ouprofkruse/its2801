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
        pos_x = random.randint(size,x-size)
        pos_y = random.randint(size,y-size)
        self.rect = pygame.Rect(pos_x,pos_y,size,size)
    def update(self):
        c = self.colors[random.randrange(0,len(self.colors))]
        self.screen.fill(c,self.rect)


pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
clock = pygame.time.Clock()

npc_blue = Color_npc(BLUE,SIZE_BLUE,screen)
npc_red = Color_npc(RED,SIZE_RED,screen)


running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
    screen.fill("silver")
    npc_blue.update()
    npc_red.update()
    
    pygame.display.flip()
    dt = clock.tick(1) / 1000

