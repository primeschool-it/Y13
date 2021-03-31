import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

background = pygame.image.load('img/sky.jpg')
background = pygame.transform.scale(background, (1000,1000))
tile_size = 100



maryo_group = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        image = pygame.image.load('img/maryo.png')
        left_image = pygame.transform.scale(image, (40,70))
        right_image = pygame.transform.flip(image,True, False)
        self.image = image
        self.right_image = right_image
        self.rect = image.get_rect()
        self.rect.x = 100
        self.rect.y = 830
        self.direction = 'right'
        self.execution_counter = 0

    def update(self):
        print(self.rect.x, self.rect.y)
        screen.blit(self.image,(self.rect.x, self.rect.y))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            self.rect.x = self.rect.x - 10
        if keys[pygame.K_RIGHT]:
            self.direction = 'right'
            self.rect.x = self.rect.x + 10
        if self.direction == 'left':
            screen.blit(self.right_image, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))



maryo = Player(100, 830)
maryo_group.add(maryo)

TILES_DATA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def draw():
    row_counter = 0
    for row in TILES_DATA:
        col_counter = 0
        for col in row:
            if col == 1:
                tile_img = pygame.image.load('img/tile.png')
                tile_img = pygame.transform.scale(tile_img, (100, 100))
                screen.blit(tile_img, (row_counter * tile_size, col_counter * tile_size))
            col_counter += 1
        row_counter += 1


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background, (0, 0))
    draw()
    maryo_group.update()
    pygame.display.update()
