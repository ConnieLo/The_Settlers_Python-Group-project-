import pygame.draw
import pygame.font
import hugo_hex
import random
from button_points import button_points

pygame.init()
# Load the image to be blitted
settle = pygame.image.load("resources/settle.png")
small_settle = pygame.transform.scale(settle, (40, 40))
#################Hexes images##############################
ORE = pygame.image.load('resources/hexType/oreHex.png')
SHEEP = pygame.image.load('resources/hexType/sheepHex.png')
CLAY = pygame.image.load('resources/hexType/clayHex.png')
WHEAT = pygame.image.load('resources/hexType/wheatHex.png')
WOOD = pygame.image.load('resources/hexType/woodHex.png')
DESERT = pygame.image.load('resources/hexType/desertHex.png')



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
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)
        number = numbers[i]

        # check if the number is equal to 7
        if number == 7:
            continue  # skip drawing this number

        # create a surface with a white circle and a transparent center
        circle_surface = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface, (255, 255, 255, 200), (20, 20), 20)

        # blit the circle surface to the main surface
        circle_rect = circle_surface.get_rect(center=center)
        _surface.blit(circle_surface, circle_rect)

        # create the number text and blit it to the main surface
        text = font.render(str(number), True, (0, 0, 0))  # creating a text instance
        text_rect = text.get_rect(center=center)  # giving coordinates
        _surface.blit(text, text_rect)  # drawing the texts



image_paths = {1: ORE, 2: ORE, 3: ORE,
               4: SHEEP, 5: SHEEP, 6: SHEEP, 7: SHEEP,
               8: CLAY, 9: CLAY, 10: CLAY,
               11: WHEAT, 12: WHEAT, 13: WHEAT, 14: WHEAT,
               15: WOOD, 16:  WOOD, 17:  WOOD, 18:  WOOD,19: WOOD }

image_paths_list = list(image_paths.items())
# shuffle the image paths to randomize the distribution of hex types
random.shuffle(image_paths_list)
image_paths = dict(image_paths_list)
print(image_paths)
def drawHex(_surface, numbers, image_paths_list, DESERT):

    # draw the images
    for i, (key, value) in enumerate(image_paths_list):
        center = hex_grid.offset(*co_ords[i])
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)
        if numbers[i] == 7:
            image = DESERT
        else:
            image = value

        # create a surface for the hex with the same size a5s the image
        hex_surface = pygame.Surface(hex_grid.hex_size, pygame.SRCALPHA)

        # draw the hexagon onto the surface
        pygame.draw.polygon(hex_surface, (0, 0, 0), hex_grid.get_hex_vertices(*co_ords[i]), width=5)

        # resize the image to fit inside the hexagon
        image = pygame.transform.scale(image, (hex_grid.hex_size[0] - 30, hex_grid.hex_size[1] - 20))

        # blit the image onto the surface
        hex_surface.blit(image, (15, 10))

        # blit the surface onto the main surface at the center coordinates
        surface_rect = hex_surface.get_rect(center=center)
        _surface.blit(hex_surface, surface_rect)
def drawButtonEdges(_surface, image):
    # Create a list to store the buttons
    buttons = []
    # Drawing the hexagons
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)

        # Create a button for each point in the points list
        for point in points:
            btn = button_points(point[0], point[1])
            buttons.append(btn)

    # Draw buttons and check for clicks
    for i, btn in enumerate(buttons):
        btn.draw(_surface)

        # Check if this button was clicked
        if btn.clicked:
            print(f"Button {i + 1} was clicked")
            # Blit the image if the button has been clicked
            _surface.blit(image, btn.rect.topleft)

            # Set the clicked attribute to True so that the image will continue to be blitted
            btn.clicked = True
        else:
            # Set the clicked attribute to False if the button is not clicked so that the image will not be blitted
            btn.clicked = False

def drawButtonMidPoints(_surface):
    # Create a list to store the buttons
    buttons = []

    # Drawing the hexagons
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        pygame.draw.polygon(_surface, (0, 0, 0,), points, width=5)

        # Create a button at the midpoint of each pair of adjacent vertices
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i+1) % len(points)]
            mid = ((p1[0]+p2[0])//2, (p1[1]+p2[1])//2)
            btn = button_points(mid[0], mid[1])
            buttons.append(btn)

    # Draw buttons and check for clicks
    for btn in buttons:
        btn.draw(_surface)

        # Check if this button was clicked
        if btn.clicked:
            print(f"Button clicked at ({btn.rect.x}, {btn.rect.y})")


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

    drawHex(_surface, numbers, image_paths_list, DESERT)

    # Draw random numbers in the center of each hexagon
    drawNumbers(_surface, numbers, font1)

    drawButtonEdges(_surface, small_settle)

    drawButtonMidPoints(_surface)



