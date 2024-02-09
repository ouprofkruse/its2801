import pygame

pygame.init()
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, 0, 1)
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("ITS 2801")
clock = pygame.time.Clock()
V = .1

#print(screen_size[1])

eye_original = pygame.image.load("images/eye.png")
eye = pygame.transform.scale(eye_original,(64,64))
eye_rect = eye.get_rect()
eye_rect.center = (screen_size[0]/2,screen_size[1]/2)

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
        eye_rect.y -= increment[1]
    if keys[pygame.K_s]:
        eye_rect.y += increment[1]
    if keys[pygame.K_a]:
        eye_rect.x -= increment[0]
    if keys[pygame.K_d]:
        eye_rect.x += increment[0]
    if keys[pygame.K_l]:
        print(screen_size,increment)
        
    screen.blit(eye,eye_rect)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
#    print(dt)



pygame.quit()
