import pygame
import random
import time

pygame.init()

# Variables
WIDTH = 800
HEIGHT = 600
#Colors
BLACK = (0, 0, 0),
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

## Game Loop

exit_game = True
r_width = 80 #Width of red square
g_width = 80 #Width of green square
r_x = random.randrange(0, WIDTH- r_width) # Position of red rect to start 1st time
r_y = 0
r_speed = 8

g_x = 400
g_y = 530
g_speed = 3

while exit_game:
    # time.sleep(1)
    ## List of events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False
    ## List of all pressed keys
    keys = pygame.key.get_pressed()
    ## change position of green on pressing left or right arrow key
    if keys[pygame.K_LEFT] and g_x > 1:
        g_x = g_x - g_speed
    if keys[pygame.K_RIGHT] and g_x < 746:
        g_x = g_x + g_speed
    r_y = r_y + r_speed
    ## reset y axis for red rect after disapparing from screen
    if r_y > 600:
        r_y = 0
        r_x = random.randrange(0, WIDTH - r_width) # Position of red rect on reappearing on screen

    ## Movements with keyboard

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (g_x, g_y, 50, 50))
    pygame.draw.rect(screen, RED, (r_x, r_y, 80, 80))
    pygame.display.update()
    clock.tick(60)
