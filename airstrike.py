"""
A red rect will fall from top of screen
a greeb rect has to move left or right not not collide with red rect
"""

import pygame
import random
pygame.init()
# Variables
WIDTH = 1200
HEIGHT = 900
# Colors
BLACK = (0, 0, 0),
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [BLACK, WHITE, RED, GREEN]

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale2x(background_img)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT - 70


spaceship_group = pygame.sprite.Group()
spaceship = Spaceship()
spaceship_group.add(spaceship)

class EnemyAsteroid(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, color):
        super(EnemyAsteroid, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos



    def update(self):
        print("self...........", self.name)
        box_width = self.rect.right - self.rect.left
        self.rect.y = self.rect.y + self.speed
        if self.name == 'BOX 17':
            self.image.fill(BLUE)
            self.speed = 5
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0,WIDTH)
            self.rect.y = 0
            ####SPEED
            # print ("disappearing.........", self.name)
            # self.kill()


asteroid_group = pygame.sprite.Group()
for i in range(5):
    rand_x = random.randint(0, WIDTH)
    rand_y = random.randint(0, HEIGHT)
    rand_width = random.randint(20,50)
    rand_height = random.randint(20, 50)
    rand_color = random.choice(COLORS)
    rand_speed = random.randint(1,2)
    asteroid = EnemyAsteroid(rand_x, rand_y, rand_width, rand_height,rand_color )
    asteroid.name = "BOX %s" %i
    asteroid.speed = rand_speed
    asteroid_group.add(asteroid)



screen = pygame.display.set_mode((WIDTH, HEIGHT))
exit_game = True
while exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False
        ## List of all pressed keys
    keys = pygame.key.get_pressed()
    ## change position of green on pressing left or right arrow key
    if keys[pygame.K_LEFT]:
        if spaceship.rect.left  > 0:
            spaceship.rect.x =  spaceship.rect.x - 10
    if keys[pygame.K_RIGHT]:
        right_border = spaceship.rect.right + 10
        if right_border < WIDTH:
            spaceship.rect.x = spaceship.rect.x + 10
    if not pygame.sprite.spritecollide(spaceship, asteroid_group, False):
        screen.blit(background_img, (0,0))
        asteroid_group.draw(screen)
        spaceship_group.draw(screen)
        asteroid_group.update()
        pygame.display.update()
