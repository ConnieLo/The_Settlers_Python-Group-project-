import random as rnd
import itertools as itt
import pygame
from tools import hugo_hex
#from classes.ui import (SCREEN_WIDTH, SCREEN_HEIGHT) #  File "C:\PycharmProjects\The_Settlers_Python\classes\board.py", line 5, in <module> from classes.ui import hex_grid, hex_radius
# ImportError: cannot import name 'hex_grid' from partially initialized module 'classes.ui' (most likely due to a circular import) (C:\Users\maruf\PycharmProjects\The_Settlers_Python\classes\ui.py)
# I cannot import stuff we should make another class maybe called constants.py where we would store all variables such as SCREEN_WIDTH, SCREEN_HEIGHT, etc..
class Board:
    def __init__(self):
        self.tiles = self.generate_tiles()
        self.foo = "bar"

    def generate_tiles(self):
        new_tiles = []

        # The resource pool
        resources = []
        resources.extend(["sheep" for i in range(4)])
        resources.extend(["wheat" for i in range(4)])
        resources.extend(["wood" for i in range(4)])
        resources.extend(["ore" for i in range(4)])
        resources.extend(["clay" for i in range(4)])
        rnd.shuffle(resources)

        # The number tokens pool
        # There whould be two of every number between 2 and 12
        # but NO 7s, only ONE 2, and only ONE 12
        numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        rnd.shuffle(numbers)

        # Assigning the numbers and resources randomly
        for i in range(18):
            new_tiles.append((numbers[i], resources[i]))

        # Putting the desert at a random spot
        new_tiles.insert(rnd.randint(0, 18), (0, "desert"))

        return new_tiles

    def draw_board(self, _surface, hex_images, number_images):
        for i, (number, resource) in enumerate(self.tiles):
            # Draw the hexagon
            center = hex_grid.offset(*co_ords[i])
            center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)
            image = hex_images.get(resource)

            if image is not None:
                hex_surface = pygame.Surface(hex_grid.hex_size, pygame.SRCALPHA)
                image = pygame.transform.scale(image, (hex_grid.hex_size[0] - 30, hex_grid.hex_size[1] - 20))
                hex_surface.blit(image, (15, 10))
                surface_rect = hex_surface.get_rect(center=center)
                _surface.blit(hex_surface, surface_rect)

            # Draw the number
            if number != 0:
                image = number_images.get(number)
                if image is not None:
                    hex_surface = pygame.Surface(hex_grid.hex_size, pygame.SRCALPHA)
                    image = pygame.transform.scale(image, (hex_grid.hex_size[0] + 60, hex_grid.hex_size[1] + 40))
                    hex_surface.blit(image, (-30, -20))
                    surface_rect = hex_surface.get_rect(center=center)
                    _surface.blit(hex_surface, surface_rect)

#################  UI ###########################
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
# Creating a new hex grid at the center of the screen
hex_grid = hugo_hex.HexGrid(60, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
hex_radius = hex_grid.hex_size
# Grid co-ordinates
co_ords = []
co_ords += [(i, 2) for i in range(-2, 1)]
co_ords += [(i, 1) for i in range(-2, 2)]
co_ords += [(i, 0) for i in range(-2, 3)]
co_ords += [(i, -1) for i in range(-1, 3)]
co_ords += [(i, -2) for i in range(0, 3)]
####################################################

b = Board()
print(b.tiles)