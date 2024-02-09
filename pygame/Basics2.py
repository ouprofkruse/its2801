import pygame
import random

def place_npc(npc_rect,screen_dim):
    x = random.random()*screen_dim[0]
    y = random.random()*screen_dim[1]
    npc_rect.center = (x,y)

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file,screen_dim) -> None:
        super().__init__()
        self.original = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.original,(64,64))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_dim[0]/2,screen_dim[1]/2)
    def update(self,screen):
        screen.blit(self.image,self.rect)
    
pygame.init()
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, 0, 1)
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("ITS 2801")
clock = pygame.time.Clock()
V = .1

#print(screen_size[1])

player = Player("Images/eye.png",screen_size)

hood_original = pygame.image.load("Images/hood.png")
hood = pygame.transform.scale(hood_original,(64,64))
hood_rect = hood.get_rect()
place_npc(hood_rect,screen_size)

running = True
dt = 0
#i = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#
    screen.fill("silver")

    increment = [0,0]
    for i in range(2):
        increment[i] = V * ((screen_size[0]+screen_size[1])/2) * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_w]:
        player.rect.y -= increment[1]
    if keys[pygame.K_s]:
        player.rect.y += increment[1]
    if keys[pygame.K_a]:
        player.rect.x -= increment[0]
    if keys[pygame.K_d]:
        player.rect.x += increment[0]
    if keys[pygame.K_l]:
        print(screen_size,increment)

    if player.rect.colliderect(hood_rect):
        place_npc(hood_rect,screen_size)
        
    player.update(screen)
    screen.blit(hood,hood_rect)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
#    print(dt)



pygame.quit()
