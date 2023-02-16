import pygame.draw
import hugo_hex

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Grid co-ordinates
co_ords = []
co_ords += [(i, 2) for i in range(-2, 1)]
co_ords += [(i, 1) for i in range(-2, 2)]
co_ords += [(i, 0) for i in range(-2, 3)]
co_ords += [(i, -1) for i in range(-1, 3)]
co_ords += [(i, -2) for i in range(0, 3)]

# Pygame shit
FLASH_EVENT = pygame.user_event + 2

# Creating a new hex grid at the center of the screen
hex_grid = hugo_hex.HexGrid(50, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

def main(_surface):
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        pygame.draw.polygon(_surface, (0, 0, 0,), points, width=3)
