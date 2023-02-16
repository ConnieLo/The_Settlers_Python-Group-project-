import pygame.draw
import pygame.font
import hugo_hex
import itertools

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Numbers
numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

# Grid co-ordinates
co_ords = []
co_ords += [(i, 2) for i in range(-2, 1)]
co_ords += [(i, 1) for i in range(-2, 2)]
co_ords += [(i, 0) for i in range(-2, 3)]
co_ords += [(i, -1) for i in range(-1, 3)]
co_ords += [(i, -2) for i in range(0, 3)]

# Creating a new hex grid at the center of the screen
hex_grid = hugo_hex.HexGrid(50, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


def main(_surface):
    # Drawing the hexagons
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        pygame.draw.polygon(_surface, (0, 0, 0,), points, width=3)

    for n, c in itertools.zip_longest(numbers, co_ords):
        print(n, c)
        pygame.draw.circle(_surface, (255, 0, 255), [*hex_grid.offset(*c)], 4)
