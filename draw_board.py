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
hex_grid = hugo_hex.HexGrid(65, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


def main(_surface):
    # Drawing the hexagons
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        pygame.draw.polygon(_surface, (0, 0, 0,), points, width=5)

        # Add a dot at each vertex of the hexagon
        for point in points:
            pygame.draw.circle(_surface, (255, 0, 255), point, 8)
            # print(point) # prints out the coordinates of each vertex of the hexagons' edges
            for i in range(len(points)):
                p1 = points[i]
                p2 = points[(i+1) % len(points)]
                mid = ((p1[0]+p2[0])//2, (p1[1]+p2[1])//2)
                pygame.draw.circle(_surface, (0, 255, 94), mid, 4)
                # print(mid) # prints out the midpoint between each pair of adjacent vertices

        # Add a circle in the center of the hexagon
        center = hex_grid.offset(*co)
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2) # adjust the x and y coordinates
        pygame.draw.circle(_surface, (255, 255, 0), center, 10)
        # print(center) # prints out the coordinates of each vertex in the center of the hexagon



#    for n, c in itertools.zip_longest(numbers, co_ords):
        #print(n, c)
        #pygame.draw.circle(_surface, (255, 0, 255), [*hex_grid.offset(*c)], 4)
