import pygame
import pygame.draw
import pygame.font

from classes import board
from tools import hugo_hex
from classes.button_points import button_points
import pygame.sprite
from classes.board import b, Board, tile_info_list
import pygame

pygame.init()
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Load the image to be blitted
# Using convert_alpha() method to increase the FPS rates of the game
settle = pygame.image.load("resources/settleRed.png").convert_alpha()
small_settle = pygame.transform.scale(settle, (30, 30))
#################### Numbers images ###############################
TWO = pygame.image.load('resources/numbers/Number_2.png')
THREE = pygame.image.load('resources/numbers/Number_3.png').convert_alpha()
FOUR = pygame.image.load('resources/numbers/Number_4.png').convert_alpha()
FIVE = pygame.image.load('resources/numbers/Number_5.png').convert_alpha()
SIX = pygame.image.load('resources/numbers/Number_6.png').convert_alpha()
EIGHT = pygame.image.load('resources/numbers/Number_8.png').convert_alpha()
NINE = pygame.image.load('resources/numbers/Number_9.png').convert_alpha()
TEN = pygame.image.load('resources/numbers/Number_10.png').convert_alpha()
ELEVEN = pygame.image.load('resources/numbers/Number_11.png').convert_alpha()
TWELVE = pygame.image.load('resources/numbers/Number_12.png').convert_alpha()

################# Hexes images ##############################
ORE = pygame.image.load('resources/hexType/oreHex.png').convert_alpha()
SHEEP = pygame.image.load('resources/hexType/sheepHex.png').convert_alpha()
CLAY = pygame.image.load('resources/hexType/clayHex.png').convert_alpha()
WHEAT = pygame.image.load('resources/hexType/wheatHex.png').convert_alpha()
WOOD = pygame.image.load('resources/hexType/woodHex.png').convert_alpha()
DESERT = pygame.image.load('resources/hexType/desertHex.png').convert_alpha()


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


def getCoordsOfCenter():  # prints out the coordinates of each vertex in the center of the hexagon
    for co in co_ords:
        center = hex_grid.offset(*co)
        center = (center[0] + SCREEN_WIDTH / 2, center[1] + SCREEN_HEIGHT / 2)
        print(center)
# print(getCoordsOfCenter())

def getCoordsOfEdges():  # prints out the coordinates of each vertex of the hexagons' edges
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        for point in points:
            print(point)
# print(getCoordsOfEdges())

def getCoordsOfEdgesMidpoints():  # prints out the midpoint between each pair of adjacent vertices
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        for point in points:
            for i in range(len(points)):
                p1 = points[i]
                p2 = points[(i + 1) % len(points)]
                mid = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
                print(mid)
# print(getCoordsOfEdgesMidpoints())

#def drawButtonMidPoints(_surface): #Zombie Code
    # create a surface with a white circle and a transparent center
#    circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
#    pygame.draw.circle(circle_surface, (255, 204, 203, 200), (10, 10), 10)

    # Create a list to store the buttons
#    buttons = []

    # Drawing the hexagons
#    for co in co_ords:
#        points = hex_grid.get_hex_vertices(*co)
#        pygame.draw.polygon(_surface, (0, 0, 0,), points, width=5)

        # Create a button at the midpoint of each pair of adjacent vertices
#        for i in range(len(points)):
#            p1 = points[i]
#            p2 = points[(i + 1) % len(points)]
#            mid = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
#            btn = button_points(mid[0], mid[1], circle_surface)
#            buttons.append(btn)

    # Draw buttons and check for clicks
#    for btn in buttons:
#        btn.draw(_surface)

        # Check if this button was clicked
#        if btn.clicked:
#            print(f"Button clicked at ({btn.rect.x}, {btn.rect.y})")

#################### BUTTON EDGES' MIDPOINTS - ROAD #################################
    # create a surface with a white circle and a transparent center
circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, (255, 204, 203, 200), (10, 10), 10)

#################### BUTTON EDGES - SETTLEMENT #################################
# create a surface with a white circle and a transparent center
circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, (255, 255, 255, 200), (10, 10), 10)
# Create a list to store the buttons
buttons = []

# Drawing the hexagons
for co in co_ords:
    points = hex_grid.get_hex_vertices(*co)

    # Create a button for each point in the points list
    for point in points:
        btn = button_points(point[0], point[1], circle_surface)
        buttons.append(btn)

# Variable to store the previous click state
was_clicked = [False] * len(buttons)

# An empty list to store the positions of clicked buttons
clicked_positions = []

# List to store dirty rects
dirty_rects = []

################################################################################
numberImages = {2: TWO, 3: THREE, 4: FOUR, 5: FIVE, 6: SIX, 8: EIGHT, 9: NINE, 10: TEN, 11: ELEVEN, 12: TWELVE}

hex_images = {"ore": ORE, "sheep": SHEEP, "clay": CLAY, "wheat": WHEAT, "wood": WOOD, "desert": DESERT}
################################################################################
def main(_surface, game_master):
    global dirty_rects

    # Drawing the hexagons
    for co in co_ords:
        points = hex_grid.get_hex_vertices(*co)
        pygame.draw.polygon(_surface, (0, 0, 0,), points, width=5)

    b.draw_board(_surface, hex_images, numberImages)
    #################### BUTTON EDGES' MIDPOINTS - ROAD #################################


    #################### BUTTON EDGES - SETTLEMENT/CITIES #################################
    # Draws the buttons and check for clicks
    for i, btn in enumerate(buttons):
        btn.draw(_surface)
        dirty_rects.append(btn.rect)  # Add button rect to the dirty rects list

        # Checks if the button is clicked
        clicked = btn.is_clicked()

        # If the button was not clicked in the previous frame and is clicked now, print a message
        if not was_clicked[i] and clicked:
            print(f"Settlement on the position {i + 1} has been placed")
            clicked_positions.append((btn.rect.x, btn.rect.y))

            # This finds the TileInfo object for the clicked position
            clicked_tile_info = None
            for tile_info in tile_info_list:
                if tile_info.position == i:
                    clicked_tile_info = tile_info
                    break
            # Appends the necessary information to the new_settlement() method in the game_master object
            if clicked_tile_info is not None:
                settlement_info = [(clicked_tile_info.tile_number, clicked_tile_info.resource)]
                game_master.new_settlement(settlement_info)
                # Outputs a list containing the chosen index, vertex number, tile number, and resource where the user

            # Adds the clicked position rect to the dirty rects list
            dirty_rects.append(pygame.Rect(btn.rect.x, btn.rect.y, small_settle.get_width(), small_settle.get_height()))

        # Updates the previous click state
        was_clicked[i] = clicked

        # Blits the clicked image at the stored positions
        for position in clicked_positions:
            _surface.blit(small_settle, position)
            dirty_rect = pygame.Rect(position[0], position[1], small_settle.get_width(), small_settle.get_height())
            dirty_rects.append(dirty_rect)

    # Updates only the dirty rects on the screen
    pygame.display.update(dirty_rects)

    # Clears the dirty rects list for the next frame
    dirty_rects.clear()

class crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path, alt_picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.alt_image = pygame.image.load(alt_picture_path)
        self.rect = self.image.get_rect()

    # checks for any collisions
    def check_collision(self, sprite):
        if self.rect.colliderect(sprite.rect):
            # Collision detected
            return True
        else:
            return False

    # gets the position of the mouse
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    # collision detection and image switching
    def switch_image(self, sprites=[], picture_path="resources/cursor_fist.gif", alt_image_path="resources/cursor.gif"):
        for sprite in sprites:
            if self.check_collision(sprite):
                self.image = pygame.image.load(alt_image_path)
                return
        self.image = pygame.image.load(picture_path)
