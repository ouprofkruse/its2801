
import pygame  # Our freshly installed pygame package
import random  # Can't have a game without RNG...


pygame.init()

screen = pygame.display.set_mode((1600,800))

# Every game action happens in an infite loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

