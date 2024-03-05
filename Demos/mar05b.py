import pygame
import random

SIZE = 150
COLORS = ("blue","purple","orange")


class Color_npc():
    def __init__(self,color,size,the_screen):
        self.screen = the_screen
        self.color = color
        self.size = size
        (x,y) = self.screen.get_size()
        pos_x = random.randint(size,x-size)
        pos_y = random.randint(size,y-size)
        self.rect = pygame.Rect(pos_x,pos_y,size,size)
    def update(self):
        self.screen.fill(self.color,self.rect)


pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
clock = pygame.time.Clock()

npc = []
for i in range(len(COLORS)):
    npc.append(Color_npc(COLORS[i],SIZE,screen))

running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
    screen.fill("silver")

    for i in range(1,len(npc)):
        if npc[0].rect.colliderect(npc[i].rect):
            npc[i].color = "red"

    for i in range(len(npc)):
        npc[i].update()
    
    pygame.display.flip()
    dt = clock.tick(30) / 1000

