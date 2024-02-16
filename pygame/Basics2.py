import pygame
import random
# Constants
V = .1

def place_npc(npc_rect,screen_dim):
    x = random.random()*screen_dim[0]
    y = random.random()*screen_dim[1]
    npc_rect.center = (x,y)

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file,the_screen) -> None:
        super().__init__()
        self.scr_ref = the_screen
        self.original = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.original,(64,64))
        self.rect = self.image.get_rect()
        screen_dim = self.scr_ref.get_size()
        self.rect.center = (screen_dim[0]/2,screen_dim[1]/2)
        self.velocity = V
    def update(self,coll_rect):
        if self.rect.colliderect(coll_rect):
            screen_dim = self.scr_ref.get_size()
            place_npc(coll_rect,screen_dim)
        self.scr_ref.blit(self.image,self.rect)
    def move(self,key_list,delta):
        screen_dim = self.scr_ref.get_size()
        increment = [0,0]
        for i in range(2):
            increment[i] = self.velocity * ((screen_dim[0]+screen_dim[1])/2) * delta
        if key_list[pygame.K_w]:
            self.rect.y -= increment[1]
            if self.rect.y < 0:
                self.rect.y = screen_dim[1]
        if key_list[pygame.K_s]:
            self.rect.y += increment[1]
            if self.rect.y > screen_dim[1]:
                self.rect.y = 0
        if key_list[pygame.K_a]:
            self.rect.x -= increment[0]
            if self.rect.x < 0:
                self.rect.x = screen_dim[0]
        if key_list[pygame.K_d]:
            self.rect.x += increment[0]
            if self.rect.x > screen_dim[0]:
                self.rect.x = 0

    
pygame.init()
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, 0, 1)
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("ITS 2801")
clock = pygame.time.Clock()


#print(screen_size[1])

player = Player("Images/eye.png",screen)

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    player.move(keys,dt)
    player.update(hood_rect)
    screen.blit(hood,hood_rect)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
#    print(dt)



pygame.quit()
