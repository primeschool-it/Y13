import pygame
from pygame.color import Color
import random

pygame.init()
# Variables
WIDTH = 500
HEIGHT = 500
TILE_WIDTH = 100
TILE_HEIGHT = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill('pink')

colors = ['white', 'black', 'yellow', 'green', 'red', 'brown', 'orange', 'purple', 'gray', 'blue',
          'white', 'black', 'yellow', 'green', 'red', 'brown', 'orange', 'purple', 'gray', 'blue']


tiles_group = pygame.sprite.Group()
class Tile(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, tile_sequence):
        super(Tile, self).__init__()
        self.x = pos_x
        self.y = pos_y
        rect = pygame.draw.rect(screen, Color('black'),(pos_x, pos_y, TILE_WIDTH, TILE_HEIGHT), 2)
        self.rect = rect
        self.color = None
        self.hidden = True
        self.name = 'Tile: %s' %tile_sequence
        self.clicked_tiles = []
        self.asserted = False
        self.ticks = 0
        if not self.color:
            color = random.choice(colors)
            self.color = color
            colors.remove(color)



    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in tiles_group:
                if tile.rect.collidepoint(event.pos):
                    print ([tile.name for tile in self.clicked_tiles])
                    if len(self.clicked_tiles) < 2:
                        if not tile.asserted:
                            self.clicked_tiles.append(tile)
                            tile.show_tile()

        if len(self.clicked_tiles) == 2:
            if not self.ticks:
                self.ticks = pygame.time.get_ticks()
            tile1 = self.clicked_tiles[0]
            tile2 = self.clicked_tiles[1]
            if tile1.color == tile2.color:
                tile1.asserted = True
                tile2.asserted = True
                self.clicked_tiles.remove(tile1)
                self.clicked_tiles.remove(tile2)
            else:
                ## A little time before hiding
                if pygame.time.get_ticks() > self.ticks + 500:
                    tile1.hide_tile()
                    tile2.hide_tile()
                    self.ticks = 0



        self.paint_board()

    def show_tile(self):
        self.hidden = False
        pygame.draw.circle(screen, Color(self.color),(self.rect.center), 30)

    def hide_tile(self):
        if not self.asserted:
            self.hidden = True
            pygame.draw.circle(screen, Color('pink'),(self.rect.center), 30)
            if self in self.clicked_tiles:
                self.clicked_tiles.remove(self)

    def paint_board(self):
        print (self.clicked_tiles)
        for tile in tiles_group:
            if tile.hidden:
                tile.hide_tile()
            else:
                tile.show_tile()


tile_sequence = 1
for row in range(5):
    row = row * TILE_WIDTH
    for col in range(4):
        col = col * TILE_WIDTH
        tile = Tile(row, col, tile_sequence)
        tiles_group.add(tile)
        tile_sequence = tile_sequence + 1


running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tiles_group.update(event)
    # import time
    # time.sleep(.7)
    pygame.display.update()




