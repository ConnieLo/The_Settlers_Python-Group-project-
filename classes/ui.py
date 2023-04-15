import pygame
import pygame.draw
import pygame.font


from classes import board
from tools import hugo_hex
from classes.button_points import button_points
import pygame.sprite
from classes.board import b, Board, tile_info_list

pygame.init()
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Load the image to be blitted
# Using convert_alpha() method to increase the FPS rates of the game
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

################# Settlements images ##############################
# Loading settlement images
RedSettle = pygame.image.load("resources/settlements/settleRed.png").convert_alpha()
BlueSettle = pygame.image.load("resources/settlements/settleBlue.png").convert_alpha()
YellowSettle = pygame.image.load("resources/settlements/settleYellow.png").convert_alpha()
GreenSettle = pygame.image.load("resources/settlements/settleGreen.png").convert_alpha()

################ Road images #####################
# Load and rotate road images
RedRoad1 = pygame.image.load("resources/roads/road_red.png").convert_alpha()
RedRoad0 = pygame.transform.rotate(RedRoad1, -60.0)
RedRoad2 = pygame.transform.rotate(RedRoad1, 60.0)
BlueRoad1 = pygame.image.load("resources/roads/road_blue.png").convert_alpha()
BlueRoad0 = pygame.transform.rotate(BlueRoad1, -60.0)
BlueRoad2 = pygame.transform.rotate(BlueRoad1, 60.0)
YellowRoad1 = pygame.image.load("resources/roads/road_yellow.png").convert_alpha()
YellowRoad0 = pygame.transform.rotate(YellowRoad1, -60.0)
YellowRoad2 = pygame.transform.rotate(YellowRoad1, 60.0)
GreenRoad1 = pygame.image.load("resources/roads/road_green.png").convert_alpha()
GreenRoad0 = pygame.transform.rotate(GreenRoad1, -60.0)
GreenRoad2 = pygame.transform.rotate(GreenRoad1, 60.0)


# Mapping
settlements = {
    "red": pygame.transform.scale(RedSettle, (30, 30)),
    "blue": pygame.transform.scale(BlueSettle, (30, 30)),
    "yellow": pygame.transform.scale(YellowSettle, (30, 30)),
    "green": pygame.transform.scale(GreenSettle, (30, 30)),
}

roads = {
    "red": (pygame.transform.scale(RedRoad0, (30,30)), pygame.transform.scale(RedRoad1, (30,30)), pygame.transform.scale(RedRoad2, (30,30))),
    "blue": (pygame.transform.scale(BlueRoad0, (30,30)), pygame.transform.scale(BlueRoad1, (30,30)), pygame.transform.scale(BlueRoad2, (30,30))),
    "yellow": (pygame.transform.scale(YellowRoad0, (30,30)), pygame.transform.scale(YellowRoad1, (30,30)), pygame.transform.scale(YellowRoad2, (30,30))),
    "green": (pygame.transform.scale(GreenRoad0, (30,30)), pygame.transform.scale(GreenRoad1, (30,30)), pygame.transform.scale(GreenRoad2, (30,30)))
}

# Gets the color based on the current turn
def get_color(turn):
    colors = ["red", "blue", "green", "yellow"]
    return colors[turn % 4]

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
#print(getCoordsOfEdges())

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

def draw_error_message(screen, message, x, y, duration=1000, font_size=30, font_color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(message, True, font_color)
    screen.blit(text_surface, (x, y))
    pygame.display.update()
    pygame.time.delay(duration)

def intersection_points():
    pass

#################### BUTTON EDGES' MIDPOINTS - ROAD #################################
# create a surface with a white circle and a transparent center
circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, (255, 204, 203, 200), (10, 10), 10)
# Create a list to store the buttons
buttons_roads = []
# Create a list to store road info
road_inf = []
# Drawing the hexagons
for co in co_ords:
    points = hex_grid.get_hex_vertices(*co)
    # Create a button at the midpoint of each pair of adjacent vertices
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        mid = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
        btn_rd = button_points(mid[0], mid[1], circle_surface)
        buttons_roads.append(btn_rd)
        if i==0 or i==3:       #stores the two ends and int to later determine the rotation of road image, accessible by index
            road_inf.append(((p1, p2), 0))
        elif i==1 or i==4:
            road_inf.append(((p1, p2), 1))
        elif i==2 or i==5:
            road_inf.append(((p1, p2), 2))

#Variable to store previous click state
was_clicked_roads = [False] * len(buttons_roads)

#An empty list to store the position of clicked buttons
clicked_positions_roads = []


    # Draw buttons and check for clicks
#    for btn in buttons:
#        btn.draw(_surface)

        # Check if this button was clicked
#        if btn.clicked:
#            print(f"Button clicked at ({btn.rect.x}, {btn.rect.y})")'''

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

#an empty list to store positions to be blitted
blitting_positions = []

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
    current_color = get_color(game_master.current_turn)
    for i, btn in enumerate(buttons_roads):
        btn.draw(_surface)
        dirty_rects.append(btn.rect) #adds button to dirty rect list

        #checks if road was clicked
        clicked_road = btn.is_clicked()

        # If the button was not clicked in the previous frame and is clicked now
        if not was_clicked_roads[i] and clicked_road and game_master.turn_inst.rolled:
            road_info = road_inf[i]
            print(game_master.turn_inst.rolled)
            current_color = get_color(game_master.current_turn)
            dup_count = 0 #variable to check if the settlement is already in position
            new_road = False 
            for pos in clicked_positions_roads:
                    if (pos[0], pos[1]) == (btn.rect.x, btn.rect.y):
                        dup_count += 1
                        break
            if dup_count == 0:
                new_road = True
                

            # This finds the TileInfo object for the clicked position
            clicked_tile_info = None
            for tile_info in tile_info_list:
                if tile_info.position == i:
                    clicked_tile_info = tile_info
                    break
            # Appends the necessary information to the new_settlement() method in the game_master object
            if clicked_tile_info is not None:
                print(clicked_positions)
                if new_road:
                    if game_master.initialised:
                        game_master.new_road(game_master.turn_queue[game_master.current_turn % 4], road_info[0])
                        clicked_positions_roads.append((btn.rect.x, btn.rect.y, current_color, road_info[1]))
                    elif (game_master.turn_queue[game_master.current_turn % 4].number_of_roads == 0 and game_master.turn_queue[game_master.current_turn % 4].number_of_settlements == 1)\
                        or (game_master.turn_queue[game_master.current_turn % 4].number_of_roads == 1 and game_master.turn_queue[game_master.current_turn % 4].number_of_settlements == 2):
                        game_master.new_road(game_master.turn_queue[game_master.current_turn % 4], road_info[0])
                        clicked_positions_roads.append((btn.rect.x, btn.rect.y, current_color, road_info[1]))
                        if game_master.turn_queue[game_master.current_turn % 4].number_of_settlements == 2 == game_master.turn_queue[game_master.current_turn % 4].number_of_roads:
                            game_master.turn_queue[game_master.current_turn % 4].initialised = True
                            if game_master.current_turn == 3:
                                game_master.initialised = True
                            game_master.next_turn()

            # Adds the clicked position rect to the dirty rects list
            road = roads[current_color][road_inf[i][1]]

            dirty_rects.append(pygame.Rect(btn.rect.x, btn.rect.y, road.get_width(), road.get_height()))

        # Updates the previous click state
        was_clicked_roads[i] = clicked_road


    #################### BUTTON EDGES - SETTLEMENT/CITIES #################################
    # Initialize small_settle with a default value
    current_color = get_color(game_master.current_turn)
    small_settle = settlements[current_color]

    # Draws the buttons and check for clicks
    for i, btn in enumerate(buttons):
        btn.draw(_surface)
        dirty_rects.append(btn.rect)  # Adds button rect to the dirty rects list

        # Checks if the button is clicked
        clicked = btn.is_clicked()

        # If the button was not clicked in the previous frame and is clicked now
        if not was_clicked[i] and clicked and game_master.turn_inst.rolled:
            print(game_master.turn_inst.rolled)
            current_color = get_color(game_master.current_turn)
            #print(f"Settlement on the position {i + 1} has been placed") # Print a message
            dup_count = 0 #variable to check if the settlement is already in position
            for pos in clicked_positions:
                    if (pos[0], pos[1]) == (btn.rect.x, btn.rect.y):
                        dup_count += 1
                    if dup_count == 3:
                        break
            if not (dup_count >= 3):
                clicked_positions.append((btn.rect.x, btn.rect.y, current_color))

            # This finds the TileInfo object for the clicked position
            clicked_tile_info = None
            for tile_info in tile_info_list:
                if tile_info.position == i:
                    clicked_tile_info = tile_info
                    break
            # Appends the necessary information to the new_settlement() method in the game_master object
            if clicked_tile_info is not None:
                settlement_info = [(clicked_tile_info.tile_number, clicked_tile_info.resource)]
                #if dup_count >= 3: #does not place settlement if 3 copies are present
                   # draw_error_message(screen, "Settlement cannot be placed there.", x=10, y=220)
                if dup_count == 2: #only places if 2 other copies are present; won't place on outer vertices
                    if game_master.initialised:
                        game_master.new_settlement(game_master.turn_queue[game_master.current_turn % 4], settlement_info)
                        blitting_positions.append((btn.rect.x, btn.rect.y, current_color))
                    elif game_master.turn_queue[game_master.current_turn % 4].number_of_settlements == 0 \
                        or ((game_master.turn_queue[game_master.current_turn % 4].number_of_roads == 1 and game_master.turn_queue[game_master.current_turn % 4].number_of_settlements == 1)):
                        game_master.new_settlement(game_master.turn_queue[game_master.current_turn % 4], settlement_info)
                        blitting_positions.append((btn.rect.x, btn.rect.y, current_color))

            # Adds the clicked position rect to the dirty rects list
            small_settle = settlements[current_color]
            dirty_rects.append(pygame.Rect(btn.rect.x, btn.rect.y, small_settle.get_width(), small_settle.get_height()))

        # Updates the previous click state
        was_clicked[i] = clicked

    # Blits the clicked image at the stored positions
    for x, y, color in blitting_positions:
        small_settle = settlements[color]
        _surface.blit(small_settle, (x, y))
        dirty_rect = pygame.Rect(x, y, small_settle.get_width(), small_settle.get_height())
        dirty_rects.append(dirty_rect)
    
    #blits the clicked roads
    for x, y, colour, rot in clicked_positions_roads:
        road = roads[colour][rot]
        _surface.blit(road, (x, y))
        dirty_rect = pygame.Rect(x, y, road.get_width(), road.get_height())
        dirty_rects.append(dirty_rect)
    


    # Updates only the dirty rects on the screen
    #pygame.display.update(dirty_rects)

    # Clears the dirty rects list for the next frame
    dirty_rects.clear()
    #################### BUTTON EDGES - SETTLEMENT/CITIES - END #################################

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
