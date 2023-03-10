import pygame.draw
import pygame.font
import hugo_hex
import random
import math

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

# Grid co-ordinates
co_ords = []
co_ords += [(i, 2) for i in range(-2, 1)]
co_ords += [(i, 1) for i in range(-2, 2)]
co_ords += [(i, 0) for i in range(-2, 3)]
co_ords += [(i, -1) for i in range(-1, 3)]
co_ords += [(i, -2) for i in range(0, 3)]

# Creating a new hex grid at the center of the screen
hex_grid = hugo_hex.HexGrid(60, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
hex_radius = hex_grid.hex_size

def getCoordsOfCenter(): # prints out the coordinates of each vertex in the center of the hexagon
    for co in co_ords:
        center = hex_grid.offset(*co)
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)
        print(center)

#print(getCoordsOfCenter())



def getCoordsOfEdges(): # prints out the coordinates of each vertex of the hexagons' edges
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        for point in points:
            print(point)

#print(getCoordsOfEdges())


def getCoordsOfEdgesMidpoints(): # prints out the midpoint between each pair of adjacent vertices
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        for point in points:
            for i in range(len(points)):
                p1 = points[i]
                p2 = points[(i+1) % len(points)]
                mid = ((p1[0]+p2[0])//2, (p1[1]+p2[1])//2)
                print(mid)

#print(getCoordsOfEdgesMidpoints())


def drawNumbers(_surface, numbers, font, images=None):
    # draw the numbers
    for i, co in enumerate(co_ords):
        center = hex_grid.offset(*co)
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)  # adjust the x and y coordinates
        number = numbers[i]

        # create a surface with a white circle and a transparent center
        circle_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface, (255, 255, 255, 200), (20, 20), 20)  # 200 is the alpha value

        # blit the circle surface to the main surface
        circle_rect = circle_surface.get_rect(center=center)
        _surface.blit(circle_surface, circle_rect)

        # create the number text and blit it to the main surface
        text = font.render(str(number), True, (0, 0, 0))  # creating a text instance
        text_rect = text.get_rect(center=center)  # giving coordinates
        _surface.blit(text, text_rect)  # drawing the texts


def drawHex(_surface, images=None):
    if images is None:
        # default image paths
        image_paths = ['resources/hexType/clayHex.png', 'resources/hexType/desertHex.png',
                       'resources/hexType/oreHex.png', 'resources/hexType/sheepHex.png',
                       'resources/hexType/wheatHex.png', 'resources/hexType/woodHex.png']
        # load the images from the paths
        images = {path: pygame.image.load(path) for path in image_paths}

    # dictionary mapping numbers to images
    number_images = {2: images['resources/hexType/clayHex.png'], 3: images['resources/hexType/woodHex.png'], 4: images['resources/hexType/sheepHex.png'],
                     5: images['resources/hexType/oreHex.png'], 6: images['resources/hexType/oreHex.png'], 7: images['resources/hexType/desertHex.png'],
                     8: images['resources/hexType/woodHex.png'], 9: images['resources/hexType/clayHex.png'], 10: images['resources/hexType/oreHex.png'],
                     11: images['resources/hexType/sheepHex.png'], 12: images['resources/hexType/clayHex.png']}# etc

    # draw the images
    for i, co in enumerate(co_ords):
        center = hex_grid.offset(*co)
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)  # adjust the x and y coordinates
        number = numbers[i]
        image = number_images.get(number)  # get the corresponding image for the number

        if image is not None:
            # create a surface for the hex with the same size a5s the image
            hex_surface = pygame.Surface(hex_grid.hex_size, pygame.SRCALPHA)

            # draw the hexagon onto the surface
            pygame.draw.polygon(hex_surface, (0, 0, 0), hex_grid.get_hex_vertices(*co), width=5)

            # resize the image to fit inside the hexagon
            image = pygame.transform.scale(image, (hex_grid.hex_size[0] - 30, hex_grid.hex_size[1] - 20))

            # blit the image onto the surface
            hex_surface.blit(image, (15, 10))

            # blit the surface onto the main surface at the center coordinates
            surface_rect = hex_surface.get_rect(center=center)
            _surface.blit(hex_surface, surface_rect)

# Numbers
numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 7]
# shuffle the numbers in the list
random.shuffle(numbers)

print(numbers)



# font1 # I did it this way due to the performance, so it does not load up the font all the time
font1 = pygame.font.SysFont(None, 36, bold=True)  # setting up the font to be bold
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
            #print(mid) # prints out the midpoint between each pair of adjacent vertices

    drawHex(_surface)

    # Draw random numbers in the center of each hexagon
    drawNumbers(_surface, numbers, font1)

